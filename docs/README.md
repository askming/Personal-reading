# Documentation Index

This folder contains all instructional and feature documentation for the Personal-reading site generator project.

## Quick Navigation

### Core Features

1. **[Margin Notes](MARGIN_NOTES_IMPLEMENTATION.md)** - Complete implementation guide
   - How margin notes work
   - Markdown syntax
   - Styling and positioning
   
   Related: [Layout Guide](MARGIN_NOTES_LAYOUT.md) | [Inline Implementation](MARGIN_NOTES_INLINE.md)

2. **[Footnotes](FOOTNOTES_FEATURE.md)** - Numbered footnotes with bidirectional links
   - Markdown syntax for footnotes
   - HTML output and styling
   - Combining with other features
   
   Quick Ref: [Quick Reference Guide](FOOTNOTES_QUICK_REFERENCE.md)

3. **[LXGW WenKai Font](LXGW_WENKAI_FONT.md)** - Beautiful Chinese font integration
   - Font setup and configuration
   - CDN delivery
   - Why this font was chosen

## Feature Documentation Files

| File | Description |
|------|-------------|
| MARGIN_NOTES_IMPLEMENTATION.md | Complete margin notes feature guide |
| MARGIN_NOTES_CHANGES.md | Summary of changes made |
| MARGIN_NOTES_LAYOUT.md | Visual layout guide with examples |
| MARGIN_NOTES_INLINE.md | Details on inline positioning |
| FOOTNOTES_FEATURE.md | Comprehensive footnotes documentation |
| FOOTNOTES_QUICK_REFERENCE.md | Quick syntax and usage guide |
| LXGW_WENKAI_FONT.md | Font integration details |

## Common Tasks

### Adding Margin Notes
See: [Margin Notes Implementation](MARGIN_NOTES_IMPLEMENTATION.md)
```markdown
```{margin} [Reference Title](url)
Margin note content
```
```

### Adding Footnotes
See: [Footnotes Quick Reference](FOOTNOTES_QUICK_REFERENCE.md)
```markdown
Text with footnote[^1]

[^1]: Footnote content here
```

### Changing the Font
See: [LXGW WenKai Font](LXGW_WENKAI_FONT.md)
Current font: LXGW WenKai (loaded via jsDelivr CDN)

## Project Structure

```
Personal-reading/
├── site_generator.py          # Main site generation script
├── main.py                    # GitHub issue processor
├── requirements.txt           # Python dependencies
├── book/                      # Markdown content
│   └── 2019-2025/            # Articles by year
├── book/_site/               # Generated static site
│   └── assets/
│       ├── style.css         # All styling (margin notes, footnotes, etc.)
│       └── script.js         # JavaScript interactivity
├── docs/                     # This folder - documentation
└── .github/workflows/        # GitHub Actions CI/CD
```

## Key Technologies

- **Python 3.9**: Site generator and markdown processing
- **Markdown Library**: Converts markdown with extensions
  - `tables`: Table support
  - `fenced_code`: Code blocks
  - `codehilite`: Syntax highlighting
  - `footnotes`: Footnote processing
- **LXGW WenKai**: Chinese font via jsDelivr CDN
- **Chart.js 3.9.1**: Statistics visualization
- **GitHub Actions**: Automated deployment

## Configuration

All key configuration is in:
- `site_generator.py`: `BASE_PATH`, `BOOK_DIR`, `OUTPUT_DIR`
- `book/_site/assets/style.css`: All visual styling
- `book/_site/assets/script.js`: Interactive features

## Getting Started

1. **Review the core features** - Start with [Margin Notes](MARGIN_NOTES_IMPLEMENTATION.md) and [Footnotes](FOOTNOTES_FEATURE.md)
2. **Check the syntax** - Use [Footnotes Quick Reference](FOOTNOTES_QUICK_REFERENCE.md) for quick syntax lookup
3. **Understand the styling** - See [Margin Notes Layout](MARGIN_NOTES_LAYOUT.md) for visual examples
4. **Build the site** - Run `python3 site_generator.py`
5. **Deploy** - Use `push_changes.sh` or GitHub Actions

## File Organization

- **Documentation** (this folder): All instructional and feature guides
- **Source Code** (root): Python scripts for generation
- **Content** (book/): Markdown article files
- **Generated Site** (book/_site/): HTML output
- **GitHub** (.github/): CI/CD configuration

This structure keeps the repository clean and organized with all documentation centralized.
