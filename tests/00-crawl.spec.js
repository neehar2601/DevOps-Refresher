/**
 * Dynamic Site Crawler
 *
 * Starting from the homepage, this test dynamically discovers all internal
 * links reachable from the S3 deployment and asserts a baseline health check
 * for every page found (no HTTP errors, title present, no JS crashes).
 *
 * The discovered URL list is exported via a global fixture so per-page
 * functional tests can consume it without re-crawling.
 */

const { test, expect } = require('@playwright/test');
const fs = require('fs');
const path = require('path');

const ENTRY = '/Docker+website/index.html';
const ORIGIN = process.env.BASE_URL || 'https://devops-learner.s3.us-east-2.amazonaws.com';
// URLs to skip (external CDN, fonts, etc.)
const SKIP_PATTERNS = [
  /^https?:\/\/(?!devops-learner\.s3)/,
  /\.(css|js|png|jpg|svg|ico|woff2?)$/i,
  /javascript:/,
  /^mailto:/,
  /#$/,
];

function shouldSkip(url) {
  return SKIP_PATTERNS.some(p => p.test(url));
}

function normalise(href, pageUrl) {
  try {
    const resolved = new URL(href, pageUrl);
    resolved.hash = '';
    return resolved.href;
  } catch {
    return null;
  }
}

test.describe('0 – Dynamic site crawl', () => {
  test('Crawl all pages reachable from the homepage', async ({ page }) => {
    const visited = new Set();
    const queue = [`${ORIGIN}${ENTRY}`];
    const failed = [];

    while (queue.length > 0) {
      const url = queue.shift();
      if (visited.has(url)) continue;
      visited.add(url);

      console.log(`[crawl] visiting → ${url}`);

      // ── Collect console errors ─────────────────────────────────────
      const jsErrors = [];
      page.on('pageerror', e => jsErrors.push(e.message));

      const response = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30_000 });

      // ── Assert: page responded without server error ────────────────
      if (response) {
        expect(
          response.status(),
          `HTTP error on ${url}: ${response.status()}`
        ).toBeLessThan(400);
      }

      // ── Assert: page has a <title> ─────────────────────────────────
      const title = await page.title();
      expect(title.trim(), `Missing <title> on ${url}`).not.toBe('');

      // ── Assert: no unhandled JS exceptions ────────────────────────
      expect(
        jsErrors,
        `JS errors on ${url}: ${jsErrors.join(' | ')}`
      ).toHaveLength(0);

      // ── Discover new internal links ────────────────────────────────
      const links = await page.evaluate(() =>
        Array.from(document.querySelectorAll('a[href]')).map(a => a.getAttribute('href'))
      );

      for (const href of links) {
        if (!href) continue;
        const abs = normalise(href, url);
        if (!abs) continue;
        if (!abs.startsWith(ORIGIN)) continue;
        if (shouldSkip(abs)) continue;
        if (!visited.has(abs) && !queue.includes(abs)) {
          queue.push(abs);
        }
      }
    }

    // Persist discovered URLs for other test files
    const outDir = path.join(__dirname, '.discovered');
    fs.mkdirSync(outDir, { recursive: true });
    fs.writeFileSync(
      path.join(outDir, 'urls.json'),
      JSON.stringify([...visited], null, 2)
    );

    console.log(`[crawl] total pages visited: ${visited.size}`);
    expect(visited.size, 'Crawler found no pages at all').toBeGreaterThan(0);
  });
});
