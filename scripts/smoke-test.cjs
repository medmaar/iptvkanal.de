// Requires the cloud environment's Playwright and Chromium installations.
// Start the static server first; SITE_URL optionally selects another server.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { chromium } = require('playwright');

(async () => {
  const base = process.env.SITE_URL || 'http://127.0.0.1:8000';
  const browser = await chromium.launch({ executablePath: '/usr/bin/chromium', args: ['--no-sandbox'] });
  try {
    const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
    const errors = [];
    const failures = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('response', response => {
      if (response.url().startsWith(base) && response.status() >= 400) failures.push(response.url());
    });
    // Fonts are optional. Verify the entire site works without outside requests.
    await page.route('https://**/*', route => route.abort());
    await page.goto(base);
    for (const asset of ['assets/main.js', 'assets/template.css']) {
      const version = crypto.createHash('sha256').update(fs.readFileSync(path.join(__dirname, '..', asset))).digest('hex').slice(0, 12);
      const attribute = asset.endsWith('.js') ? 'src' : 'href';
      assert.equal(await page.locator(`[${attribute}="${asset}?v=${version}"]`).count(), 1, `${asset} must use its current content hash to bypass older cached bundles`);
    }
    console.log('PASS current JavaScript and CSS cache keys match their contents');
    await page.emulateMedia({ reducedMotion: 'reduce' });
    assert.deepEqual(await page.locator('[data-review-platform]').evaluateAll(sections => sections.map(section => section.dataset.reviewPlatform)), ['trustpilot', 'whatsapp', 'google']);
    assert.equal(await page.locator('[data-placeholder="true"]').count(), 18);
    assert.equal(await page.locator('[data-review-id]').count(), 0);
    assert.equal(await page.locator('.review-toolbar').count(), 0);
    for (const [platform, perView, count] of [['trustpilot', 1, 3], ['whatsapp', 2, 6], ['google', 3, 9]]) {
      const section = page.locator(`[data-review-platform="${platform}"]`);
      const viewport = section.locator('[data-review-viewport]');
      await section.scrollIntoViewIfNeeded();
      assert.equal(await viewport.evaluate(element => Number(getComputedStyle(element).getPropertyValue('--per-view'))), perView);
      assert.equal(await section.locator('[data-review-card]').count(), count);
      assert.equal(await section.locator('[data-review-dots] button').count(), 3);
      assert.equal(await section.locator('[data-review-pause]').getAttribute('aria-pressed'), 'true');
      await section.locator('[data-review-next]').click();
      await page.waitForFunction(id => document.querySelector(`[data-review-platform="${id}"] [data-review-viewport]`).scrollLeft > 10, platform);
      assert.equal(await section.locator('[data-review-dots] button').nth(1).getAttribute('aria-current'), 'page');
      await section.locator('[data-review-dots] button').last().click();
      assert.equal(await section.locator('[data-review-dots] button').last().getAttribute('aria-current'), 'page');
      await viewport.press('Home');
      assert.equal(await section.locator('[data-review-dots] button').first().getAttribute('aria-current'), 'page');
      await section.locator('[data-review-prev]').click();
      assert.equal(await section.locator('[data-review-dots] button').last().getAttribute('aria-current'), 'page');
      await viewport.press('Home');
    }
    console.log('PASS separate Trustpilot/WhatsApp/Google layouts, labeled placeholders, arrows, dots, keyboard navigation, and reduced-motion pause');

    // Virtual time verifies real automatic advancement without a seven-second sleep.
    const autoPage = await browser.newPage({ viewport: { width: 1200, height: 500 } });
    await autoPage.clock.install();
    await autoPage.route('https://**/*', route => route.abort());
    await autoPage.goto(base);
    const autoplay = autoPage.locator('[data-review-platform="trustpilot"]');
    await autoplay.scrollIntoViewIfNeeded();
    await autoPage.mouse.move(0, 0);
    await autoPage.waitForFunction(() => document.querySelector('[data-review-platform="trustpilot"]').getBoundingClientRect().top < innerHeight);
    await autoPage.clock.runFor(7500);
    await autoPage.waitForFunction(() => document.querySelector('[data-review-platform="trustpilot"] [data-review-viewport]').scrollLeft > 10);
    await autoPage.waitForFunction(() => document.querySelector('[data-review-platform="trustpilot"] [data-review-dots] [aria-current="page"]').getAttribute('aria-label').endsWith('Seite 2'));
    await autoplay.locator('[data-review-pause]').click();
    assert.equal(await autoplay.locator('[data-review-pause]').getAttribute('aria-pressed'), 'true');
    const pausedPosition = await autoplay.locator('[data-review-dots] [aria-current="page"]').getAttribute('aria-label');
    await autoPage.mouse.click(5, 200);
    await autoPage.clock.runFor(15000);
    assert.equal(await autoplay.locator('[data-review-dots] [aria-current="page"]').getAttribute('aria-label'), pausedPosition);
    await autoplay.locator('[data-review-pause]').click();
    await autoPage.mouse.click(5, 200);
    await autoPage.clock.runFor(7500);
    await autoPage.waitForFunction(previous => document.querySelector('[data-review-platform="trustpilot"] [data-review-dots] [aria-current="page"]').getAttribute('aria-label') !== previous, pausedPosition);
    await autoPage.close();
    console.log('PASS automatic review sliding, explicit pause, and resume');

    assert.equal(await page.locator('.hero-slide').evaluate(element => getComputedStyle(element).backgroundImage.includes('hero-posters.webp')), true);
    assert.equal(await page.locator('.tv-hero-img').evaluate(element => getComputedStyle(element).backgroundImage.includes('photo-keeper.jpg')), true);
    assert.equal(await page.locator('.highlights .slide').count(), 6);
    await page.emulateMedia({ reducedMotion: 'reduce' });
    await page.locator('.slider-btn[data-dir="1"]').click();
    await page.waitForFunction(() => document.querySelector('.highlights .slider').scrollLeft > 10);
    await page.locator('.slider-btn[data-dir="-1"]').click();
    await page.waitForFunction(() => document.querySelector('.highlights .slider').scrollLeft < 2);
    for (const image of await page.locator('.vod img').all()) {
      assert.equal((await page.request.get(new URL(await image.getAttribute('src'), base).href)).status(), 200);
    }
    console.log('PASS original background images, highlights controls, and VOD posters');

    const expected = [[9, 29, 39, 49], [18, 50, 69, 89], [27, 75, 105, 135], [36, 99, 140, 180], [45, 120, 175, 225]];
    for (let devices = 1; devices <= 5; devices++) {
      await page.locator(`[data-devices="${devices}"]`).click();
      assert.deepEqual(await page.locator('.plan-price b').allTextContents(), expected[devices - 1].map(String));
      const hrefs = await page.locator('.plan-btn').evaluateAll(links => links.map(link => link.getAttribute('href')));
      hrefs.forEach((href, index) => {
        assert.ok(href.startsWith('mailto:info@iptvkanal.de?subject='));
        assert.ok(decodeURIComponent(href).includes(`Geräte: ${devices}`));
        assert.ok(decodeURIComponent(href).includes(`Preis: ${expected[devices - 1][index]} €`));
      });
    }
    await page.locator('[data-devices="5"]').press('ArrowRight');
    assert.equal(await page.locator('[data-devices="1"]').getAttribute('aria-pressed'), 'true');
    await page.locator('[data-devices="1"]').press('ArrowLeft');
    assert.equal(await page.locator('[data-devices="5"]').getAttribute('aria-pressed'), 'true');
    console.log('PASS all 20 prices, order details, and keyboard device selection');

    for (const width of [1440, 768, 390, 320]) {
      await page.setViewportSize({ width, height: 844 });
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, `Overflow at ${width}px`);
      if (width <= 600) {
        for (const [platform, count] of [['trustpilot', 3], ['whatsapp', 6], ['google', 9]]) {
          await page.waitForFunction(({ platform, count }) => {
            const section = document.querySelector(`[data-review-platform="${platform}"]`);
            return Number(getComputedStyle(section.querySelector('[data-review-viewport]')).getPropertyValue('--per-view')) === 1
              && section.querySelectorAll('[data-review-dots] button').length === count;
          }, { platform, count });
        }
      }
    }
    await page.locator('.menu-btn').click();
    assert.equal(await page.locator('.menu-btn').getAttribute('aria-expanded'), 'true');
    await page.keyboard.press('Escape');
    assert.equal(await page.locator('.menu-btn').getAttribute('aria-expanded'), 'false');
    await page.locator('.menu-btn').click();
    await page.locator('#nav-links a').first().click();
    assert.equal(await page.locator('.menu-btn').getAttribute('aria-expanded'), 'false');
    assert.equal(await page.locator('body').evaluate(body => body.classList.contains('no-scroll')), false);
    await page.locator('.faq summary').first().click();
    assert.equal(await page.locator('.faq details').first().getAttribute('open'), '');
    console.log('PASS mobile navigation, FAQ, and layouts from 320px to 1440px');

    const badAnchors = await page.locator('a[href^="#"]').evaluateAll(links => links.filter(link => !document.getElementById(link.hash.slice(1))).map(link => link.hash));
    assert.deepEqual(badAnchors, []);
    for (const target of ['/impressum.html', '/datenschutz.html', '/404.html', '/assets/main.js', '/assets/template.css', '/assets/reference/style.css', '/assets/img/photo-keeper.jpg', '/assets/review-platforms.json', '/sitemap.xml', '/robots.txt']) {
      assert.equal((await page.request.get(base + target)).status(), 200, target);
    }
    const noJS = await browser.newContext({ javaScriptEnabled: false });
    const plain = await noJS.newPage();
    await plain.route('https://**/*', route => route.abort());
    await plain.goto(base);
    assert.equal(await plain.locator('[data-review-card]').count(), 18);
    assert.equal(await plain.locator('[data-review-controls]:visible').count(), 0);
    const plainRail = plain.locator('[data-review-viewport]').first();
    await plainRail.evaluate(element => { element.scrollLeft = element.scrollWidth; });
    assert.ok(await plainRail.evaluate(element => element.scrollLeft > 0));
    assert.equal(await plain.locator('.plan-btn[href^="mailto:"]').count(), 4);
    await noJS.close();
    assert.deepEqual(errors, []);
    assert.deepEqual(failures, []);
    console.log('PASS local routes, anchors, no-JavaScript review scrolling, and no runtime errors');
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
