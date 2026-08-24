const { test, expect } = require('@playwright/test');

const LINUX_LOGGING = '/Linux/linux_logging.html';

test.describe('11 – Linux Logging & Monitoring Guide', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(LINUX_LOGGING, { waitUntil: 'networkidle' });
  });

  test('Page title contains "Logging"', async ({ page }) => {
    await expect(page).toHaveTitle(/Logging/i);
  });

  test('Core Concepts section is visible', async ({ page }) => {
    await page.locator('button', { hasText: 'Core Concepts' }).click();
    const section = page.locator('h3', { hasText: 'Logging Services' });
    await expect(section).toBeVisible();
  });

  test('Daemons & Configs section is visible', async ({ page }) => {
    await page.locator('button', { hasText: 'Daemons & Configs' }).click();
    const section = page.locator('h3', { hasText: 'The syslogd Utility' });
    await expect(section).toBeVisible();
  });

  test('Common Files & Tools section is visible', async ({ page }) => {
    await page.locator('button', { hasText: 'Common Files & Tools' }).click();
    const section = page.locator('h3', { hasText: 'Common Log Files' });
    await expect(section).toBeVisible();
  });
});
