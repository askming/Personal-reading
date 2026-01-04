# LXGW WenKai Font Integration

## What Changed

The site now uses **LXGW WenKai (霞鹜文楷)**, an elegant open-source Chinese font, instead of the system default fonts.

### File Modified
- `book/_site/assets/style.css`

### Implementation Details

1. **Font Import**
   ```css
   @import url('https://cdn.jsdelivr.net/npm/lxgw-wenkai@1.7.2/style.css');
   ```
   - Uses jsDelivr CDN for fast, reliable font delivery
   - Automatically handles multiple font weights and variants

2. **Font Stack**
   ```css
   font-family: 'LXGW WenKai', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
   ```
   - Primary: LXGW WenKai (beautiful Chinese/CJK characters)
   - Fallback: System fonts for compatibility and English text

## About LXGW WenKai

- **Name**: LXGW WenKai (霞鹜文楷)
- **Style**: Elegant, modern Chinese font with a hint of calligraphy
- **License**: Open Font License (OFL) - Free for personal and commercial use
- **Based on**: Fontworks' Klee One
- **Repository**: https://github.com/lxgw/LxgwWenKai
- **Supports**: Chinese (Simplified & Traditional), Japanese, Korean

## Why This Font?

✅ **Beautiful**: Combines elegance with readability  
✅ **Free**: OFL open-source license, commercial use allowed  
✅ **Fast**: Delivered via CDN with optimized loading  
✅ **Complete**: Full CJK support for all languages on the site  
✅ **Professional**: Widely used in modern Chinese web design  

## Font Characteristics

- **Style**: Modern sans-serif with subtle serif elements (混搭风格)
- **Weight**: Regular (main) with additional weights available
- **Spacing**: Well-optimized for screen reading
- **Language Support**: Simplified Chinese, Traditional Chinese, Japanese, Korean

## Technical Details

- CDN: jsDelivr (https://cdn.jsdelivr.net/)
- Version: 1.7.2 (latest stable)
- Format: WOFF2 (optimized for web, fast loading)
- Fallback fonts: macOS, Windows, Linux system fonts

## Testing

The font will automatically load from the CDN when users visit the site. The entire site text (navigation, articles, sidebars, margin notes) will display in LXGW WenKai.

Run `python3 site_generator.py` to regenerate the site with the new font.
