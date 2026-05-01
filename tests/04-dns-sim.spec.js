/**
 * DNS Simulator – Functional Tests
 *
 * Tests:
 *  - Page loads and displays query panel
 *  - Recursive mode tab is default
 *  - Iterative mode tab switches correctly
 *  - Auto mode: clicking Play starts the animation and shows steps
 *  - Step mode: Next button progresses through steps
 *  - Reset button brings simulator back to initial state
 */

const { test, expect } = require('@playwright/test');

const DNS_SIM = '/Docker+website/Networking/DNS_sim.html';

test.describe('4 – DNS Simulator', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(DNS_SIM, { waitUntil: 'networkidle' });
  });

  test('Page title contains "DNS"', async ({ page }) => {
    await expect(page).toHaveTitle(/DNS/i);
  });

  test('Recursive tab is active by default', async ({ page }) => {
    const recursiveTab = page.locator('#tab-recursive');
    await expect(recursiveTab).toBeVisible();
    // Check it has an active class
    const cls = await recursiveTab.getAttribute('class');
    expect(cls, 'Recursive tab should be active by default').toContain('active');
  });

  test('Iterative tab switches mode', async ({ page }) => {
    const iterativeTab = page.locator('#tab-iterative');
    await iterativeTab.click();
    await page.waitForTimeout(300);
    const cls = await iterativeTab.getAttribute('class');
    expect(cls, 'Iterative tab should be active after click').toContain('active');
  });

  test('Play button is visible', async ({ page }) => {
    await expect(page.locator('#btn-play')).toBeVisible();
  });

  test('Auto mode: clicking Play triggers simulation steps', async ({ page }) => {
    // Ensure auto mode is active
    await page.locator('#mode-auto').click();
    await page.waitForTimeout(200);

    await page.locator('#btn-play').click();

    // After play, at least one step/log entry should appear within 10s
    await expect(async () => {
      const logs = await page.locator('[class*="log"], [class*="step"], [class*="message"], #dns-log, .log-entry').count();
      expect(logs).toBeGreaterThan(0);
    }).toPass({ timeout: 10_000 });
  });

  test('Step mode: Next button advances simulation', async ({ page }) => {
    await page.locator('#mode-step').click();
    await page.waitForTimeout(200);

    await page.locator('#btn-play').click();
    await page.waitForTimeout(500);

    // Next button should become visible in step mode
    const nextBtn = page.locator('#btn-next');
    await expect(nextBtn).toBeVisible({ timeout: 5_000 });

    // Click Next and assert something changes
    const contentBefore = await page.locator('body').innerText();
    await nextBtn.click();
    await page.waitForTimeout(800);
    const contentAfter = await page.locator('body').innerText();
    expect(contentAfter).not.toEqual(contentBefore);
  });

  test('Reset button restores initial state', async ({ page }) => {
    await page.locator('#btn-play').click();
    await page.waitForTimeout(2_000);

    await page.locator('#btn-reset').click();
    await page.waitForTimeout(500);

    // Play button should be visible again after reset
    await expect(page.locator('#btn-play')).toBeVisible();
  });
});
