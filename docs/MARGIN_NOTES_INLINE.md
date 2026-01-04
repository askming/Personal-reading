# Margin Notes - Inline Implementation

## Changes Made

Successfully repositioned margin notes from the right sidebar to the main content panel, where they float next to the text they're associated with.

### Modified Files

1. **site_generator.py**
   - Changed `extract_margin_notes()` to convert margin blocks to inline HTML `<div>` elements instead of storing separately
   - Updated `markdown_to_html()` to return single string instead of tuple (no longer needs separate margin notes list)
   - Removed `margin_notes` parameter from `generate_page_html()`
   - Simplified `main()` function to handle new flow

2. **book/_site/assets/style.css**
   - Added `.margin-note-inline` styling for floating margin notes
   - Margin notes float to the right of text with `float: right`
   - Width: 300px on desktop
   - Responsive: Converts to full-width block on tablets/mobile (max-width: 1200px)

## How It Works Now

### Input (Markdown)
```markdown
## Section Heading

```{margin} [James Clerk Maxwell](https://en.wikipedia.org/wiki/James_Clerk_Maxwell)
James Clerk Maxwell FRSE FRS (13 June 1831 – 5 November 1879) was a Scottish scientist in the field of mathematics and mathematical physics.
```

Regular paragraph text continues here...
```

### Output (HTML in Main Content)
```html
<h2 id="section-heading">Section Heading</h2>

<div class="margin-note-inline">
  <p><a href="https://..." target="_blank"><strong>James Clerk Maxwell</strong></a></p>
  <p>James Clerk Maxwell FRSE FRS...</p>
</div>

<p>Regular paragraph text continues here...</p>
```

### Visual Result
The margin note appears as a floating box to the right of the text, connected to where it was placed in the markdown.

## Styling Details

### Desktop (width > 1200px)
```
┌─────────────────────────────────────────┐
│ Content text here...                    │
│ Lorem ipsum dolor sit amet.   ╔════════╗│
│                               ║ Margin ║│
│ More content text...          ║ Note   ║│
│ Consectetur adipiscing.       ║ Here   ║│
│                               ║ Floats ║│
│ Another paragraph...          ║ Right  ║│
│                               ╚════════╝│
└─────────────────────────────────────────┘
```

### Mobile/Tablet (width ≤ 1200px)
```
┌──────────────────────────────┐
│ Content text here...         │
│ Lorem ipsum dolor sit amet.  │
│                              │
│ ╔───────────────────────────╗│
│ ║ Margin Note Here          ║│
│ ║ Floats full width on      ║│
│ ║ smaller screens           ║│
│ ╚───────────────────────────╝│
│                              │
│ More content text...         │
│ Consectetur adipiscing.      │
└──────────────────────────────┘
```

## CSS Properties

```css
.margin-note-inline {
    float: right;           /* Floats to right of content */
    clear: right;           /* Prevents overlap */
    width: 300px;           /* Fixed width on desktop */
    margin: 0 0 20px 20px;  /* Spacing around the note */
    padding: 15px;          /* Internal padding */
    background-color: #f9f9f9;          /* Light gray background */
    border-left: 3px solid #3498db;     /* Blue left border */
    font-size: 13px;        /* Smaller text for sidebar-like appearance */
}
```

## Advantages Over Sidebar Approach

✅ **Contextual**: Margin notes appear next to the text they reference  
✅ **Natural Flow**: Text wraps around the note naturally  
✅ **Connected**: Visual connection between note and content  
✅ **Responsive**: Automatically stacks on mobile devices  
✅ **Traditional**: Follows academic paper margin note convention  

## Testing

Run `python3 site_generator.py` to generate the site with inline margin notes.

Example: Open an article with margin notes (like "对赌：信息不足时如何做出高明决策.md") to see the margin notes floating to the right of the main content.
