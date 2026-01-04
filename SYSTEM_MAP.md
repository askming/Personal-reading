# 🗺️ Complete System Map

## Repository Structure

```
Personal-reading/
│
├── 📁 book/ (Your Reading Notes)
│   ├── 📁 2026/
│   │   ├── book1.md
│   │   └── book2.md
│   ├── 📁 2025/
│   ├── 📁 2024/
│   ├── ... (other years)
│   └── 📁 _site/ (GENERATED - Don't edit!)
│       ├── assets/
│       │   ├── style.css
│       │   └── script.js
│       ├── 2025/
│       │   ├── book1.html (generated)
│       │   └── book2.html (generated)
│       ├── index.html (generated)
│       ├── about.html (generated)
│       └── .nojekyll
│
├── 📁 .github/workflows/
│   └── generate_note_from_issue.yml (CI/CD Pipeline)
│
├── 🐍 site_generator.py (New Main Generator)
│
├── 🐍 main.py (GitHub Issue Processor)
│
├── 📄 requirements.txt (Python Dependencies)
│   ├── PyGithub
│   ├── markdown
│   └── pygments
│
├── 📝 .gitignore (Git Configuration)
│
├── 📚 Documentation/
│   ├── 00_START_HERE.md (← You are here!)
│   ├── QUICKSTART.md
│   ├── SITE_SETUP.md
│   ├── MIGRATION_SUMMARY.md
│   ├── ARCHITECTURE.md
│   ├── DEPLOYMENT_CHECKLIST.md
│   ├── PROJECT_STATUS.md
│   └── README_MIGRATION.md
│
└── 🔧 push_changes.sh (Helper Script)
```

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    YOUR ACTIONS                             │
│  (Push to master, Create issues, Edit notes)                │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              GITHUB REPOSITORY                              │
│  ├── master branch (your code & markdown)                   │
│  └── gh-pages branch (generated site - deployed)            │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│           GITHUB ACTIONS WORKFLOW                           │
│                                                             │
│  1. Trigger Event:                                          │
│     - Push to master                                        │
│     - Issue created/edited                                  │
│     - Manual dispatch                                       │
│                                                             │
│  2. Setup (10 seconds):                                     │
│     - Checkout code                                         │
│     - Setup Python 3.9                                      │
│     - Install dependencies                                  │
│                                                             │
│  3. Process (5 seconds):                                    │
│     - main.py (optional - if issue triggered)              │
│       └─ Convert issue to markdown                          │
│                                                             │
│  4. Build (5 seconds):                                      │
│     - site_generator.py                                     │
│       └─ Read all markdown files                            │
│       └─ Extract headings & metadata                        │
│       └─ Convert markdown to HTML                           │
│       └─ Generate page templates                            │
│       └─ Create navigation structures                       │
│       └─ Copy CSS & JavaScript                              │
│       └─ Output to book/_site/                              │
│                                                             │
│  5. Deploy (3 seconds):                                     │
│     - Push to gh-pages branch                               │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│            GITHUB PAGES                                     │
│  (Automatic Hosting & Deployment)                           │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│         YOUR WEBSITE                                        │
│  (Live at github.io URL)                                    │
│                                                             │
│  ┌──────────────────────────────────────────────────┐      │
│  │  Navigation Bar: Home | About | GitHub           │      │
│  ├──────────┬──────────────┬───────────────────────┤      │
│  │ Sidebar  │ Main Content │ Table of Contents     │      │
│  │ Years    │ • Markdown   │ • Auto-generated TOC  │      │
│  │ & Books  │ • Code       │ • Clickable links     │      │
│  │ Tree     │ • Lists      │ • Active highlighting │      │
│  │          │ • Tables     │                       │      │
│  ├──────────┴──────────────┴───────────────────────┤      │
│  │ Footer: Generated on YYYY-MM-DD                │      │
│  └──────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│         USERS VISIT YOUR SITE                              │
│  (Desktop, tablet, mobile - all supported)                 │
└─────────────────────────────────────────────────────────────┘
```

## Site Generator Logic

```
site_generator.py
│
├─ get_markdown_files()
│  └─ Scan book/YYYY/ directories
│     └─ Return: {2025: [file1.md, file2.md], ...}
│
├─ For each year and file:
│  │
│  ├─ Read markdown file
│  │  └─ Get content as string
│  │
│  ├─ extract_headings()
│  │  └─ Parse heading levels and text
│  │     └─ Generate anchor IDs for TOC links
│  │
│  ├─ markdown_to_html()
│  │  ├─ Convert markdown syntax to HTML
│  │  ├─ Apply syntax highlighting to code
│  │  └─ Add heading IDs for TOC anchors
│  │
│  ├─ generate_toc_html()
│  │  ├─ Build nested list from headings
│  │  └─ Create clickable TOC navigation
│  │
│  ├─ generate_sidebar_html()
│  │  ├─ Build year/book tree in sidebar
│  │  └─ Highlight currently selected book
│  │
│  ├─ generate_page_html()
│  │  ├─ Insert navigation bar (top)
│  │  ├─ Insert sidebar (left)
│  │  ├─ Insert main content (center)
│  │  ├─ Insert TOC (right)
│  │  ├─ Insert footer (bottom)
│  │  └─ Include CSS and JavaScript
│  │
│  └─ Write to book/_site/YYYY/filename.html
│
├─ generate_index_page()
│  └─ Create home page with statistics
│
├─ generate_about_page()
│  └─ Create about page
│
└─ Output: book/_site/ (full website ready to deploy)
```

## Interaction Flow (User's Perspective)

```
USER VISITS SITE
│
├─ Home Page Loads
│  ├─ CSS loads (styling applied)
│  ├─ JavaScript loads (interactivity enabled)
│  └─ Statistics display (count of books by year)
│
├─ User clicks a year in sidebar
│  ├─ Sidebar item highlights
│  └─ List of books appears
│
├─ User clicks a book
│  ├─ Page navigates to book
│  ├─ Main content loads (markdown rendered as HTML)
│  ├─ TOC appears in right sidebar
│  └─ JavaScript detects scroll position
│
├─ User scrolls through content
│  ├─ JavaScript monitors scroll
│  ├─ TOC highlights active heading
│  └─ Reading position is tracked
│
├─ User clicks TOC link
│  ├─ Page smoothly scrolls to heading
│  ├─ Heading is highlighted
│  └─ TOC link highlights as active
│
├─ User resizes window
│  ├─ CSS media queries trigger
│  ├─ Layout adapts (desktop → tablet → mobile)
│  └─ Navigation adjusts
│
└─ User visits another page
   └─ (Repeat above)
```

## File Dependencies

```
Site Generator
│
└─ site_generator.py (main script)
   │
   ├─ Requirements:
   │  ├─ markdown library (Python package)
   │  ├─ pygments library (Python package)
   │  ├─ os module (built-in)
   │  ├─ json module (built-in)
   │  ├─ datetime module (built-in)
   │  └─ pathlib module (built-in)
   │
   ├─ Input:
   │  ├─ book/YYYY/*.md (your markdown files)
   │  └─ _toc.yml (optional, not used currently)
   │
   └─ Output:
      ├─ book/_site/index.html (home)
      ├─ book/_site/about.html (about)
      ├─ book/_site/YYYY/*.html (generated pages)
      ├─ book/_site/assets/style.css (styling)
      └─ book/_site/assets/script.js (interactivity)
```

## Deployment Pipeline

```
┌─ TRIGGER ─────────────────────────────────────────┐
│                                                   │
│  • Push to master                                 │
│  • Issue created/edited                           │
│  • Workflow dispatch (manual)                     │
│                                                   │
└─────────────────────┬─────────────────────────────┘
                      │
                      ▼
┌─ CHECKOUT ────────────────────────────────────────┐
│                                                   │
│  Uses: actions/checkout@v4                        │
│  Gets: Latest code from repository                │
│                                                   │
└─────────────────────┬─────────────────────────────┘
                      │
                      ▼
┌─ SETUP PYTHON ────────────────────────────────────┐
│                                                   │
│  Uses: actions/setup-python@v4                    │
│  Version: 3.9                                     │
│  Cache: pip (optimized!)                          │
│                                                   │
└─────────────────────┬─────────────────────────────┘
                      │
                      ▼
┌─ INSTALL ─────────────────────────────────────────┐
│                                                   │
│  Runs: pip install -r requirements.txt            │
│  Installs: markdown, pygments, PyGithub          │
│                                                   │
└─────────────────────┬─────────────────────────────┘
                      │
                      ▼
┌─ PROCESS ISSUES (optional) ────────────────────────┐
│                                                   │
│  Runs: python main.py ...                         │
│  Only if: Triggered by issue/issue_comment       │
│  Does: Convert issue to markdown file             │
│                                                   │
└─────────────────────┬─────────────────────────────┘
                      │
                      ▼
┌─ COMMIT & PUSH (optional) ─────────────────────────┐
│                                                   │
│  Uses: github-actions-x/commit@v2.9              │
│  Only if: Files were created/modified            │
│  Does: Commit and push to master                 │
│                                                   │
└─────────────────────┬─────────────────────────────┘
                      │
                      ▼
┌─ BUILD SITE ───────────────────────────────────────┐
│                                                   │
│  Runs: python site_generator.py                   │
│  Generates: All HTML files in book/_site/        │
│  Time: ~5 seconds                                 │
│                                                   │
└─────────────────────┬─────────────────────────────┘
                      │
                      ▼
┌─ DEPLOY ───────────────────────────────────────────┐
│                                                   │
│  Uses: peaceiris/actions-gh-pages@v3.6.1         │
│  Publishes: book/_site/ to gh-pages branch       │
│  Deploys: GitHub Pages serves the site           │
│                                                   │
└─────────────────────┬─────────────────────────────┘
                      │
                      ▼
┌─ RESULT ───────────────────────────────────────────┐
│                                                   │
│  ✅ Site live at: https://github.io/Personal-r...│
│  ✅ Ready for users to visit                      │
│  ✅ All content updated automatically             │
│                                                   │
└─────────────────────────────────────────────────────┘
```

## Git Workflow

```
                    master branch
                    (your code)
                          │
                          │ Push triggered
                          │
                    GitHub Actions
                          │
                          │ Generates
                          │
                    book/_site/
                          │
                          │ Deployed to
                          │
                    gh-pages branch
                    (hosting)
                          │
                          │ Served by
                          │
                    GitHub Pages
                          │
                          │
                   Your Website 🌐
```

## Content Organization

```
Your Markdown Files (Input)
│
├─ 2026/
│  ├─ Book1.md (800 words)
│  ├─ Book2.md (1200 words)
│  └─ ...
│
├─ 2025/
│  ├─ Book3.md (900 words)
│  ├─ Book4.md (1100 words)
│  └─ ...
│
└─ (other years)

                    ↓ site_generator.py ↓

Generated Website (Output)
│
├─ index.html (home page)
├─ about.html (about page)
├─ assets/ (CSS & JS)
│
├─ 2026/
│  ├─ Book1.html (12 KB)
│  ├─ Book2.html (14 KB)
│  └─ ...
│
├─ 2025/
│  ├─ Book3.html (11 KB)
│  ├─ Book4.html (13 KB)
│  └─ ...
│
└─ (other year pages)

Total Size: ~2.5 MB (very lean!)
```

---

## 🎯 Key Points

1. **Simple Flow**: Markdown → Generator → HTML → GitHub Pages → Website
2. **Automatic**: Everything runs on GitHub Actions
3. **Fast**: ~5 seconds to build entire site
4. **Lean**: Only ~2.5 MB total
5. **Scalable**: Can handle hundreds of notes
6. **Responsive**: Works on all devices
7. **Customizable**: Full control over HTML/CSS/JS

---

**This is your complete system! Everything works together seamlessly. 🚀**
