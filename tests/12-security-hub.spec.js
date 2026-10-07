/**
 * Security & Cybersecurity Hub – Functional Tests
 *
 * Tests the Security Hub landing page:
 *  - Header, hero, and navigation links
 *  - CIA Triad interactive explorer
 *  - Risk ROI calculator and heatmap
 *  - IAM & Access Control section (Claim/AuthN, MFA, Kerberos stepper, ACL simulator, 5 Access Control models)
 *  - Endpoint Hardening, Patch Management & Application Control (Scorecard, Allow/Deny simulator, Sandbox)
 *  - DevSecOps pipeline simulator
 *  - Digital Signatures, HTTPS Handshake, Chain of Trust, and Key Escrow
 *  - Knowledge Quiz engine (30 comprehensive questions)
 */

const { test, expect } = require('@playwright/test');

const SECURITY_INDEX = '/Security/security_index.html';

test.describe('12 – Security Hub', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(SECURITY_INDEX, { waitUntil: 'networkidle' });
  });

  test('Page title contains "Security"', async ({ page }) => {
    await expect(page).toHaveTitle(/Security/i);
  });

  test('Top navigation contains IAM & Access Control link', async ({ page }) => {
    const iamLink = page.locator('a[href="#iam-access-control"]').first();
    await expect(iamLink).toBeVisible();
    await expect(iamLink).toContainText('IAM & Access Control');
  });

  test('Top navigation contains Endpoint Hardening link', async ({ page }) => {
    const ehLink = page.locator('a[href="#endpoint-hardening"]').first();
    await expect(ehLink).toBeVisible();
    await expect(ehLink).toContainText('Endpoint Hardening');
  });

  test('IAM section renders all 5 parts and interactive tools', async ({ page }) => {
    const iamSection = page.locator('#iam-access-control');
    await expect(iamSection).toBeVisible();
    await expect(iamSection).toContainText('Authentication, SSO & Access Control');

    // Claim demo container
    await expect(page.locator('#iam-claim-box')).toBeVisible();

    // MFA lab grid and presets
    await expect(page.locator('#iam-method-grid')).toBeVisible();
    await expect(page.locator('#iam-mfa-badge')).toBeVisible();

    // Kerberos stepper
    await expect(page.locator('#iam-kerb-steps')).toBeVisible();
    await expect(page.locator('#iam-kerb-detail')).toBeVisible();

    // ACL & Implicit deny simulator
    await expect(page.locator('#iam-acl-user')).toBeVisible();
    await expect(page.locator('#iam-acl-resource')).toBeVisible();
    await expect(page.locator('#iam-acl-result')).toBeVisible();

    // 5 Access Control models tabs
    await expect(page.locator('#iam-model-tabs')).toBeVisible();
    await expect(page.locator('#iam-model-detail')).toBeVisible();
  });

  test('MFA Strength lab updates badge and factor count on preset click', async ({ page }) => {
    await page.locator('button:has-text("Bank Card + PIN")').click();
    await expect(page.locator('#iam-mfa-badge')).toContainText('MULTI-FACTOR (2FA)');
    await expect(page.locator('#iam-mfa-count')).toContainText('2 / 5');
  });

  test('ACL simulator correctly tests implicit deny', async ({ page }) => {
    await page.locator('#iam-acl-user').selectOption('alice');
    await page.locator('#iam-acl-resource').selectOption('vault');
    await expect(page.locator('#iam-acl-result')).toContainText('ACCESS DENIED — Implicit Deny');
  });

  test('Access control models tabs switch correctly', async ({ page }) => {
    await page.locator('#iam-model-tabs button:has-text("ABAC")').click();
    await expect(page.locator('#iam-model-detail')).toContainText('Attribute-Based Access Control');
  });

  test('Endpoint hardening section renders interactive scorecard and simulator', async ({ page }) => {
    const ehSection = page.locator('#endpoint-hardening');
    await expect(ehSection).toBeVisible();
    await expect(ehSection).toContainText('Endpoint Hardening, Patching & Application Control');

    // Hardening scorecard
    await expect(page.locator('#eh-score-badge')).toContainText('100%');

    // Application control simulator
    await expect(page.locator('#eh-sim-app')).toBeVisible();
    await expect(page.locator('#eh-sim-mode')).toBeVisible();
    await expect(page.locator('#eh-sim-result')).toBeVisible();
  });

  test('Application Control simulator blocks zero-day on Allow List policy', async ({ page }) => {
    await page.locator('#eh-sim-app').selectOption('zeroday');
    await page.locator('#eh-sim-mode').selectOption('allowlist');
    await expect(page.locator('#eh-sim-result')).toContainText('EXECUTION BLOCKED (Implicit Deny)');
  });

  test('Top navigation contains Certificates & HTTPS link', async ({ page }) => {
    const certLink = page.locator('a[href="#certificates-https"]').first();
    await expect(certLink).toBeVisible();
    await expect(certLink).toContainText('Certificates & HTTPS');
  });

  test('Digital signature lab generates signature and detects tampering', async ({ page }) => {
    const sigLab = page.locator('#cert-signatures');
    await expect(sigLab).toBeVisible();
    await expect(page.locator('#sig-hash-display')).toBeVisible();

    // Tamper with payload
    await sigLab.locator('button:has-text("Tamper")').click();
    await expect(page.locator('#sig-result-box')).toContainText('SIGNATURE FAILED');

    // Reset payload
    await sigLab.locator('button:has-text("Reset")').click();
    await expect(page.locator('#sig-result-box')).toContainText('SIGNATURE VALID');
  });

  test('Certificate Inspector correctly identifies secure vs mismatch domains', async ({ page }) => {
    const inspector = page.locator('#cert-domain-matching');
    await expect(inspector).toBeVisible();
    await expect(page.locator('#cert-status-pill')).toContainText('SECURE');

    // Input invalid domain
    await page.locator('#cert-test-domain').fill('bank.net');
    await expect(page.locator('#cert-status-pill')).toContainText('INSECURE');
  });

  test('HTTPS Handshake visualizer advances through steps', async ({ page }) => {
    const httpsSection = page.locator('#https-architecture');
    await expect(httpsSection).toBeVisible();
    await expect(page.locator('#https-step-counter')).toContainText('Step 1 of 6');

    // Click Next
    await httpsSection.locator('button:has-text("Next")').first().click();
    await expect(page.locator('#https-step-counter')).toContainText('Step 2 of 6');
  });

  test('PKI Chain of Trust interactive visualizer displays node details on click', async ({ page }) => {
    const chainSection = page.locator('#cert-chain-escrow');
    await expect(chainSection).toBeVisible();
    await expect(chainSection).toContainText('Chain of Trust');

    // Click Root CA
    await page.locator('#chain-btn-root').click();
    await expect(page.locator('#chain-detail-box')).toContainText('Apex Authority');
    await expect(page.locator('#chain-detail-box')).toContainText('Self-Signed');

    // Click Subordinate CA 1
    await page.locator('#chain-btn-sub1').click();
    await expect(page.locator('#chain-detail-box')).toContainText('Subordinate CA 1');

    // Click End-Entity Client
    await page.locator('#chain-btn-cl1').click();
    await expect(page.locator('#chain-detail-box')).toContainText('Leaf Certificate');
  });

  test('Key Escrow vs Archival simulator tests disaster, subpoena, and lost key scenarios', async ({ page }) => {
    await page.locator('button:has-text("Court Subpoena")').click();
    await expect(page.locator('#escrow-result-box')).toContainText('Retrieved via Key Escrow');

    await page.locator('button:has-text("Hardware Crash")').click();
    await expect(page.locator('#escrow-result-box')).toContainText('Restored via Key Archival');

    await page.locator('button:has-text("Lost Key (No Backup)")').click();
    await expect(page.locator('#escrow-result-box')).toContainText('PERMANENT DATA LOSS');
  });

  test('Top navigation contains Vuln Scanning & PenTesting link', async ({ page }) => {
    const vulnLink = page.locator('a[href="#vuln-pentesting"]').first();
    await expect(vulnLink).toBeVisible();
    await expect(vulnLink).toContainText('Vuln Scanning & PenTesting');
  });

  test('Vulnerability scanning section renders simulator and toggles credentialed scan', async ({ page }) => {
    const vulnSection = page.locator('#vuln-pentesting');
    await expect(vulnSection).toBeVisible();
    await expect(vulnSection).toContainText('Vulnerability Assessment, Fuzzing & Ethical Hacking');

    // Check Scanner Simulator controls
    await expect(page.locator('#btn-scan-non-cred')).toBeVisible();
    await expect(page.locator('#btn-scan-cred')).toBeVisible();
    await expect(page.locator('#vuln-scanner-console')).toBeVisible();

    // Click credentialed scan
    await page.locator('#btn-scan-cred').click();

    // Verify credentialed findings
    await expect(page.locator('#vuln-scanner-console')).toContainText('privilege escalation');
    await expect(page.locator('#vuln-scanner-console')).toContainText('CREDENTIALED SCAN');
  });

  test('Fuzzing lab simulates boundary edge cases and automated AFL fuzz batch', async ({ page }) => {
    const fuzzConsole = page.locator('#fuzz-lab-console');
    await expect(fuzzConsole).toBeVisible();

    // Test negative age
    await page.locator('button:has-text("Negative Age (-10)")').click();
    await expect(fuzzConsole).toContainText('BOUNDARY ERROR PREVENTED');

    // Test integer overflow
    await page.locator('button:has-text("Integer Overflow")').click();
    await expect(fuzzConsole).toContainText('CRASH PREVENTED');

    // Run automated AFL batch
    await page.locator('button:has-text("Run Fuzz Batch (1,000 Payloads)")').click();
    await expect(fuzzConsole).toContainText('100% RESILIENCE ACHIEVED');
  });

  test('Testing Models interactive selector toggles Black, Gray, and White box', async ({ page }) => {
    await page.locator('#btn-model-black').click();
    await expect(page.locator('#testing-model-detail')).toContainText('Black-Box Testing');
    await expect(page.locator('#testing-model-detail')).toContainText('Zero prior knowledge');

    await page.locator('#btn-model-white').click();
    await expect(page.locator('#testing-model-detail')).toContainText('White-Box Testing');
    await expect(page.locator('#testing-model-detail')).toContainText('Complete knowledge');
  });

  test('Penetration testing lifecycle stepper navigates through 7 stages', async ({ page }) => {
    const stepContent = page.locator('#pentest-step-content');
    await expect(stepContent).toBeVisible();

    // Check initial stage is Passive Recon
    await expect(stepContent).toContainText('Passive Recon');

    // Click Stage 2
    await page.locator('#btn-penstep-1').click();
    await expect(stepContent).toContainText('Active Recon');

    // Jump to Stage 6 (Clearing Tracks)
    await page.locator('#btn-penstep-5').click();
    await expect(stepContent).toContainText('Clearing Tracks');
    await expect(stepContent).toContainText('Colorado');
  });

  test('Top navigation contains Wireless Attacks and Password Attacks links', async ({ page }) => {
    const wirelessLink = page.locator('a[href="#wireless-threats"]').first();
    await expect(wirelessLink).toBeVisible();
    await expect(wirelessLink).toContainText('Wireless Attacks');

    const pwdLink = page.locator('a[href="#password-attacks"]').first();
    await expect(pwdLink).toBeVisible();
    await expect(pwdLink).toContainText('Password Attacks');
  });

  test('Wireless Threats section renders and interactive simulator advances steps', async ({ page }) => {
    const wirelessSec = page.locator('#wireless-threats');
    await expect(wirelessSec).toBeVisible();
    await expect(wirelessSec).toContainText('Wireless Threat Vectors & RF Exploits');
    await expect(wirelessSec).toContainText('Rogue Access Points');
    await expect(wirelessSec).toContainText('Evil Twin');
    await expect(wirelessSec).toContainText('Bluesnarfing');

    // Test simulator step progression
    const simConsole = page.locator('#wireless-sim-console');
    await expect(simConsole).toBeVisible();

    // Advance to Step 5: Test Access & Sniff
    await page.locator('#btn-wstep-5').click();
    await expect(simConsole).toContainText('HALLMARK OBSERVED');
    await expect(simConsole).toContainText('INTERNET PASSES, INTRANET FAILS');

    // Test War driving tabs
    const warDetail = page.locator('#war-tab-detail');
    await page.locator('#btn-war-fly').click();
    await expect(warDetail).toContainText('War Flying');
    await expect(warDetail).toContainText('drones');

    await page.locator('#btn-war-wigle').click();
    await expect(warDetail).toContainText('WiGLE.net');
    await expect(warDetail).toContainText('database');
  });

  test('Password & Hash Attacks section renders and interactive simulators function', async ({ page }) => {
    const pwdSec = page.locator('#password-attacks');
    await expect(pwdSec).toBeVisible();
    await expect(pwdSec).toContainText('Password Attacks & Cryptographic Collisions');
    await expect(pwdSec).toContainText('Online vs. Offline');
    await expect(pwdSec).toContainText('Password Spraying');
    await expect(pwdSec).toContainText('Birthday Paradox');
    await expect(pwdSec).toContainText('Credential Stuffing');

    // Test Credential Simulator
    const pwdConsole = page.locator('#pwd-sim-console');
    await expect(pwdConsole).toBeVisible();

    // Run Dictionary Attack (should trigger Account Lockout)
    await page.locator('#btn-pwd-dict').click();
    await expect(pwdConsole).toContainText('ACCOUNT LOCKED OUT');

    // Run Password Spraying (should evade Lockout)
    await page.locator('#btn-pwd-spray').click();
    await expect(pwdConsole).toContainText('STEALTH COMPROMISE: ZERO LOCKOUTS TRIGGERED');
    await expect(pwdConsole).toContainText('without tripping account lockout');

    // Test Rainbow Table Salt toggle
    const rainbowBox = page.locator('#rainbow-result-box');
    await page.locator('#btn-rainbow-salted').click();
    await expect(rainbowBox).toContainText('Rainbow Table Neutralized');

    // Test Birthday Paradox Slider
    const bdayBadge = page.locator('#bday-prob-badge');
    await expect(bdayBadge).toContainText('50.7%');
  });

  test('Knowledge quiz renders with 44 comprehensive questions', async ({ page }) => {
    const quizCount = page.locator('#quiz-progress-text');
    await expect(quizCount).toContainText('44');
  });
});


