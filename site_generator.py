#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static site generator for reading notes
Converts markdown files to HTML with navigation and TOC
"""

import os
import json
import re
import markdown
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

BOOK_DIR = 'book'
OUTPUT_DIR = 'book/_site'
# Base path for GitHub Pages project repository
# Change this to '' if using a user/org page (askming.github.io)
BASE_PATH = '/Personal-reading'


def get_markdown_files() -> Dict[str, List[str]]:
    """Get all markdown files organized by year (dynamically discovered)"""
    files_by_year = {}
    
    # Dynamically discover years from the file system
    if os.path.exists(BOOK_DIR):
        for item in os.listdir(BOOK_DIR):
            item_path = os.path.join(BOOK_DIR, item)
            # Check if it's a directory and looks like a year (4 digits)
            if os.path.isdir(item_path) and item.isdigit() and len(item) == 4:
                files = sorted([f for f in os.listdir(item_path) if f.endswith('.md')])
                if files:
                    files_by_year[item] = files
    
    # Return sorted by year in ascending order (oldest first)
    return dict(sorted(files_by_year.items()))
    
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


def extract_margin_notes(md_content: str) -> Tuple[str, List[Dict[str, str]]]:
    """Extract margin notes from markdown content
    Returns (cleaned_content, margin_notes_list)
    
    Margin notes are formatted as:
    ```{margin} [Title](url)
    Content line 1
    Content line 2
    ...
    ```
    """
    margin_notes = []
    
    # Pattern to match ```{margin} blocks
    pattern = r'```\{margin\}\s*\n(.*?)\n```'
    
    def replace_margin(match):
        full_content = match.group(1)
        lines = full_content.split('\n')
        
        # First line may contain a link [Text](url)
        first_line = lines[0].strip()
        remaining_lines = lines[1:] if len(lines) > 1 else []
        
        # Convert markdown link to HTML in first line
        html_content = ''
        if first_line:
            def convert_link(m):
                text = m.group(1)
                url = m.group(2)
                return f'<a href="{url}" target="_blank"><strong>{text}</strong></a>'
            
            first_line_html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', convert_link, first_line)
            html_content += f'<p>{first_line_html}</p>\n'
        
        # Add remaining lines as paragraphs
        for line in remaining_lines:
            line = line.strip()
            if line:
                html_content += f'<p>{line}</p>\n'
        
        margin_notes.append({
            'content': html_content.rstrip()
        })
        # Return empty string to remove the margin block from content
        return ''
    
    cleaned_content = re.sub(pattern, replace_margin, md_content, flags=re.DOTALL)
    
    return cleaned_content, margin_notes


def markdown_to_html(md_content: str) -> Tuple[str, List[Dict[str, str]]]:
    """Convert markdown to HTML with anchor IDs for headings, inline margin notes, and footnotes
    
    Returns (html_content, margin_notes)
    """
    # First extract margin notes
    cleaned_content, margin_notes = extract_margin_notes(md_content)
    
    md = markdown.Markdown(
        extensions=['tables', 'fenced_code', 'codehilite', 'footnotes']
    )
    html = md.convert(cleaned_content)
    
    # Add anchor IDs to headings that don't already have links
    lines = html.split('\n')
    result = []
    for line in lines:
        if line.strip().startswith('<h'):
            # Extract heading level and content
            match = re.match(r'<h(\d)>(.*?)</h\d>', line)
            if match:
                level = match.group(1)
                content = match.group(2)
                # Only add ID if there's no link in the heading (i.e., no <a> tag)
                if '<a' not in content:
                    anchor_id = content.lower().replace(' ', '-').replace('[', '').replace(']', '')
                    line = f'<h{level} id="{anchor_id}">{content}</h{level}>'
        result.append(line)
    
    return '\n'.join(result), margin_notes


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
    
    for year in files_by_year:
        html += f'<div class="year-section">\n<h3 class="year-title">{year}</h3>\n<ul>\n'
        
        for filename in files_by_year[year]:
            filepath = f'{year}/{filename[:-3]}'  # Remove .md extension
            is_current = (filepath == current_file)
            css_class = ' active' if is_current else ''
            file_title = filename[:-3]  # Remove .md extension
            html += f'<li><a href="{BASE_PATH}/{filepath}.html" class="nav-link{css_class}">{file_title}</a></li>\n'
        
        html += '</ul>\n</div>\n'
    
    html += '</div>\n</aside>'
    return html


def generate_page_html(title: str, content_html: str, toc_html: str, 
                      files_by_year: Dict[str, List[str]], current_file: str,
                      margin_notes: List[Dict[str, str]] = None) -> str:
    """Generate complete page HTML"""
    
    if margin_notes is None:
        margin_notes = []
    
    # Generate margin notes HTML for right sidebar
    margin_html = ''
    if margin_notes:
        margin_html = '<div class="margin-notes">\n'
        for note in margin_notes:
            margin_html += f'<div class="margin-note">\n{note["content"]}\n</div>\n'
        margin_html += '</div>\n'
    
    template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - MY's Readings</title>
    <link rel="stylesheet" href="{base_path}/assets/style.css">
</head>
<body>
    <header class="navbar">
        <div class="navbar-container">
            <div class="logo"><a href="{base_path}/">MY's Readings</a></div>
            <nav class="navbar-nav">
                <a href="{base_path}/" class="nav-item">Home</a>
                <a href="{base_path}/about.html" class="nav-item">About</a>
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
            <div class="toc-title">Table of Contents</div>
            {toc}
            {margin}
        </aside>
    </div>

    <footer class="footer">
        <p>Generated on {timestamp}</p>
    </footer>

    <script src="{base_path}/assets/script.js"></script>
</body>
</html>'''
    
    sidebar_html = generate_sidebar_html(files_by_year, current_file)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return template.format(
        title=title,
        sidebar=sidebar_html,
        content=content_html,
        toc=toc_html,
        margin=margin_html,
        timestamp=timestamp,
        base_path=BASE_PATH
    )


def generate_index_page(files_by_year: Dict[str, List[str]]) -> str:
    """Generate home page"""
    content = '<div class="home-content">\n'
    content += f'<img src="{BASE_PATH}/assets/logo.png" alt="Logo" class="home-logo">\n'
    content += '<h2>Welcome to My Reading Site!</h2>\n'
    
    total_books = sum(len(files) for files in files_by_year.values())
    
    # Prepare data for bar chart
    years_with_data = list(files_by_year.keys())  # Already sorted by get_markdown_files()
    book_counts = [len(files_by_year[year]) for year in years_with_data]
    
    # Create chart data as JSON
    chart_data = json.dumps({
        'labels': years_with_data,
        'counts': book_counts
    })
    
    content += '<div class="chart-container">\n'
    content += '<canvas id="statsChart"></canvas>\n'
    content += '</div>\n'
    content += f'<div class="total-stats"><p>Total books read since 2019: <strong>{total_books}</strong></p></div>\n'
    
    sidebar_html = generate_sidebar_html(files_by_year)
    
    template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MY's Readings</title>
    <link rel="stylesheet" href="{base_path}/assets/style.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>
</head>
<body>
    <header class="navbar">
        <div class="navbar-container">
            <div class="logo"><a href="{base_path}/">MY's Readings</a></div>
            <nav class="navbar-nav">
                <a href="{base_path}/" class="nav-item active">Home</a>
                <a href="{base_path}/about.html" class="nav-item">About</a>
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
    </div>

    <footer class="footer">
        <p>Generated on {timestamp}</p>
    </footer>

    <script src="{base_path}/assets/script.js"></script>
    <script>
        // Create minimalistic bar chart
        const chartData = {chart_data};
        const ctx = document.getElementById('statsChart').getContext('2d');
        const chart = new Chart(ctx, {{
            type: 'bar',
            data: {{
                labels: chartData.labels,
                datasets: [{{
                    label: 'Books Read',
                    data: chartData.counts,
                    backgroundColor: '#3498db',
                    borderColor: 'transparent',
                    borderWidth: 0,
                    borderRadius: 2
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: true,
                indexAxis: 'x',
                scales: {{
                    x: {{
                        grid: {{
                            display: false
                        }}
                    }},
                    y: {{
                        beginAtZero: true,
                        max: Math.max(...chartData.counts) + 1,
                        ticks: {{
                            stepSize: 1,
                            callback: function(value) {{
                                return Number.isInteger(value) ? value : '';
                            }}
                        }},
                        grid: {{
                            color: 'rgba(0, 0, 0, 0.05)',
                            drawBorder: false
                        }}
                    }}
                }},
                plugins: {{
                    legend: {{
                        display: false
                    }},
                    tooltip: {{
                        backgroundColor: 'rgba(44, 62, 80, 0.9)',
                        padding: 8,
                        titleFont: {{
                            size: 12
                        }},
                        bodyFont: {{
                            size: 12
                        }},
                        callbacks: {{
                            label: function(context) {{
                                return context.parsed.y + ' book' + (context.parsed.y !== 1 ? 's' : '');
                            }},
                            title: function() {{
                                return '';
                            }}
                        }}
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>'''
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return template.format(
        sidebar=sidebar_html,
        content=content,
        timestamp=timestamp,
        base_path=BASE_PATH,
        chart_data=chart_data
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
    <title>About - MY's Readings</title>
    <link rel="stylesheet" href="{base_path}/assets/style.css">
</head>
<body>
    <header class="navbar">
        <div class="navbar-container">
            <div class="logo"><a href="{base_path}/">MY's Readings</a></div>
            <nav class="navbar-nav">
                <a href="{base_path}/" class="nav-item">Home</a>
                <a href="{base_path}/about.html" class="nav-item active">About</a>
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
    </div>

    <footer class="footer">
        <p>Generated on {timestamp}</p>
    </footer>

    <script src="{base_path}/assets/script.js"></script>
</body>
</html>'''
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return template.format(
        sidebar=sidebar_html,
        content=content,
        timestamp=timestamp,
        base_path=BASE_PATH
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
            
            # Convert markdown to HTML with inline margin notes
            content_html, margin_notes = markdown_to_html(md_content)
            
            # Extract headings for TOC
            headings = extract_headings(md_content)
            toc_html = generate_toc_html(headings)
            
            # Generate page
            title = filename[:-3]  # Remove .md extension
            current_file = f'{year}/{filename[:-3]}'
            page_html = generate_page_html(title, content_html, toc_html, files_by_year, current_file, margin_notes)
            
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
