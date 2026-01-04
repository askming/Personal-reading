# Static Site Architecture

## Website Layout

```
┌─────────────────────────────────────────────────────────────────┐
│                        NAVIGATION BAR                            │
│                [Home] [About] [GitHub]                           │
└─────────────────────────────────────────────────────────────────┘

┌────────────────┬─────────────────────────────┬──────────────────┐
│                │                             │                  │
│  LEFT SIDEBAR  │     MAIN CONTENT            │  RIGHT SIDEBAR   │
│                │                             │                  │
│ Years          │  ╔════════════════════════╗ │  TABLE OF        │
│                │  ║ Book Title              ║ │  CONTENTS        │
│ 📅 2026        │  ║                        ║ │                  │
│   📖 Book 1    │  ║ Full markdown content  ║ │  # Heading 1    │
│   📖 Book 2    │  ║                        ║ │    • Heading 2   │
│                │  ║ - Lists                ║ │    • Heading 3   │
│ 📅 2025        │  ║ - Support              ║ │                  │
│   📖 Book 3    │  ║ - Code blocks          ║ │  # Heading 2    │
│   📖 Book 4    │  ║ - Quotes               ║ │    • Sub-point   │
│                │  ║ - Tables               ║ │                  │
│ 📅 2024        │  ║                        ║ │                  │
│   📖 Book 5    │  ╚════════════════════════╝ │                  │
│   ...          │                             │                  │
│                │                             │                  │
└────────────────┴─────────────────────────────┴──────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                          FOOTER                                  │
│                    Generated on YYYY-MM-DD                       │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow

```
GitHub Repository
│
├── book/
│   ├── 2025/
│   │   ├── Book Title.md
│   │   └── Another Book.md
│   ├── 2024/
│   │   └── ...
│   └── _site/ (generated)
│
└── GitHub Actions Trigger
   (push, issue, issue_comment)
        │
        ├── main.py (process issues)
        │   └── Generate markdown from GitHub issues
        │
        ├── site_generator.py (build site)
        │   ├── Read all markdown files
        │   ├── Extract headings for TOC
        │   ├── Convert markdown to HTML
        │   ├── Generate pages with templates
        │   └── Create assets (CSS, JS)
        │
        └── Deploy to gh-pages branch
            └── GitHub Pages serves site
```

## Generated Site Structure

```
book/_site/
├── index.html (Home page)
├── about.html (About page)
├── assets/
│   ├── style.css (Styling)
│   └── script.js (Interactivity)
├── 2025/
│   ├── Book Title.html
│   └── Another Book.html
├── 2024/
│   ├── ...
│   └── ...
└── .nojekyll (GitHub Pages config)
```

## Technology Stack

```
Frontend:
├── HTML (Structure)
├── CSS (Styling)
└── JavaScript (Interactivity)

Backend:
├── Python 3.9 (Site generator)
├── markdown (Markdown processing)
├── pygments (Code highlighting)
└── PyGithub (Issue processing)

Deployment:
├── GitHub Actions (CI/CD)
└── GitHub Pages (Hosting)
```

## Page Generation Process

For each reading note:

```
Input: book/2025/Book Title.md

Step 1: Read markdown
└── Extract title, content, headings

Step 2: Convert markdown to HTML
├── Parse markdown syntax
├── Apply syntax highlighting to code
└── Generate HTML elements

Step 3: Extract headings for TOC
├── Find all heading levels
├── Create anchor IDs
└── Generate nested list structure

Step 4: Build complete page HTML
├── Include navigation bar
├── Include left sidebar (with active item highlighted)
├── Include main content with converted HTML
├── Include right sidebar with TOC
└── Include footer

Step 5: Write to output
└── Save as book/_site/2025/Book%20Title.html

Output: book/_site/2025/Book Title.html
```

## Interaction Points

```
User clicks link in sidebar
    ↓
Load new page (e.g., /2025/Book Title.html)
    ↓
JavaScript executes:
    ├── Highlight active sidebar item
    └── Setup TOC interactions

User scrolls through content
    ↓
JavaScript monitors scroll position
    ↓
Highlights active heading in TOC

User clicks TOC link
    ↓
Smooth scroll to heading
    ↓
Update active TOC link
```

## Build Performance

Timeline (GitHub Actions):
- Checkout: ~5 seconds
- Setup Python: ~3 seconds
- Install dependencies: ~10 seconds
- Run main.py: ~2 seconds (only if triggered by issue)
- Generate site: ~1-5 seconds (depends on number of books)
- Deploy: ~3 seconds
- **Total**: ~15-30 seconds

## Browser Compatibility

- ✅ Chrome/Edge 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## Responsive Breakpoints

```
Desktop (>1200px):
├── Full three-column layout
├── Sidebar left: 250px
├── Main content: flexible
└── Sidebar right: 250px

Tablet (768px - 1200px):
├── Two-column layout
├── Sidebar left: 250px
├── Main content + TOC combined
└── No right sidebar

Mobile (<768px):
├── Single column
├── Expandable sidebar
├── No right sidebar
└── Stacked footer
```

## Data Volume

Per book (~2000 words):
- Markdown: ~10 KB
- Generated HTML: ~12 KB
- Page size (with CSS/JS): ~40 KB

Total site (~200 books):
- Markdown: ~2 MB
- Generated HTML: ~2.4 MB
- With assets: ~2.5 MB
- **Total site size**: ~2.5 MB (very lean!)
