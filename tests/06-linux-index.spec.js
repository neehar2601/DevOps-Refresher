/**
 * Linux Hub – Functional Tests
 *
 * Tests the Linux section landing page:
 *  - Guide cards render
 *  - Links to sub-pages resolve without 404
 */

const { test, expect } = require('@playwright/test');

const LINUX_INDEX = '/Linux/linux_index.html';

test.describe('6 – Linux Hub', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(LINUX_INDEX, { waitUntil: 'networkidle' });
  });

  test('Page title contains "Linux"', async ({ page }) => {
    await expect(page).toHaveTitle(/Linux/i);
  });

  test('Filesystem Guide link is present', async ({ page }) => {
    const link = page.locator('a[href*="linux_filesystem.html"]').first();
    await expect(link).toBeVisible();
  });

  test('Boot Process link is present', async ({ page }) => {
    const link = page.locator('a[href*="linux_boot.html"]').first();
    await expect(link).toBeVisible();
  });

  test('Permissions Guide link is present', async ({ page }) => {
    const link = page.locator('a[href*="linux_permissions.html"]').first();
    await expect(link).toBeVisible();
  });

  test('Commands Guide link is present', async ({ page }) => {
    const link = page.locator('a[href*="linux_commands.html"]').first();
    await expect(link).toBeVisible();
  });

  test('Package Management link is present', async ({ page }) => {
    const link = page.locator('a[href*="linux_package_management.html"]').first();
    await expect(link).toBeVisible();
  });

  test('Networking link is present', async ({ page }) => {
    const link = page.locator('a[href*="linux_networking.html"]').first();
    await expect(link).toBeVisible();
  });

  test('Filesystem Guide page loads from nav link', async ({ page }) => {
    const link = page.locator('a[href*="linux_filesystem.html"]').first();
    const [response] = await Promise.all([
      page.waitForResponse(resp => resp.url().includes('linux_filesystem') && resp.status() < 400),
      link.click(),
    ]);
    expect(response.status()).toBeLessThan(400);
  });

  test('Package Management page loads from nav link', async ({ page }) => {
    const link = page.locator('a[href*="linux_package_management.html"]').first();
    const [response] = await Promise.all([
      page.waitForResponse(resp => resp.url().includes('linux_package_management') && resp.status() < 400),
      link.click(),
    ]);
    expect(response.status()).toBeLessThan(400);
  });

  test('Networking page loads from nav link', async ({ page }) => {
    const link = page.locator('a[href*="linux_networking.html"]').first();
    const [response] = await Promise.all([
      page.waitForResponse(resp => resp.url().includes('linux_networking') && resp.status() < 400),
      link.click(),
    ]);
    expect(response.status()).toBeLessThan(400);
  });
});
