# OpenType Variant Analyzer

**A browser-based tool for type designers and font enthusiasts to visualize how glyph variants are distributed in OpenType fonts.**

If you design handwriting fonts, calligraphic typefaces, or any font with contextual alternates — you know the challenge: *are my alternates actually being used evenly, or does the shaping engine keep picking the same variant?* This tool answers that question instantly.

Drop any OTF, TTF, WOFF, or WOFF2 file into the browser. Type some text. See exactly which variant of each letter HarfBuzz selects — rendered with the actual glyph outlines, color-coded by variant, with distribution charts and metrics updating live.

**No install. No build step. Just one HTML file.**

→ **[Try it live](https://toolbox.haraldgeisler.com/?p=131)**
 
→ **[GitHub Pages mirror](https://d-barrow.github.io/opentype-variant-analyzer/opentype-variant-analyzer.html)**

> Built during the development of a Goethe handwriting font with 4+ contextual alternates per letter.

## Who is this for?

- **Type designers** testing distribution of alternates, stylistic sets (ss01–ss20), and randomization features
- **Font engineers** debugging GSUB lookup behavior and variant distribution
- **Calligraphy & handwriting font creators** checking that letter repetition looks natural
- **Typography students** learning how OpenType shaping works under the hood
- **Anyone curious** about what happens inside a font when you type

## Features

- **Drag & drop** any OTF, TTF, WOFF, or WOFF2 font — works entirely in the browser, no upload to any server
- **Real HarfBuzz WASM shaping** — the same engine used in Chrome, Firefox, and professional layout tools, running client-side
- **Actual glyph outlines** — each letter is rendered as an inline SVG using the real variant-specific shape from the font, not re-drawn browser text
- **Color-coded variant preview** — every letter gets a tinted background showing which variant HarfBuzz selected; hover for glyph name details
- **Distribution bar chart** — see at a glance if variants are balanced or skewed
- **Transition heatmap** — which variant tends to follow which? Spot patterns in the GSUB logic
- **Metrics panel** — Versions Found, Spread Score (Shannon entropy), Perfect Score, Range, Repeats, Letters Analyzed
- **Adjustable preview** — font size and line height controls, collapsible preview section
- **Live re-analysis** — type or edit text, results update in real time (300 ms debounce)
- **Preset texts** — Goethe (German), Lorem Ipsum, Pangrams (EN/DE), Alphabet Repeat
- **Beginner-friendly labels** — no jargon; tooltips explain every metric

## How It Works

1. Open `opentype-variant-analyzer.html` in any modern browser (Chrome, Firefox, Safari, Edge).
2. Drop a font file onto the drop zone (or click to browse).
3. HarfBuzz WASM loads and shapes your text through the font's full GSUB pipeline — contextual alternates, ligatures, positional forms, and all.
4. Each resulting glyph ID is matched to its glyph name via opentype.js (e.g., `a.001`, `e.init.003`, `A.swash`).
5. The variant suffix is parsed and color-coded in the preview.
6. Distribution charts and quality metrics update live as you type.

## Supported Variant Naming Conventions

| Pattern | Example | Parsed As |
|---------|---------|-----------|
| Numeric suffix | `a.001`, `a.003` | Variant 1, 3 |
| Stylistic set | `a.ss01`, `a.ss02` | Variant ss01, ss02 |
| Alt suffix | `a.alt`, `a.alt2` | Variant alt, alt2 |
| Swash | `A.swash` | Variant swash |
| Contextual + numeric | `a.init.002` | Variant 2 (base: a.init) |
| Plain name | `a` | Base |

## CDN Dependencies

All dependencies load from jsDelivr CDN — no build step required:

- [Chart.js 4.5.1](https://www.chartjs.org/) — bar charts
- [chartjs-chart-matrix 3.0.0](https://github.com/kurkle/chartjs-chart-matrix) — heatmap
- [opentype.js 1.3.4](https://opentype.js.org/) — OTF/TTF parsing & glyph name resolution
- [harfbuzzjs 0.10.1](https://github.com/nicolo-ribaudo/harfbuzzjs) — HarfBuzz WASM text shaping

## WordPress Embedding

The analyzer can be embedded in a WordPress page using **Custom HTML blocks**. Because WordPress applies `wptexturize` and other content filters that can mangle inline JavaScript (e.g. `&&` becomes `&#038;&#038;`), and because `data:` URI iframes have a `null` origin that blocks file I/O in Safari, we use a **blob: URL iframe** approach.

### How it works

`gen-wp-embed.py` base64-encodes the entire `opentype-variant-analyzer.html` and wraps it in a tiny bootstrap script. When the page loads, the script:

1. Decodes the base64 payload via `atob()`
2. Converts the binary string to a `Uint8Array` (to avoid UTF-8 double-encoding)
3. Creates a `Blob` with the HTML content
4. Opens the blob as an iframe via `URL.createObjectURL()`

The iframe inherits the parent page's real origin, so all browser APIs (FileReader, Font loading, etc.) work normally.

### Steps to embed

```bash
cd font-analyzer
python3 gen-wp-embed.py
```

This generates `wordpress-embed.html` (~62 KB). Then:

1. Open your WordPress page in the editor.
2. Add a **Custom HTML** block.
3. Paste the entire contents of `wordpress-embed.html` into the block.
4. Publish or preview the page.

### Technical notes

- The bootstrap script avoids `&&` operators to prevent `wptexturize` mangling.
- The `Uint8Array` conversion is essential: `atob()` returns a binary string where each character is one byte, but `new Blob([string])` would re-encode it as UTF-8, corrupting any multi-byte characters (e.g. `·` → `Â·`).
- The blob: URL iframe inherits the parent page's origin (e.g. `https://yoursite.com`), unlike `data:` URI iframes which get `null` origin and block all blob/FileReader operations in Safari.

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](LICENSE).

You are free to use, share, and adapt this tool for **non-commercial purposes** with attribution. Commercial use requires separate permission — please get in touch.

## Version

v1.0.0 · 2026-03-23

---

**Keywords:** OpenType, font testing, glyph variants, contextual alternates, calt, stylistic sets, HarfBuzz, WASM, type design, typography, font analysis, handwriting font, calligraphy, GSUB, variant distribution, font tools
