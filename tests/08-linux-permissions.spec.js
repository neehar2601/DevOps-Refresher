const { test, expect } = require('@playwright/test');

const LINUX_PERMISSIONS = '/Linux/linux_permissions.html';

test.describe('8 – Linux Permissions Guide', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(LINUX_PERMISSIONS, { waitUntil: 'networkidle' });
  });

  test('Page title contains "Permissions"', async ({ page }) => {
    await expect(page).toHaveTitle(/Permissions/i);
  });

  test('Listing Files & System Identity section is visible', async ({ page }) => {
    const section = page.locator('h2', { hasText: 'Listing Files' });
    await expect(section).toBeVisible();
  });

  test('Permissions Basics section is visible', async ({ page }) => {
    const section = page.locator('h2', { hasText: 'Permissions Basics' });
    await expect(section).toBeVisible();
  });

  test('Identity Management section is visible', async ({ page }) => {
    const section = page.locator('h2', { hasText: 'Identity Management' });
    await expect(section).toBeVisible();
  });
});
