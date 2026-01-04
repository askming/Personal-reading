# Margin Notes Feature Implementation Summary

## Overview
Added support for Jupyter Book style margin notes in the custom static site generator. Margin notes are now extracted from markdown files and displayed in the right sidebar of article pages.

## What Changed

### 1. **site_generator.py** - Core Changes

#### Added Imports
- Added `re` module for regex pattern matching

#### New Function: `extract_margin_notes()`
Extracts margin notes from markdown content with the format:
```
```{margin} [Optional Link Title](url)
Content line 1
Content line 2
```
```

**Functionality:**
- Uses regex pattern to find all margin blocks
- Converts markdown links `[text](url)` to HTML links with `<strong>` formatting
- Wraps each line in `<p>` tags for proper HTML formatting
- Removes margin blocks from main content to prevent duplication
- Returns both cleaned content and list of margin notes

#### Modified Function: `markdown_to_html()`
**Before:** 
- Took markdown string, returned HTML string

**After:**
- Calls `extract_margin_notes()` first to clean content
- Returns tuple: `(html_content, margin_notes_list)`
- Margin notes are processed separately from main content

#### Modified Function: `generate_page_html()`
**Changes:**
- Added `margin_notes` parameter with default `None`
- Generates HTML for margin notes
- Inserts margin notes HTML into right sidebar after TOC
- Updated template placeholder to include `{margin}`

#### Modified Function: `main()`
**Changes:**
- Updated to handle tuple return from `markdown_to_html()`
- Unpacks: `content_html, margin_notes = markdown_to_html(md_content)`
- Passes `margin_notes` to `generate_page_html()`

### 2. **book/_site/assets/style.css** - Styling

Added comprehensive CSS styling for margin notes:

```css
.margin-notes {
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid var(--border-color);
}

.margin-note {
    background-color: #f9f9f9;
    padding: 12px;
    margin-bottom: 15px;
    border-left: 3px solid var(--secondary-color);
    border-radius: 3px;
    font-size: 13px;
    line-height: 1.6;
    color: #555;
}
```

**Styling Features:**
- Light gray background (#f9f9f9) for visual distinction
- Left border in secondary color (blue) matching TOC/sidebar theme
- Smaller font size (13px) for sidebar context
- Proper paragraph spacing within notes
- Responsive: Margins adjust on smaller screens
- Links styled with secondary color and hover underline effect

### 3. **HTML Template** - Integration

The article page template now includes margin notes in the right sidebar:

```html
<aside class="sidebar-right">
    <div class="toc-title">Table of Contents</div>
    {toc}
    {margin}
</aside>
```

Margin notes appear after the table of contents in the right sidebar.

## How It Works

1. **Extraction Phase:** When processing a markdown file, `extract_margin_notes()` finds all `{margin}` blocks
2. **Cleaning Phase:** Removes margin blocks from main content to prevent display as code blocks
3. **Conversion Phase:** Converts margin markdown links to HTML
4. **Rendering Phase:** Displays margin notes in right sidebar with proper formatting and styling

## Example Input

```markdown
## "我不确定"：充分利用不确定性
```{margin} [James Clerk Maxwell](https://en.wikipedia.org/wiki/James_Clerk_Maxwell)
James Clerk Maxwell FRSE FRS (13 June 1831 – 5 November 1879) was a Scottish scientist in the field of mathematics and mathematical physics.
```
Clerk Maxwell 的名言来支持这一观点...
```

## Example Output

The margin note appears in the right sidebar as:
- **[James Clerk Maxwell]** (as a link)
- James Clerk Maxwell FRSE FRS (13 June 1831 – 5 November 1879) was a Scottish scientist in the field of mathematics and mathematical physics.

With styling:
- Light gray background box
- Blue left border
- Smaller, refined font
- Professional appearance matching the rest of the site

## Backward Compatibility

Files without margin notes continue to work normally - the feature is entirely optional.

## Testing

The implementation was tested with the actual margin note from [对赌：信息不足时如何做出高明决策.md](book/2019/%E5%AF%B9%E8%B5%8C%EF%BC%9A%E4%BF%A1%E6%81%AF%E4%B8%8D%E8%B6%B3%E6%97%B6%E5%A6%82%E4%BD%95%E5%81%9A%E5%87%BA%E9%AB%98%E6%98%8E%E5%86%B3%E7%AD%96.md) and correctly extracted both the link and content.
