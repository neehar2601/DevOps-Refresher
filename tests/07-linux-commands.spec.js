const { test, expect } = require('@playwright/test');

const LINUX_COMMANDS = '/Linux/linux_commands.html';

test.describe('7 – Linux Commands Guide', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(LINUX_COMMANDS, { waitUntil: 'networkidle' });
  });

  test('Page title contains "Commands"', async ({ page }) => {
    await expect(page).toHaveTitle(/Commands/i);
  });

  test('System & Basic Info section is visible', async ({ page }) => {
    await page.locator('button', { hasText: 'System & Basic Info' }).click();
    const section = page.locator('h2', { hasText: 'System & Basic Info' });
    await expect(section).toBeVisible();
  });

  test('Navigation & File Operations section is visible', async ({ page }) => {
    await page.locator('button', { hasText: 'Nav & File Ops' }).click();
    const section = page.locator('h2', { hasText: 'Navigation & File Operations' });
    await expect(section).toBeVisible();
  });

  test('Package Management (APT) section is visible', async ({ page }) => {
    await page.locator('button', { hasText: 'Packages' }).click();
    const section = page.locator('h2', { hasText: 'Package Management (APT)' });
    await expect(section).toBeVisible();
  });
  test('Text Editors (Vim) section is visible', async ({ page }) => {
    await page.locator('button', { hasText: 'Text Editors' }).click();
    const section = page.locator('h2', { hasText: 'Text Editors (Vim)' });
    await expect(section).toBeVisible();
  });
});
