# Margin Notes - Visual Layout Guide

## Article Page Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│                          MY's Readings                              │
└─────────────────────────────────────────────────────────────────────┘

┌──────────────┬─────────────────────────────────┬──────────────────────┐
│              │                                 │                      │
│   SIDEBAR    │      MAIN CONTENT               │    RIGHT SIDEBAR     │
│   (Years)    │   Article Title                 │  Table of Contents   │
│              │   ================              │  ==================  │
│  • 2025      │                                 │  • Introduction      │
│  • 2024      │  Article content here...        │  • Section A         │
│  • 2023      │  Lorem ipsum dolor sit          │  • Section B         │
│              │  amet, consectetur adipiscing   │                      │
│  • 2022      │  elit.                          │  ╔════════════════╗  │
│              │                                 │  ║ MARGIN NOTES   ║  │
│              │  [James Clerk Maxwell]          │  ╠════════════════╣  │
│              │  reference here                 │  ║ James Clerk    ║  │
│              │                                 │  ║ Maxwell        ║  │
│              │                                 │  ║ ────────────   ║  │
│              │  More article text...           │  ║ James Clerk    ║  │
│              │                                 │  ║ Maxwell FRSE   ║  │
│              │                                 │  ║ FRS (13 June   ║  │
│              │                                 │  ║ 1831 – 5 Nov   ║  │
│              │                                 │  ║ 1879) was a    ║  │
│              │                                 │  ║ Scottish       ║  │
│              │                                 │  ║ scientist...   ║  │
│              │                                 │  ╚════════════════╝  │
│              │                                 │                      │
└──────────────┴─────────────────────────────────┴──────────────────────┘
```

## Margin Note Styling

```
┌─────────────────────────────────────────┐
│ ╔═════════════════════════════════════╗ │
│ ║                                     ║ │ ← Light gray background (#f9f9f9)
│ ║ [James Clerk Maxwell]               ║ │ ← Link in <strong> tag
│ ║                                     ║ │
│ ║ James Clerk Maxwell FRSE FRS        ║ │ ← Regular text (13px font)
│ ║ (13 June 1831 – 5 November 1879)    ║ │
│ ║ was a Scottish scientist in the     ║ │
│ ║ field of mathematics and            ║ │
│ ║ mathematical physics.               ║ │
│ ║                                     ║ │
│ ╚═════════════════════════════════════╝ │ ← Blue left border (3px)
│                                         │
│ (additional margin notes follow)        │
└─────────────────────────────────────────┘
```

## Markdown Input Format

```markdown
## "我不确定"：充分利用不确定性

```{margin} [James Clerk Maxwell](https://en.wikipedia.org/wiki/James_Clerk_Maxwell)
James Clerk Maxwell FRSE FRS (13 June 1831 – 5 November 1879) was a Scottish scientist in the field of mathematics and mathematical physics.
```

Clerk Maxwell 的名言来支持这一观点："完全自知的无知是每一次科学进步的序幕。"
```

## CSS Classes

```css
.margin-notes          /* Container for all margin notes */
  ↓
.margin-note           /* Individual margin note box */
  ├─ Background: #f9f9f9 (light gray)
  ├─ Border-left: 3px solid #3498db (blue)
  ├─ Font-size: 13px (smaller for sidebar)
  ├─ Line-height: 1.6 (readable spacing)
  └─ Color: #555 (dark gray text)
  
.margin-note p         /* Paragraphs within notes */
  └─ Proper spacing (8px margin bottom)

.margin-note a         /* Links within notes */
  ├─ Color: #3498db (blue)
  └─ Hover: underline text-decoration
```

## Features

✅ **Markdown Link Support**
   - `[Text](url)` automatically converted to HTML links
   - Links open in new tab (target="_blank")
   - Title rendered in bold (`<strong>`)

✅ **Multi-line Content**
   - Each line becomes a separate paragraph
   - Proper spacing between paragraphs
   - Handles empty lines gracefully

✅ **Visual Design**
   - Consistent with site theme (uses CSS variables)
   - Light gray background for distinction
   - Blue left border matching TOC styling
   - Professional, minimalist appearance

✅ **Responsive**
   - Adjusts margin spacing on smaller screens
   - Maintains readability on mobile
   - Properly flows with sidebar layout

## Integration Example

When the page renders, this markdown:

```
```{margin} [Author Name](https://example.com)
Author description and biography.
```
```

Becomes this HTML in the right sidebar:

```html
<div class="margin-notes">
  <div class="margin-note">
    <p><a href="https://example.com" target="_blank"><strong>Author Name</strong></a></p>
    <p>Author description and biography.</p>
  </div>
</div>
```

With CSS styling automatically applied to display it beautifully in the sidebar.
