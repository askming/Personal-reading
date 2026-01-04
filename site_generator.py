#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static site generator for reading notes
Converts markdown files to HTML with navigation and TOC
"""

import os
import json
import markdown
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

BOOK_DIR = 'book'
OUTPUT_DIR = 'book/_site'
YEARS = ['2026', '2025', '2024', '2023', '2022', '2021', '2020', '2019']


def get_markdown_files() -> Dict[str, List[str]]:
    """Get all markdown files organized by year"""
    files_by_year = {}
    
    for year in YEARS:
        year_dir = os.path.join(BOOK_DIR, year)
        if os.path.exists(year_dir):
            files = sorted([f for f in os.listdir(year_dir) if f.endswith('.md')])
            if files:
                files_by_year[year] = files
    
    return files_by_year


def extract_headings(md_content: str) -> List[Tuple[int, str, str]]:
    """Extract headings from markdown content for TOC
    Returns list of (level, text, anchor_id)
    """
    headings = []
    for line in md_content.split('\n'):
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            text = line.lstrip('# ').strip()
            # Create anchor ID from text
            anchor_id = text.lower().replace(' ', '-').replace('[', '').replace(']', '')
            headings.append((level, text, anchor_id))
    
    return headings


def markdown_to_html(md_content: str) -> str:
    """Convert markdown to HTML with anchor IDs for headings"""
    md = markdown.Markdown(
        extensions=['tables', 'fenced_code', 'codehilite']
    )
    html = md.convert(md_content)
    
    # Add anchor IDs to headings
    lines = html.split('\n')
    result = []
    for line in lines:
        if line.strip().startswith('<h'):
            # Extract heading level and content
            import re
            match = re.match(r'<h(\d)>(.*?)</h\d>', line)
            if match:
                level = match.group(1)
                content = match.group(2)
                anchor_id = content.lower().replace(' ', '-').replace('[', '').replace(']', '')
                line = f'<h{level} id="{anchor_id}">{content}</h{level}>'
        result.append(line)
    
    return '\n'.join(result)


def generate_toc_html(headings: List[Tuple[int, str, str]]) -> str:
    """Generate table of contents HTML"""
    if not headings:
        return '<div class="toc-empty">No headings found</div>'
    
    html = '<nav class="toc">\n<ul>\n'
    current_level = 1
    
    for level, text, anchor_id in headings:
        if level < 1 or level > 6:
            continue
        
        # Adjust indentation
        if level > current_level:
            for _ in range(level - current_level):
                html += '<ul>\n'
        elif level < current_level:
            for _ in range(current_level - level):
                html += '</ul>\n'
        
        current_level = level
        html += f'<li><a href="#{anchor_id}">{text}</a></li>\n'
    
    # Close remaining lists
    for _ in range(current_level - 1):
        html += '</ul>\n'
    
    html += '</ul>\n</nav>'
    return html


def generate_sidebar_html(files_by_year: Dict[str, List[str]], current_file: str = None) -> str:
    """Generate sidebar navigation HTML"""
    html = '<aside class="sidebar-left">\n<div class="sidebar-content">\n'
    
    for year in YEARS:
        if year in files_by_year:
            html += f'<div class="year-section">\n<h3 class="year-title">{year}</h3>\n<ul>\n'
            
            for filename in files_by_year[year]:
                filepath = f'{year}/{filename[:-3]}'  # Remove .md extension
                is_current = (filepath == current_file)
                css_class = ' active' if is_current else ''
                file_title = filename[:-3]  # Remove .md extension
                html += f'<li><a href="/{filepath}.html" class="nav-link{css_class}">{file_title}</a></li>\n'
            
            html += '</ul>\n</div>\n'
    
    html += '</div>\n</aside>'
    return html


def generate_page_html(title: str, content_html: str, toc_html: str, 
                      files_by_year: Dict[str, List[str]], current_file: str) -> str:
    """Generate complete page HTML"""
    
    template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Reading Notes</title>
    <link rel="stylesheet" href="/assets/style.css">
</head>
<body>
    <header class="navbar">
        <div class="navbar-container">
            <div class="logo"><a href="/">Reading Notes</a></div>
            <nav class="navbar-nav">
                <a href="/" class="nav-item">Home</a>
                <a href="/about.html" class="nav-item">About</a>
                <a href="https://github.com/askming/Personal-reading" class="nav-item" target="_blank">GitHub</a>
            </nav>
        </div>
    </header>

    <div class="container">
        {sidebar}
        
        <main class="main-content">
            <article class="article">
                <h1>{title}</h1>
                {content}
            </article>
        </main>

        <aside class="sidebar-right">
            <div class="toc-title">Table of Contents</div>
            {toc}
        </aside>
    </div>

    <footer class="footer">
        <p>Generated on {timestamp}</p>
    </footer>

    <script src="/assets/script.js"></script>
</body>
</html>'''
    
    sidebar_html = generate_sidebar_html(files_by_year, current_file)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return template.format(
        title=title,
        sidebar=sidebar_html,
        content=content_html,
        toc=toc_html,
        timestamp=timestamp
    )


def generate_index_page(files_by_year: Dict[str, List[str]]) -> str:
    """Generate home page"""
    content = '<div class="home-content">\n<h2>Welcome to Reading Notes</h2>\n'
    content += '<p>Explore reading summaries organized by year.</p>\n'
    content += '<div class="year-stats">\n'
    
    total_books = sum(len(files) for files in files_by_year.values())
    content += f'<div class="stat"><span class="stat-number">{total_books}</span><span class="stat-label">Books Read</span></div>\n'
    
    for year in YEARS:
        if year in files_by_year:
            count = len(files_by_year[year])
            content += f'<div class="stat"><span class="stat-number">{count}</span><span class="stat-label">{year}</span></div>\n'
    
    content += '</div>\n</div>'
    
    sidebar_html = generate_sidebar_html(files_by_year)
    
    template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reading Notes</title>
    <link rel="stylesheet" href="/assets/style.css">
</head>
<body>
    <header class="navbar">
        <div class="navbar-container">
            <div class="logo"><a href="/">Reading Notes</a></div>
            <nav class="navbar-nav">
                <a href="/" class="nav-item active">Home</a>
                <a href="/about.html" class="nav-item">About</a>
                <a href="https://github.com/askming/Personal-reading" class="nav-item" target="_blank">GitHub</a>
            </nav>
        </div>
    </header>

    <div class="container">
        {sidebar}
        
        <main class="main-content">
            <article class="article">
                {content}
            </article>
        </main>

        <aside class="sidebar-right">
            <div class="toc-title">Statistics</div>
            <div class="stats-panel">
                <p>Total books: <strong>{total}</strong></p>
            </div>
        </aside>
    </div>

    <footer class="footer">
        <p>Generated on {timestamp}</p>
    </footer>

    <script src="/assets/script.js"></script>
</body>
</html>'''
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return template.format(
        sidebar=sidebar_html,
        content=content,
        total=total_books,
        timestamp=timestamp
    )


def generate_about_page(files_by_year: Dict[str, List[str]]) -> str:
    """Generate about page"""
    content = '''<div class="about-content">
<h2>About This Project</h2>
<p>This is a personal collection of reading notes and summaries of books I've read.</p>
<h3>How to Use</h3>
<ul>
    <li>Browse the sidebar on the left to find books by year</li>
    <li>Click on any book to view the full reading notes</li>
    <li>Use the table of contents on the right to navigate within a document</li>
</ul>
<h3>Source</h3>
<p>The source code for this website is available on <a href="https://github.com/askming/Personal-reading">GitHub</a>.</p>
</div>'''
    
    sidebar_html = generate_sidebar_html(files_by_year, 'about')
    
    template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About - Reading Notes</title>
    <link rel="stylesheet" href="/assets/style.css">
</head>
<body>
    <header class="navbar">
        <div class="navbar-container">
            <div class="logo"><a href="/">Reading Notes</a></div>
            <nav class="navbar-nav">
                <a href="/" class="nav-item">Home</a>
                <a href="/about.html" class="nav-item active">About</a>
                <a href="https://github.com/askming/Personal-reading" class="nav-item" target="_blank">GitHub</a>
            </nav>
        </div>
    </header>

    <div class="container">
        {sidebar}
        
        <main class="main-content">
            <article class="article">
                {content}
            </article>
        </main>

        <aside class="sidebar-right">
        </aside>
    </div>

    <footer class="footer">
        <p>Generated on {timestamp}</p>
    </footer>

    <script src="/assets/script.js"></script>
</body>
</html>'''
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return template.format(
        sidebar=sidebar_html,
        content=content,
        timestamp=timestamp
    )


def main():
    """Generate the static site"""
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Create assets directory
    assets_dir = os.path.join(OUTPUT_DIR, 'assets')
    os.makedirs(assets_dir, exist_ok=True)
    
    # Get all markdown files
    files_by_year = get_markdown_files()
    
    # Generate home page
    print("Generating home page...")
    with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(generate_index_page(files_by_year))
    
    # Generate about page
    print("Generating about page...")
    with open(os.path.join(OUTPUT_DIR, 'about.html'), 'w', encoding='utf-8') as f:
        f.write(generate_about_page(files_by_year))
    
    # Generate pages for each reading note
    total_pages = 0
    for year, files in files_by_year.items():
        year_dir = os.path.join(OUTPUT_DIR, year)
        os.makedirs(year_dir, exist_ok=True)
        
        for filename in files:
            md_file = os.path.join(BOOK_DIR, year, filename)
            
            with open(md_file, 'r', encoding='utf-8') as f:
                md_content = f.read()
            
            # Convert markdown to HTML
            content_html = markdown_to_html(md_content)
            
            # Extract headings for TOC
            headings = extract_headings(md_content)
            toc_html = generate_toc_html(headings)
            
            # Generate page
            title = filename[:-3]  # Remove .md extension
            current_file = f'{year}/{filename[:-3]}'
            page_html = generate_page_html(title, content_html, toc_html, files_by_year, current_file)
            
            # Write to file
            output_file = os.path.join(year_dir, filename[:-3] + '.html')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(page_html)
            
            total_pages += 1
            print(f"  Generated: {year}/{filename}")
    
    print(f"\nGenerated {total_pages} pages successfully!")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == '__main__':
    main()
