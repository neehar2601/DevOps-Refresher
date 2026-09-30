/**
 * Networking Hub – Functional Tests
 *
 * Tests the Networking section landing page:
 *  - Guide cards render (all 7 deep-dive modules)
 *  - Links to sub-pages resolve without 404
 *  - Navigation tabs (Intro, Packet Journey, Command Cheat Sheet) switch correctly
 *  - Interactive elements (Journey steps, Cheatsheet search) function as expected
 */

const { test, expect } = require('@playwright/test');

const NETWORK_INDEX = '/Networking/Network_index.html';

test.describe('2 – Networking Hub', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(NETWORK_INDEX, { waitUntil: 'networkidle' });
  });

  test('Page title contains "Networking"', async ({ page }) => {
    await expect(page).toHaveTitle(/Networking/i);
  });

  // ── Guide Cards Presence ───────────────────────────────────────────────────

  test('IP Addressing Guide link is present', async ({ page }) => {
    const link = page.locator('a[href*="IP Addressing Guide"], a[href*="IP%20Addressing"], a[href*="IP+Addressing"]').first();
    await expect(link).toBeVisible();
  });

  test('Networking Tools Guide link is present', async ({ page }) => {
    const link = page.locator('a[href*="Networking-Tools-Guide.html"]').first();
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

  test('Network Components Guide link is present', async ({ page }) => {
    const link = page.locator('a[href*="Network_components.html"]').first();
    await expect(link).toBeVisible();
  });

  test('Network Security & VPN Guide link is present', async ({ page }) => {
    const link = page.locator('a[href*="Network_Security_Guide.html"]').first();
    await expect(link).toBeVisible();
  });

  // ── Sub-page Navigation & Loading ──────────────────────────────────────────

  test('IP Addressing Guide page loads from nav link', async ({ page }) => {
    const link = page.locator('a[href*="IP Addressing Guide"], a[href*="IP%20Addressing"], a[href*="IP+Addressing"]').first();
    const [response] = await Promise.all([
      page.waitForResponse(resp => (resp.url().includes('IP') || resp.url().includes('Addressing')) && resp.status() < 400),
      link.click(),
    ]);
    expect(response.status()).toBeLessThan(400);
  });

  test('Networking Tools Guide page loads from nav link', async ({ page }) => {
    const link = page.locator('a[href*="Networking-Tools-Guide.html"]').first();
    const [response] = await Promise.all([
      page.waitForResponse(resp => resp.url().includes('Networking-Tools-Guide') && resp.status() < 400),
      link.click(),
    ]);
    expect(response.status()).toBeLessThan(400);
  });

  test('DNS Guide page loads from nav link', async ({ page }) => {
    const link = page.locator('a[href*="DNS_guide"]').first();
    const [response] = await Promise.all([
      page.waitForResponse(resp => resp.url().includes('DNS_guide') && resp.status() < 400),
      link.click(),
    ]);
    expect(response.status()).toBeLessThan(400);
  });

  test('DNS Simulator page loads from nav link', async ({ page }) => {
    const link = page.locator('a[href*="DNS_sim"]').first();
    const [response] = await Promise.all([
      page.waitForResponse(resp => resp.url().includes('DNS_sim') && resp.status() < 400),
      link.click(),
    ]);
    expect(response.status()).toBeLessThan(400);
  });

  test('Packet Simulator page loads from nav link', async ({ page }) => {
    const link = page.locator('a[href*="Packet_sim"]').first();
    const [response] = await Promise.all([
      page.waitForResponse(resp => resp.url().includes('Packet_sim') && resp.status() < 400),
      link.click(),
    ]);
    expect(response.status()).toBeLessThan(400);
  });

  test('Network Components Guide page loads from nav link', async ({ page }) => {
    const link = page.locator('a[href*="Network_components.html"]').first();
    const [response] = await Promise.all([
      page.waitForResponse(resp => resp.url().includes('Network_components') && resp.status() < 400),
      link.click(),
    ]);
    expect(response.status()).toBeLessThan(400);
  });

  test('Network Security & VPN Guide page loads from nav link', async ({ page }) => {
    const link = page.locator('a[href*="Network_Security_Guide.html"]').first();
    const [response] = await Promise.all([
      page.waitForResponse(resp => resp.url().includes('Network_Security_Guide') && resp.status() < 400),
      link.click(),
    ]);
    expect(response.status()).toBeLessThan(400);
  });

  // ── Navigation Tabs & Dynamic Content ──────────────────────────────────────

  test('Introduction tab renders core sections and deep-dive modules', async ({ page }) => {
    const heading = page.locator('h2', { hasText: 'What is Networking & Network Types' });
    await expect(heading).toBeVisible();
    await expect(page.locator('h3', { hasText: 'What is a Network?' })).toBeVisible();
    await expect(page.locator('h3', { hasText: 'Specialized Deep-Dive Guides & Simulators' })).toBeVisible();
  });

  test('Packet Journey tab switches, displays OSI layers and simulation controls', async ({ page }) => {
    await page.locator('#nav-tabs button', { hasText: 'Packet Journey' }).click();
    await expect(page.locator('h2', { hasText: 'Packet Journey & OSI Model' })).toBeVisible();

    const startBtn = page.locator('#journey-start-btn');
    await expect(startBtn).toBeVisible();

    // Start simulation step
    await startBtn.click();
    const counter = page.locator('#journey-step-counter');
    await expect(counter).toHaveText(/1 \/ 9/);

    const nextBtn = page.locator('#journey-next-btn');
    await expect(nextBtn).toBeEnabled();
    await nextBtn.click();
    await expect(counter).toHaveText(/2 \/ 9/);
  });

  test('Command Cheat Sheet tab switches and search filter works', async ({ page }) => {
    await page.locator('#nav-tabs button', { hasText: 'Command Cheat Sheet' }).click();
    await expect(page.locator('h2', { hasText: 'Command Cheat Sheet' })).toBeVisible();

    const searchInput = page.locator('#cheatsheet-search');
    await expect(searchInput).toBeVisible();

    // Filter commands by 'ping'
    await searchInput.fill('ping');
    await page.waitForTimeout(300);
    const visibleCmds = page.locator('.cheatsheet-item:visible');
    const count = await visibleCmds.count();
    expect(count).toBeGreaterThan(0);
    await expect(page.locator('.cheatsheet-item:visible', { hasText: 'ping' }).first()).toBeVisible();
  });
});
