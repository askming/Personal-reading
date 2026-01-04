#!/bin/bash
# Push migration changes to GitHub

echo "📦 Preparing to push changes..."
echo ""
echo "✅ Files being committed:"
echo "  - site_generator.py (new custom site generator)"
echo "  - book/_site/assets/style.css (website styling)"
echo "  - book/_site/assets/script.js (website interactivity)"
echo "  - book/_site/.nojekyll (GitHub Pages config)"
echo "  - .github/workflows/generate_note_from_issue.yml (updated workflow)"
echo "  - requirements.txt (updated dependencies)"
echo "  - .gitignore (project config)"
echo "  - SITE_SETUP.md (setup documentation)"
echo "  - MIGRATION_SUMMARY.md (migration details)"
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not found. Please run this from your repo root."
    exit 1
fi

# Add all changes
echo "Adding files to git..."
git add site_generator.py
git add "book/_site/"
git add ".github/workflows/"
git add "requirements.txt"
git add ".gitignore"
git add "SITE_SETUP.md"
git add "MIGRATION_SUMMARY.md"

echo ""
echo "Committing changes..."
git commit -m "chore: migrate from jupyter-book to custom static site generator

- Add custom Python site generator (site_generator.py)
- Create responsive HTML/CSS/JS website layout
- Update GitHub Actions workflow to use new generator
- Optimize dependencies (remove jupyter-book, add markdown/pygments)
- Add comprehensive documentation (SITE_SETUP.md, MIGRATION_SUMMARY.md)
- Add .gitignore for generated files and venv

Features:
- Top navigation bar (Home, About, GitHub)
- Left sidebar with reading notes by year
- Auto-generated table of contents in right sidebar
- Responsive design for desktop/tablet/mobile
- Smooth scrolling and active section highlighting"

echo ""
echo "✨ Changes committed! Now pushing to remote..."
git push origin master

echo ""
echo "✅ Done! Your changes have been pushed to GitHub."
echo ""
echo "⚙️ Next steps:"
echo "1. Check your GitHub repository settings"
echo "2. Enable GitHub Pages"
echo "3. Set Pages source to 'gh-pages' branch"
echo "4. Your site will be live in a few minutes!"
echo ""
echo "📖 For more information, see SITE_SETUP.md"
