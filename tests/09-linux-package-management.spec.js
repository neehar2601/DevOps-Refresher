const { test, expect } = require('@playwright/test');

const LINUX_PACKAGE_MANAGEMENT = '/Linux/linux_package_management.html';

test.describe('9 – Linux Package Management Guide', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(LINUX_PACKAGE_MANAGEMENT, { waitUntil: 'networkidle' });
  });

  test('Page title contains "Package Management"', async ({ page }) => {
    await expect(page).toHaveTitle(/Package Management/i);
  });

  test('The Concept of Package Management section is visible', async ({ page }) => {
    const section = page.locator('h2', { hasText: 'The Concept of Package Management' });
    await expect(section).toBeVisible();
  });

  test('Updating and Upgrading section is visible', async ({ page }) => {
    const section = page.locator('h2', { hasText: '1. Updating and Upgrading' });
    await expect(section).toBeVisible();
  });

  test('Searching and Installing section is visible', async ({ page }) => {
    const section = page.locator('h2', { hasText: '2. Searching and Installing' });
    await expect(section).toBeVisible();
  });

  test('Removing and Purging Software section is visible', async ({ page }) => {
    const section = page.locator('h2', { hasText: '3. Removing and Purging Software' });
    await expect(section).toBeVisible();
  });

  test('System Housekeeping section is visible', async ({ page }) => {
    const section = page.locator('h2', { hasText: '4. System Housekeeping' });
    await expect(section).toBeVisible();
  });
});
