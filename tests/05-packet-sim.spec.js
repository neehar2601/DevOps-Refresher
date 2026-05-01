/**
 * Packet Simulator – Functional Tests
 *
 * Tests:
 *  - Page loads with both mode tabs (Encapsulation, Journey)
 *  - Encapsulation mode: clicking OSI stage buttons changes the displayed layer
 *  - Journey mode: Next/Prev device buttons step through network devices
 *  - Device cards are clickable and update the view
 */

const { test, expect } = require('@playwright/test');

const PACKET_SIM = '/Docker+website/Networking/Packet_sim.html';

test.describe('5 – Packet Simulator', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(PACKET_SIM, { waitUntil: 'networkidle' });
  });

  test('Page title contains "Packet" or "Simulator"', async ({ page }) => {
    await expect(page).toHaveTitle(/packet|simulator/i);
  });

  test('Encapsulation tab is present', async ({ page }) => {
    await expect(page.locator('#tab-encap')).toBeVisible();
  });

  test('Journey tab is present', async ({ page }) => {
    await expect(page.locator('#tab-journey')).toBeVisible();
  });

  // ── Encapsulation mode ────────────────────────────────────────────────────
  test.describe('Encapsulation mode', () => {
    test.beforeEach(async ({ page }) => {
      await page.locator('#tab-encap').click();
      await page.waitForTimeout(400);
    });

    test('Stage buttons are visible', async ({ page }) => {
      const stageButtons = page.locator('.stage-btn');
      const count = await stageButtons.count();
      expect(count, 'Expected at least 4 OSI stage buttons').toBeGreaterThanOrEqual(4);
    });

    test('Clicking each stage button updates the view', async ({ page }) => {
      const stageButtons = page.locator('.stage-btn');
      const count = await stageButtons.count();

      for (let i = 0; i < count; i++) {
        const textBefore = await page.locator('#encap-view, [id*="stage"], main').innerText().catch(() => '');
        await stageButtons.nth(i).click();
        await page.waitForTimeout(400);
        // Each stage should have an active class applied
        const activeCls = await stageButtons.nth(i).getAttribute('class');
        expect(activeCls, `Stage ${i} button should become active`).toContain('active');
      }
    });
  });

  // ── Journey mode ──────────────────────────────────────────────────────────
  test.describe('Journey mode', () => {
    test.beforeEach(async ({ page }) => {
      await page.locator('#tab-journey').click();
      await page.waitForTimeout(400);
    });

    test('Next device button is visible', async ({ page }) => {
      await expect(page.locator('#dev-next-btn')).toBeVisible();
    });

    test('Prev device button is visible', async ({ page }) => {
      await expect(page.locator('#dev-prev-btn')).toBeVisible();
    });

    test('Next button advances through devices', async ({ page }) => {
      const nextBtn = page.locator('#dev-next-btn');
      const contentBefore = await page.locator('body').innerText();
      await nextBtn.click();
      await page.waitForTimeout(500);
      const contentAfter = await page.locator('body').innerText();
      expect(contentAfter).not.toEqual(contentBefore);
    });

    test('Device cards are clickable', async ({ page }) => {
      const deviceCards = page.locator('.device-card');
      const count = await deviceCards.count();
      expect(count, 'Expected at least 4 device cards').toBeGreaterThanOrEqual(4);

      // Click the last card and check active state changes
      await deviceCards.last().click();
      await page.waitForTimeout(400);
      const activeCls = await deviceCards.last().getAttribute('class');
      expect(activeCls, 'Clicked device card should be active').toContain('active');
    });
  });
});
