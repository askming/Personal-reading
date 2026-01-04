# Static Site Generator for Reading Notes

This project uses a custom Python script to generate a static website from markdown reading notes.

## Features

- **Top Navigation**: Home, About, and GitHub links
- **Left Sidebar**: Browse reading notes organized by year
- **Main Content**: Full markdown content with proper formatting
- **Right Sidebar**: Automatic table of contents for each document
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Interactive TOC**: Click to jump to sections, auto-highlighting based on scroll

## Project Structure

```
.
├── book/
│   ├── 2019/
│   │   └── *.md (reading notes)
│   ├── 2020/
│   │   └── *.md
│   ├── ...
│   ├── 2025/
│   │   └── *.md
│   ├── 2026/
│   │   └── *.md
│   └── _site/ (generated HTML output)
│       ├── assets/
│       │   ├── style.css
│       │   └── script.js
│       ├── YYYY/
│       │   └── *.html
│       ├── index.html
│       └── about.html
├── site_generator.py (main generator script)
├── requirements.txt
├── main.py (GitHub issue processor)
└── .github/workflows/generate_note_from_issue.yml
```

## Local Development

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Generate the Site

```bash
python site_generator.py
```

This will create the `book/_site/` directory with all HTML files.

### 3. View the Site Locally

You can serve the generated site using Python's built-in HTTP server:

```bash
cd book/_site
python -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

## GitHub Actions Workflow

The workflow automatically:

1. Triggers on:
   - Issue creation/editing
   - Issue comment creation/editing
   - Push to master (if main.py changes)
   - Manual workflow dispatch

2. Processes:
   - Generates markdown from GitHub issues (via main.py)
   - Converts all markdown to HTML using site_generator.py
   - Deploys to GitHub Pages

## Customization

### Styling

Edit `book/_site/assets/style.css` to customize colors and layout.

Key CSS variables:
```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --sidebar-width: 250px;
    --toc-width: 250px;
}
```

### Site Generator

Modify `site_generator.py` to:
- Change markdown parsing options
- Customize HTML templates
- Add new pages (e.g., categories)
- Modify TOC generation

## Deployment

Push to the `master` branch:

```bash
git add .
git commit -m "Update reading notes"
git push origin master
```

The GitHub Actions workflow will:
1. Run the site generator
2. Deploy to `gh-pages` branch
3. GitHub Pages will serve your site automatically

Your site will be available at: `https://github.com/askming/Personal-reading/`

(Enable GitHub Pages in your repository settings and set it to use the `gh-pages` branch)

## Markdown Format

Your reading notes should be in the standard markdown format. The generator will:
- Extract headings automatically for TOC
- Support code blocks with syntax highlighting
- Format lists, quotes, and tables
- Preserve links and formatting

Example:

```markdown
# Book Title

Started: 2025-01-01

## Main Ideas
- Idea 1
- Idea 2

## Key Takeaways
This is important.

### Subpoint
More details here.
```

## Troubleshooting

**No HTML generated?**
- Check that markdown files are in the correct directory structure (book/YYYY/*.md)
- Ensure file encoding is UTF-8

**Assets not loading?**
- Verify that style.css and script.js are in `book/_site/assets/`
- Check browser console for errors

**TOC not appearing?**
- Ensure your markdown has headings (# # ##, etc.)
- The generator extracts headings automatically

## Future Enhancements

Potential improvements:
- Add search functionality
- Add tags/categories for notes
- Add book cover images
- Add reading progress tracking
- Add note export (PDF, EPUB)
