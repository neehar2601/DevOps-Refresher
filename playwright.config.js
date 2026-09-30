// @ts-check
const { defineConfig, devices } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests',
  timeout: 60_000,          // 60s per test (S3 can be slow on cold start)
  expect: { timeout: 15_000 },
  fullyParallel: false,      // Run sequentially – shared S3 env, no isolation needed
  retries: 1,                // One automatic retry on flaky network
  reporter: [
    ['list'],
    ['html', { outputFolder: 'playwright-report', open: 'never' }],
    ['junit', { outputFile: 'test-results/results.xml' }],
  ],

  use: {
    baseURL: process.env.BASE_URL || 'https://devops-learner.s3.us-east-2.amazonaws.com',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    trace: 'on-first-retry',
    headless: true,
  },

  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],
});
