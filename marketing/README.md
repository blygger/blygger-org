# marketing

Branding assets for Blygger: wordmarks, event graphics, and later the real logos
and a page that offers them for download. Not published by `build.py`.

Each image has an HTML source beside it; the PNG is rendered from that, never
edited by hand. To re-render every `*.html` here to a PNG of the same name, run
from `../blygger-studio` (which has Playwright; it drives the installed Chrome):

    node ../blygger-org/marketing/render.mjs

| File | What |
|---|---|
| `wordmark-square.html` → `wordmark-square.png` | 2048×2048. The blygger.org header wordmark (`site.css` `.wordmark`): the `#d95a1f` dot and lowercase `blygger` in the monospace stack, ink `#1b1d22` on paper `#f6f4ee`. Made for the hackathon (2026-11-04). |
