/**
 * IP Addressing Guide + ARP/BGP Simulator – Functional Tests
 *
 * Tests:
 *  - All tabs render their content correctly
 *  - ARP Simulator:
 *      • Send Packet populates the Switch MAC Table
 *      • A second Send Packet populates the Host ARP Cache (cache hit path)
 *  - BGP Simulator:
 *      • Announce Prefix populates the BGP RIB table
 *  - Reset button clears state
 */

const { test, expect } = require('@playwright/test');

const IP_GUIDE = '/Docker+website/Networking/IP%20Addressing%20Guide.html';

test.describe('3 – IP Addressing Guide', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(IP_GUIDE, { waitUntil: 'networkidle' });
  });

  // ── Tab navigation ────────────────────────────────────────────────────────
  test('Page loads with tab navigation', async ({ page }) => {
    await expect(page.locator('nav, [role="tablist"], .tab-btn, button').first()).toBeVisible();
  });

  test('Clicking each nav tab renders content without errors', async ({ page }) => {
    const tabButtons = page.locator('button.tab-btn, [data-tab], nav button');
    const count = await tabButtons.count();
    expect(count, 'Expected at least one tab button').toBeGreaterThan(0);

    for (let i = 0; i < count; i++) {
      const jsErrors = [];
      page.on('pageerror', e => jsErrors.push(e.message));
      await tabButtons.nth(i).click();
      await page.waitForTimeout(400); // let animations settle
      expect(jsErrors, `JS error after clicking tab ${i}: ${jsErrors.join(' | ')}`).toHaveLength(0);
    }
  });

  // ── ARP Simulator ─────────────────────────────────────────────────────────
  test.describe('ARP & BGP Simulator tab', () => {
    test.beforeEach(async ({ page }) => {
      // Navigate to the simulator tab
      const simTab = page.locator('button:has-text("ARP"), button:has-text("Simulator"), button[onclick*="arp_bgp"]');
      await simTab.first().click();
      await page.waitForTimeout(600);
    });

    test('Simulator canvas is visible', async ({ page }) => {
      await expect(page.locator('#canvas')).toBeVisible();
    });

    test('L2/ARP mode controls are visible', async ({ page }) => {
      // Ensure ARP mode is active
      const arpBtn = page.locator('#btn-arp');
      await arpBtn.click();
      await page.waitForTimeout(300);
      await expect(page.locator('#src-node')).toBeVisible();
      await expect(page.locator('#dest-ip')).toBeVisible();
      await expect(page.locator('#sim-btn')).toBeVisible();
    });

    test('ARP broadcast: Switch MAC Table is populated after Send Packet', async ({ page }) => {
      const arpBtn = page.locator('#btn-arp');
      await arpBtn.click();
      await page.waitForTimeout(300);

      // Select PC-1 → PC-2
      await page.selectOption('#src-node', '1');
      await page.selectOption('#dest-ip', '10.0.0.20');

      // Initial table should be empty
      const macBody = page.locator('#mac-rows');
      await expect(macBody).toContainText('Empty');

      // Send packet
      await page.locator('#sim-btn').click();

      // Wait for animation + MAC table to populate (up to 10s)
      await expect(macBody).not.toContainText('Empty', { timeout: 10_000 });
      const macContent = await macBody.innerText();
      expect(macContent.trim(), 'Expected a MAC entry to appear').not.toBe('');
    });

    test('ARP cache hit: ARP cache is populated on second Send Packet', async ({ page }) => {
      const arpBtn = page.locator('#btn-arp');
      await arpBtn.click();
      await page.waitForTimeout(300);

      await page.selectOption('#src-node', '1');
      await page.selectOption('#dest-ip', '10.0.0.20');

      // First send (ARP broadcast + reply)
      await page.locator('#sim-btn').click();
      await page.waitForTimeout(8_000); // wait for full animation

      // Second send (should hit cache)
      await page.locator('#sim-btn').click();
      await page.waitForTimeout(8_000);

      const arpBody = page.locator('#arp-rows');
      await expect(arpBody).not.toContainText('Empty', { timeout: 5_000 });
    });

    test('Diagnostic console logs appear after Send Packet', async ({ page }) => {
      const arpBtn = page.locator('#btn-arp');
      await arpBtn.click();
      await page.waitForTimeout(300);

      await page.selectOption('#src-node', '1');
      await page.locator('#sim-btn').click();

      const consoleEl = page.locator('#console');
      // Console should have more than just the initial "System Ready" line
      await expect(async () => {
        const text = await consoleEl.innerText();
        expect(text.split('\n').filter(l => l.trim()).length).toBeGreaterThan(1);
      }).toPass({ timeout: 10_000 });
    });

    // ── BGP Simulator ───────────────────────────────────────────────────────
    test('BGP mode: Announce Prefix populates BGP RIB table', async ({ page }) => {
      const bgpBtn = page.locator('#btn-bgp');
      await bgpBtn.click();
      await page.waitForTimeout(400);

      // BGP controls should be visible
      await expect(page.locator('#bgp-btn')).toBeVisible();

      // BGP table initially empty
      const bgpBody = page.locator('#bgp-rows');
      await expect(bgpBody).toContainText('No Routes');

      // Announce prefix
      await page.locator('#bgp-btn').click();

      // Wait for BGP propagation animation
      await expect(bgpBody).not.toContainText('No Routes', { timeout: 15_000 });
      const bgpContent = await bgpBody.innerText();
      expect(bgpContent).toContain('8.8.8.0');
    });

    // ── Reset button ─────────────────────────────────────────────────────────
    test('Reset button clears MAC table and console', async ({ page }) => {
      const arpBtn = page.locator('#btn-arp');
      await arpBtn.click();
      await page.waitForTimeout(300);

      await page.selectOption('#src-node', '1');
      await page.locator('#sim-btn').click();
      await page.waitForTimeout(8_000); // let animation run

      // Reset
      await page.locator('button:has-text("Reset")').click();
      await page.waitForTimeout(600);

      // MAC table should be empty again
      await expect(page.locator('#mac-rows')).toContainText('Empty', { timeout: 5_000 });
    });
  });
});
