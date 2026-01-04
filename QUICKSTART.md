# Quick Start Guide - Static Site Generator

## What Changed?
✅ Replaced Jupyter Book with a custom static site generator  
✅ Optimized workflow and dependencies  
✅ Added responsive, modern website layout  

## Deploy Your Changes

### Option 1: Using the Script (Recommended)
```bash
chmod +x push_changes.sh
./push_changes.sh
```

### Option 2: Manual Git Commands
```bash
# Review changes
git status

# Add all files
git add .

# Commit
git commit -m "Migrate to static site generator"

# Push to master
git push origin master
```

## After Pushing

1. **Enable GitHub Pages** (if not already done)
   - Go to Settings → Pages
   - Set source to `gh-pages` branch
   - Save

2. **Wait for deployment**
   - GitHub Actions will automatically:
     - Generate the static site
     - Deploy to `gh-pages` branch
   - This takes ~1-2 minutes

3. **Visit your site**
   - Your site will be available at the URL shown in GitHub Pages settings
   - Usually: `https://username.github.io/Personal-reading/`

## Test Locally (Optional)

```bash
# Install dependencies
pip install -r requirements.txt

# Generate site
python site_generator.py

# Serve locally
cd book/_site
python -m http.server 8000

# Open http://localhost:8000 in browser
```

## Make Changes

To update your site:

1. **Add a new reading note**
   - Create `book/YYYY/Book Title.md`
   - Push to master

2. **Edit an existing note**
   - Modify `book/YYYY/Book Title.md`
   - Push to master

3. **GitHub Actions will automatically**
   - Regenerate your site
   - Deploy the changes

## Customization

### Change Colors
Edit `book/_site/assets/style.css`:
```css
:root {
    --primary-color: #2c3e50;  /* Change this */
    --secondary-color: #3498db; /* And this */
}
```

### Change Layout
Edit `site_generator.py` - look for `template` variable in functions like `generate_page_html()`

### Change Home Page Content
Edit `generate_index_page()` function in `site_generator.py`

## Troubleshooting

**Site not building?**
- Check GitHub Actions log
- Verify `main.py` has correct indentation
- Check `requirements.txt` for syntax errors

**Site looks broken after push?**
- Give GitHub Pages 2-3 minutes to rebuild
- Hard refresh in browser (Ctrl+Shift+R or Cmd+Shift+R)
- Check browser console for JavaScript errors

**Can't see recent changes?**
- Make sure files are in `book/YYYY/` (not elsewhere)
- Verify filenames are in `.md` format
- Check that year directory exists

## Files to Know

| File | Purpose |
|------|---------|
| `site_generator.py` | Main site generator script |
| `book/_site/assets/style.css` | Website styling |
| `book/_site/assets/script.js` | Website interactivity |
| `.github/workflows/generate_note_from_issue.yml` | GitHub Actions workflow |
| `main.py` | GitHub issue processor |
| `requirements.txt` | Python dependencies |
| `SITE_SETUP.md` | Detailed setup guide |
| `MIGRATION_SUMMARY.md` | What changed |

## Need Help?

- **SITE_SETUP.md** - Complete setup documentation
- **MIGRATION_SUMMARY.md** - Details of all changes
- **site_generator.py** - Well-commented source code

---

**You're all set! 🚀 Push your changes and your new site will be live!**
