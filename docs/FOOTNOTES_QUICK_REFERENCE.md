# Footnotes - Quick Reference Guide

## Basic Usage

### Write
```markdown
This is text with a footnote[^1].

[^1]: The footnote content appears here.
```

### See
Text: "This is text with a footnote¹."

At bottom:
```
Footnotes

1. The footnote content appears here. ↩
```

## Multiple Footnotes

```markdown
First mention[^1], second mention[^2], third mention[^3].

[^1]: First note
[^2]: Second note  
[^3]: Third note
```

Renders as:
- "First mention¹, second mention², third mention³."
- Footnotes section with all three numbered entries

## Multi-line Footnotes

```markdown
Complex concept[^complex].

[^complex]: This footnote has multiple lines.
    You can indent continuation lines 
    and they will be grouped together as one footnote.
```

## Footnotes with Formatting

```markdown
See the reference[^ref].

[^ref]: See _Advanced Topics_ by **Smith** (2020).
    Available at https://example.com
```

Footnote renders as: "See _Advanced Topics_ by **Smith** (2020). Available at..."

## Interaction Features

| Action | Result |
|--------|--------|
| Click footnote number (¹) | Jumps to footnote at bottom |
| Click ↩ in footnote | Jumps back to text |
| Press Tab | Navigate through all footnote links |
| Mobile tap | Works same as desktop |

## Styling

**In-text reference:**
- Superscript number (smaller, raised)
- Blue color, dotted underline
- Hover effect (opacity change)

**Footnotes section:**
- Separated from content by horizontal line
- Smaller font (13px)
- Numbered list format
- Each footnote has back-reference arrow (↩)

## Common Patterns

### Citation
```markdown
According to research[^study].

[^study]: Smith, J. (2023). "Topic". Journal Name, Vol. 1.
```

### Definition
```markdown
The algorithm[^algo] works as follows...

[^algo]: An algorithm is a step-by-step procedure for solving a problem.
```

### External Reference
```markdown
See the documentation[^docs].

[^docs]: https://example.com/documentation
```

### Note/Warning
```markdown
This feature is experimental[^note].

[^note]: **Note:** This is still in beta testing.
```

## Tips

✅ Number footnotes in order of first appearance  
✅ Keep footnote text concise (use external links for details)  
✅ Footnotes auto-number - don't manually type numbers  
✅ Can use different reference markers: `[^1]`, `[^note]`, `[^ref]`  
✅ Footnotes work in all markdown files  
✅ Combine with margin notes and code blocks freely  

## Browser Support

Works on:
- ✅ Desktop (Chrome, Firefox, Safari, Edge)
- ✅ Tablet (iOS Safari, Android Chrome)
- ✅ Mobile (all modern browsers)
- ✅ Keyboard navigation accessible
- ✅ Screen readers compatible
