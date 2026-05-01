/**
 * Networking Hub – Functional Tests
 *
 * Tests the Networking section landing page:
 *  - Guide cards render
 *  - Links to sub-pages resolve without 404
 *  - Packet Flow / Simulation entry points visible
 */

const { test, expect } = require('@playwright/test');

const NETWORK_INDEX = '/Docker+website/Networking/Network_index.html';

test.describe('2 – Networking Hub', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(NETWORK_INDEX, { waitUntil: 'networkidle' });
  });

  test('Page title contains "Networking"', async ({ page }) => {
    await expect(page).toHaveTitle(/Networking/i);
  });

  test('IP Addressing Guide link is present', async ({ page }) => {
    const link = page.locator('a[href*="IP Addressing Guide"], a[href*="IP+Addressing"]').first();
    await expect(link).toBeVisible();
  });

  test('DNS Guide link is present', async ({ page }) => {
    const link = page.locator('a[href*="DNS_guide"]').first();
    await expect(link).toBeVisible();
  });

  test('DNS Simulator link is present', async ({ page }) => {
    const link = page.locator('a[href*="DNS_sim"]').first();
    await expect(link).toBeVisible();
  });

  test('Packet Simulator link is present', async ({ page }) => {
    const link = page.locator('a[href*="Packet_sim"]').first();
    await expect(link).toBeVisible();
  });

  test('IP Addressing Guide page loads from nav link', async ({ page }) => {
    const link = page.locator('a[href*="IP Addressing Guide"], a[href*="IP+Addressing"]').first();
    const href = await link.getAttribute('href');
    const [response] = await Promise.all([
      page.waitForResponse(resp => resp.url().includes('IP') && resp.status() < 400),
      link.click(),
    ]);
    expect(response.status()).toBeLessThan(400);
  });
});
