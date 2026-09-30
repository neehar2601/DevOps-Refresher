const { test, expect } = require('@playwright/test');

const LINUX_NETWORKING = '/Linux/linux_networking.html';

test.describe('10 – Linux Networking Guide', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(LINUX_NETWORKING, { waitUntil: 'networkidle' });
  });

  test('Page title contains "Networking"', async ({ page }) => {
    await expect(page).toHaveTitle(/Networking/i);
  });

  test('Process Management section is visible', async ({ page }) => {
    await page.locator('button', { hasText: 'Process Management' }).click();
    const section = page.locator('h2', { hasText: 'Process Management' });
    await expect(section).toBeVisible();
  });

  test('Networking Essentials section is visible', async ({ page }) => {
    await page.locator('button', { hasText: 'Networking Essentials' }).click();
    const section = page.locator('h2', { hasText: 'Networking Essentials' });
    await expect(section).toBeVisible();
  });
});
