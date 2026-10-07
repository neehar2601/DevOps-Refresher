const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file:///home/neehar/learning_devops/Linux/linux_index.html');
  const count = await page.locator('a[href*="linux_package_management.html"]').count();
  console.log("Count:", count);
  if(count > 0) {
    const isVisible = await page.locator('a[href*="linux_package_management.html"]').first().isVisible();
    console.log("Is visible:", isVisible);
  }
  await browser.close();
})();
