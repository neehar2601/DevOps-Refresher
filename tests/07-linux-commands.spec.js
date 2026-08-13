const { test, expect } = require('@playwright/test');

const LINUX_COMMANDS = '/Linux/linux_commands.html';

test.describe('7 – Linux Commands Guide', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(LINUX_COMMANDS, { waitUntil: 'networkidle' });
  });

  test('Page title contains "Commands"', async ({ page }) => {
    await expect(page).toHaveTitle(/Commands/i);
  });

  test('System Awareness section is visible', async ({ page }) => {
    const section = page.locator('h2', { hasText: 'System Awareness' });
    await expect(section).toBeVisible();
  });

  test('Navigation section is visible', async ({ page }) => {
    const section = page.locator('h2', { hasText: 'Navigation' });
    await expect(section).toBeVisible();
  });

  test('Package Management (APT) section is visible', async ({ page }) => {
    const section = page.locator('h2', { hasText: 'Package Management (APT)' });
    await expect(section).toBeVisible();
  });
});
