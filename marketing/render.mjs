// Renders each marketing/*.html source to a PNG of the same name at its body size.
// Run from blygger-studio, which has Playwright installed:
//   node ../blygger-org/marketing/render.mjs
import { chromium } from 'playwright';
import { readdirSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, join } from 'node:path';

const dir = dirname(fileURLToPath(import.meta.url));
const browser = await chromium.launch({ channel: 'chrome' }); // the installed Chrome; no Playwright download needed
for (const name of readdirSync(dir).filter(f => f.endsWith('.html'))) {
  const page = await browser.newPage({ viewport: { width: 2048, height: 2048 } });
  await page.goto(pathToFileURL(join(dir, name)).href);
  await page.evaluate(() => document.fonts.ready);
  const out = join(dir, name.replace(/\.html$/, '.png'));
  await page.locator('body').screenshot({ path: out });
  console.log('wrote', out);
  await page.close();
}
await browser.close();
