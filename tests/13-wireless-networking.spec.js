const { test, expect } = require('@playwright/test');

test.describe('13 – Wireless Networking & Security Modules', () => {

  test('Network Security Guide: Wireless Security tab and interactive tools', async ({ page }) => {
    await page.goto('/Networking/Network_Security_Guide.html', { waitUntil: 'networkidle' });

    // Verify Wireless Security tab button exists
    const wifiTabBtn = page.locator('#tab-wireless_security');
    await expect(wifiTabBtn).toBeVisible();
    await expect(wifiTabBtn).toContainText('Wireless Security');

    // Click tab
    await wifiTabBtn.click();
    await expect(page.locator('h1', { hasText: 'Wireless Security, WPA3 & AAA' })).toBeVisible();

    // Verify Section 1: Open Wi-Fi, Hotspots & Captive Portals
    await expect(page.locator('h2', { hasText: 'Open Wi-Fi, Hotspots & Captive Portals' })).toBeVisible();

    // Verify Section 2: Interactive 802.11 Encryption Protocol Analyzer
    await expect(page.locator('h2', { hasText: 'The Evolution of Wi-Fi Encryption' })).toBeVisible();
    const btnWpa3 = page.locator('#btn-proto-WPA3');
    await expect(btnWpa3).toBeVisible();
    await btnWpa3.click();
    await expect(page.locator('#proto-name')).toHaveText(/WPA3/);
    await expect(page.locator('#proto-cipher')).toHaveText(/AES-GCM|GCMP-256/);

    const btnWep = page.locator('#btn-proto-WEP');
    await expect(btnWep).toBeVisible();
    await btnWep.click();
    await expect(page.locator('#proto-name')).toHaveText(/WEP/);
    await expect(page.locator('#proto-badge')).toHaveText(/CRITICALLY BROKEN/);

    // Verify Section 3: Interactive Authentication Mode Simulator
    await expect(page.locator('h2', { hasText: 'Wi-Fi Authentication: Personal (PSK) vs. Enterprise (802.1X)' })).toBeVisible();
    const btnEnterprise = page.locator('#btn-auth-enterprise');
    await expect(btnEnterprise).toBeVisible();
    await btnEnterprise.click();
    await expect(page.locator('#auth-flow-container')).toContainText('WPA-Enterprise (802.1X + RADIUS)');
    await expect(page.locator('#auth-flow-container')).toContainText('EAP-over-RADIUS Relay (UDP Port 1812)');

    const btnPersonal = page.locator('#btn-auth-personal');
    await btnPersonal.click();
    await expect(page.locator('#auth-flow-container')).toContainText('WPA-Personal (PSK)');

    // Verify Section 4: Centralized AAA Framework
    await expect(page.locator('h2', { hasText: 'Centralized AAA Framework: RADIUS vs. TACACS+' })).toBeVisible();
    await expect(page.locator('table', { hasText: 'RADIUS (Remote Authentication Dial-In)' })).toBeVisible();

    // Verify Section 5: RF Containment & Transmit Power
    await expect(page.locator('h2', { hasText: 'Physical RF Containment, Transmit Power Tuning & Antenna Engineering' })).toBeVisible();
  });

  test('Network Components Guide: Wireless & RF Architecture section', async ({ page }) => {
    await page.goto('/Networking/Network_components.html', { waitUntil: 'networkidle' });

    // Quick jump link
    const wifiJumpLink = page.locator('a[href="#wireless-architecture"]').first();
    await expect(wifiJumpLink).toBeVisible();

    // WLAN card in network-types
    await expect(page.locator('h4', { hasText: 'Wireless Local Area Network (WLAN)' })).toBeVisible();

    // Section 10: Wireless Architecture
    const wifiSection = page.locator('#wireless-architecture');
    await expect(wifiSection).toBeVisible();
    await expect(wifiSection.locator('h3')).toContainText('Wireless Networks, RF Physics & Mesh Architecture');

    // Standards table presence
    await expect(wifiSection.locator('table', { hasText: '802.11be (Wi-Fi 7)' })).toBeVisible();

    // Operating modes
    await expect(wifiSection.locator('h5', { hasText: 'Infrastructure Mode' })).toBeVisible();
    await expect(wifiSection.locator('h5', { hasText: 'Ad-Hoc Mode' })).toBeVisible();

    // Attenuation heat map
    await expect(wifiSection.locator('text=Enterprise Wi-Fi RF Heat Map Calibration Scale')).toBeVisible();

    // Extension comparison: Repeaters vs APs vs Mesh
    await expect(wifiSection.locator('text=Wireless Mesh System')).toBeVisible();
    await expect(wifiSection.locator('text=Dedicated Backhaul Channel')).toBeVisible();
  });

  test('Networking Hub: Command Cheat Sheet wireless CLI tools', async ({ page }) => {
    await page.goto('/Networking/Network_index.html', { waitUntil: 'networkidle' });

    // Navigate to cheatsheet tab
    const cheatTab = page.locator('#nav-tabs button', { hasText: 'Command Cheat Sheet' });
    await cheatTab.click();

    // Check for wireless commands
    await expect(page.locator('text=Wireless & Wi-Fi Management (CLI)')).toBeVisible();
    await expect(page.locator('text=nmcli dev wifi list')).toBeVisible();
    await expect(page.locator('text=iwconfig')).toBeVisible();
  });

});
