// Requires the cloud environment's Playwright and Chromium installations.
// Start the static server first; SITE_URL optionally selects another server.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');

(async () => {
  const base = process.env.SITE_URL || 'http://127.0.0.1:8000';
  const data = JSON.parse(fs.readFileSync(path.join(__dirname, '../assets/reviews.json'), 'utf8'));
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
    const counts = {};
    for (const review of data.reviews) counts[review.group] = (counts[review.group] || 0) + 1;
    assert.deepEqual(counts, { trustpilot: 15, whatsapp: 20, google: 20, metadata: 8 });
    assert.equal(new Set(data.reviews.map(review => review.id)).size, 63);
    assert.equal(await page.locator('[data-review-id]').count(), 63);
    for (const review of data.reviews) {
      const card = page.locator(`[data-review-id="${review.id}"]`);
      assert.equal(await card.locator('blockquote p').textContent(), review.text);
      assert.equal(await card.locator('.review-author strong').textContent(), review.author);
      assert.equal(await card.locator('.review-author a').getAttribute('href'), data.source_url);
    }
    console.log('PASS all 63 review records, original wording, authors, and source links');
    assert.equal(await page.locator('[data-review-id]:visible').count(), 6);
    while (await page.locator('#reviews-more').isVisible()) await page.locator('#reviews-more').click();
    assert.equal(await page.locator('[data-review-id]:visible').count(), 63);
    for (const [group, count] of Object.entries(counts)) {
      await page.locator(`[data-review-filter="${group}"]`).click();
      assert.equal(await page.locator('[data-review-id]:visible').count(), 6);
      while (await page.locator('#reviews-more').isVisible()) await page.locator('#reviews-more').click();
      assert.equal(await page.locator('[data-review-id]:visible').count(), count);
    }
    await page.locator('[data-review-filter="all"]').click();
    await page.locator('#review-search').fill('Thomas R.');
    assert.equal(await page.locator('[data-review-id]:visible').count(), 2);
    await page.locator('#review-search').fill('no-match-123456789');
    assert.equal(await page.locator('[data-review-id]:visible').count(), 0);
    assert.match(await page.locator('#review-status').textContent(), /Keine passenden/);
    assert.equal(await page.locator('#reviews-more').isVisible(), false);
    await page.locator('#review-search').fill('');
    console.log('PASS review filtering, search, empty state, and loading every record');

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
    for (const target of ['/impressum.html', '/datenschutz.html', '/404.html', '/assets/main.js', '/assets/template.css', '/assets/reference/style.css', '/assets/img/photo-keeper.jpg', '/assets/reviews.json', '/sitemap.xml', '/robots.txt']) {
      assert.equal((await page.request.get(base + target)).status(), 200, target);
    }
    const noJS = await browser.newContext({ javaScriptEnabled: false });
    const plain = await noJS.newPage();
    await plain.route('https://**/*', route => route.abort());
    await plain.goto(base);
    assert.equal(await plain.locator('[data-review-id]:visible').count(), 63);
    assert.equal(await plain.locator('.plan-btn[href^="mailto:"]').count(), 4);
    assert.equal(await plain.locator('.review-toolbar').isVisible(), false);
    await noJS.close();
    assert.deepEqual(errors, []);
    assert.deepEqual(failures, []);
    console.log('PASS local routes, anchors, no-JavaScript archive, and no runtime errors');
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
