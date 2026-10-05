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
    await page.locator('button:has-text("Tamper with Payload")').click();
    await expect(page.locator('#sig-result-box')).toContainText('SIGNATURE FAILED: Integrity Breach Detected');

    // Reset payload
    await page.locator('button:has-text("Reset")').click();
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
    await page.locator('button:has-text("Next")').first().click();
    await expect(page.locator('#https-step-counter')).toContainText('Step 2 of 6');
  });

  test('PKI Chain of Trust interactive visualizer displays node details on click', async ({ page }) => {
    const chainSection = page.locator('#cert-chain-escrow');
    await expect(chainSection).toBeVisible();
    await expect(chainSection).toContainText('PKI Chain of Trust, Certificate Lifecycle & Key Escrow');

    // Click Root CA
    await page.locator('#chain-btn-root').click();
    await expect(page.locator('#chain-detail-box')).toContainText('Apex Root CA');
    await expect(page.locator('#chain-detail-box')).toContainText('Self-signed');

    // Click Subordinate CA 1
    await page.locator('#chain-btn-sub1').click();
    await expect(page.locator('#chain-detail-box')).toContainText('Intermediate / Subordinate CA 1');

    // Click End-Entity Client
    await page.locator('#chain-btn-cl1').click();
    await expect(page.locator('#chain-detail-box')).toContainText('End-Entity / Leaf Certificate');
  });

  test('Key Escrow vs Archival simulator tests disaster, subpoena, and lost key scenarios', async ({ page }) => {
    await page.locator('button:has-text("Legal Discovery Subpoena")').click();
    await expect(page.locator('#escrow-result-box')).toContainText('Retrieved via Key Escrow');

    await page.locator('button:has-text("Storage Crash Disaster")').click();
    await expect(page.locator('#escrow-result-box')).toContainText('Restored via Key Archival');

    await page.locator('button:has-text("No Backup Disaster")').click();
    await expect(page.locator('#escrow-result-box')).toContainText('PERMANENT DATA LOSS');
  });

  test('Knowledge quiz renders with 30 comprehensive questions', async ({ page }) => {
    const quizCount = page.locator('#quiz-progress-text');
    await expect(quizCount).toContainText('30');
  });
});
