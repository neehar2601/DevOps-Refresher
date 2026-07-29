/**
 * Homepage – Functional Tests
 *
 * Tests the DevOps Learning Hub root page:
 *  - Navigation cards visible and linked correctly
 *  - Live badges present on Git, Docker, Networking
 *  - "Coming soon" toast fires for disabled cards
 *  - Footer present
 */

const { test, expect } = require('@playwright/test');

const HOME = '/index.html';

test.describe('1 – Homepage', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(HOME, { waitUntil: 'networkidle' });
  });

  test('Page title is DevOps Learning Hub', async ({ page }) => {
    await expect(page).toHaveTitle(/DevOps Learning Hub/i);
  });

  test('Header brand is visible', async ({ page }) => {
    await expect(page.locator('header h1')).toContainText('DevOps');
  });

  test('Git card links to git hub', async ({ page }) => {
    const link = page.locator('a[href*="git_index.html"]').first();
    await expect(link).toBeVisible();
    await expect(link).toContainText('Open Git Hub');
  });

  test('Docker card links to docker hub', async ({ page }) => {
    const link = page.locator('a[href*="docker_index.html"]').first();
    await expect(link).toBeVisible();
    await expect(link).toContainText('Open Docker Hub');
  });

  test('Networking card links to networking hub', async ({ page }) => {
    const link = page.locator('a[href*="Network_index.html"]').first();
    await expect(link).toBeVisible();
    await expect(link).toContainText('Open Networking Hub');
  });

  test('Linux card links to linux hub', async ({ page }) => {
    const link = page.locator('a[href*="linux_index.html"]').first();
    await expect(link).toBeVisible();
    await expect(link).toContainText('Open Linux Hub');
  });

  test('Live badges visible for Git, Docker, Networking, Linux', async ({ page }) => {
    const liveBadges = page.locator('span:has-text("Live")');
    await expect(liveBadges).toHaveCount(4);
  });

  test('"Coming soon" cards show toast on click', async ({ page }) => {
    const toast = page.locator('#toast');
    // Click Kubernetes card (first "coming soon")
    await page.locator('h3:has-text("Kubernetes")').click();
    await expect(toast).toBeVisible({ timeout: 3000 });
    await expect(toast).toContainText('Kubernetes');
  });

  test('Footer is visible', async ({ page }) => {
    await expect(page.locator('footer')).toBeVisible();
    await expect(page.locator('footer')).toContainText('DevOps Learning Hub');
  });
});
