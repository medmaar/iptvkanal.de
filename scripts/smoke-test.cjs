// Requires the cloud environment's Playwright and Chromium installations.
// Start the static server first; SITE_URL optionally selects another server.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { chromium } = require('playwright');

(async () => {
  const base = process.env.SITE_URL || 'http://127.0.0.1:8000';
  const supplied = JSON.parse(fs.readFileSync(path.join(__dirname, '../assets/review-platforms.json'), 'utf8'));
  const browser = await chromium.launch({ executablePath: '/usr/bin/chromium', args: ['--no-sandbox'] });
  try {
    const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
    const errors = [];
    const failures = [];
    const externalRequests = [];
    page.on('request', request => {
      if (new URL(request.url()).origin !== new URL(base).origin) externalRequests.push(request.url());
    });
    page.on('pageerror', error => errors.push(error.message));
    page.on('response', response => {
      if (response.url().startsWith(base) && response.status() >= 400) failures.push(response.url());
    });
    // All application assets, including fonts, must load from the site itself.
    await page.route('**/*', route => new URL(route.request().url()).origin === new URL(base).origin ? route.continue() : route.abort());
    await page.goto(base);
    await page.evaluate(() => document.fonts.ready);
    assert.equal(await page.evaluate(() => document.fonts.check('16px Inter') && document.fonts.check('16px Sora')), true);
    for (const asset of ['assets/main.js', 'assets/base.css', 'assets/template.css']) {
      const version = crypto.createHash('sha256').update(fs.readFileSync(path.join(__dirname, '..', asset))).digest('hex').slice(0, 12);
      const attribute = asset.endsWith('.js') ? 'src' : 'href';
      assert.equal(await page.locator(`[${attribute}="${asset}?v=${version}"]`).count(), 1, `${asset} must use its current content hash to bypass older cached bundles`);
    }
    console.log('PASS current JavaScript and CSS cache keys match their contents');
    assert.equal(await page.locator('.brand-wordmark').count(), 2);
    for (const wordmark of await page.locator('.brand-wordmark').all()) {
      await wordmark.evaluate(image => image.decode());
      assert.equal(await wordmark.getAttribute('alt'), 'IPTV Kanal Premium');
    }
    assert.equal(await page.locator('#bewertungen').evaluate(element => getComputedStyle(element).backgroundColor), await page.locator('body').evaluate(element => getComputedStyle(element).backgroundColor));
    await page.emulateMedia({ reducedMotion: 'reduce' });
    assert.deepEqual(await page.locator('[data-review-platform]').evaluateAll(sections => sections.map(section => section.dataset.reviewPlatform)), ['trustpilot', 'whatsapp', 'google']);
    assert.equal(await page.locator('[data-placeholder="true"]').count(), 0);
    assert.equal(await page.locator('[data-review-card]').count(), 60);
    assert.equal(await page.locator('[data-review-pause]').count(), 0);
    assert.equal(await page.locator('.reviews-pending').count(), 0);
    assert.equal(await page.locator('[data-review-id]').count(), 0);
    assert.equal(await page.locator('.review-toolbar').count(), 0);
    for (const [platform, perView, count] of [['trustpilot', 1, 20], ['whatsapp', 2, 20], ['google', 3, 20]]) {
      const section = page.locator(`[data-review-platform="${platform}"]`);
      const viewport = section.locator('[data-review-viewport]');
      await section.scrollIntoViewIfNeeded();
      assert.equal(await viewport.evaluate(element => Number(getComputedStyle(element).getPropertyValue('--per-view'))), perView);
      assert.equal(await section.locator('[data-review-card]').count(), count);
      const pages = String(Math.ceil(count / perView)).padStart(2, '0');
      assert.equal(await section.locator('[data-review-total]').textContent(), pages);
      assert.equal(await section.locator('[data-review-controls] button').count(), 2);
      assert.equal(await section.locator('[data-review-dots]').count(), 0);
      const reviews = supplied.platforms.find(item => item.id === platform).reviews;
      for (let index = 0; index < reviews.length; index++) {
        const card = section.locator('[data-review-card]').nth(index);
        assert.equal(await card.locator('blockquote p').textContent(), reviews[index].text);
        const author = reviews[index].author.replace(/[\u{1F1E6}-\u{1F1FF}]{2}/gu, '').trim();
        assert.equal((await card.locator('.platform-review-author').textContent()).trim(), author);
        const flag = card.locator('.review-country-flag');
        assert.equal(await flag.getAttribute('src'), 'assets/flags/de.svg');
        assert.equal(await flag.evaluate(image => image.complete && image.naturalWidth > 0), true);
        if (reviews[index].title) assert.equal(await card.locator('h4').textContent(), reviews[index].title);
        if (reviews[index].rating) assert.equal(await card.locator('.platform-review-stars').textContent(), '★'.repeat(reviews[index].rating));
      }
      await section.locator('[data-review-next]').click();
      await page.waitForFunction(id => document.querySelector(`[data-review-platform="${id}"] [data-review-viewport]`).scrollLeft > 10, platform);
      assert.equal(await section.locator('[data-review-current]').textContent(), '02');
      await viewport.press('End');
      assert.equal(await section.locator('[data-review-current]').textContent(), pages);
      await viewport.press('Home');
      assert.equal(await section.locator('[data-review-current]').textContent(), '01');
      await section.locator('[data-review-prev]').click();
      assert.equal(await section.locator('[data-review-current]').textContent(), pages);
      await viewport.press('Home');
    }
    console.log('PASS all 60 supplied reviews with original text, names and ratings; separate layouts, compact counters, arrows and keyboard navigation; no pause buttons');

    // Virtual time verifies real automatic advancement without a seven-second sleep.
    const autoPage = await browser.newPage({ viewport: { width: 1200, height: 500 } });
    await autoPage.clock.install();
    await autoPage.route('**/*', route => new URL(route.request().url()).origin === new URL(base).origin ? route.continue() : route.abort());
    await autoPage.goto(base);
    const autoplay = autoPage.locator('[data-review-platform="trustpilot"]');
    await autoplay.scrollIntoViewIfNeeded();
    await autoPage.mouse.move(0, 0);
    await autoPage.waitForFunction(() => document.querySelector('[data-review-platform="trustpilot"]').getBoundingClientRect().top < innerHeight);
    await autoPage.clock.runFor(7500);
    await autoPage.waitForFunction(() => document.querySelector('[data-review-platform="trustpilot"] [data-review-viewport]').scrollLeft > 10);
    await autoPage.waitForFunction(() => document.querySelector('[data-review-platform="trustpilot"] [data-review-current]').textContent === '02');
    await autoplay.hover();
    const hoveredPosition = await autoplay.locator('[data-review-current]').textContent();
    await autoPage.clock.runFor(15000);
    assert.equal(await autoplay.locator('[data-review-current]').textContent(), hoveredPosition);
    await autoPage.mouse.move(0, 0);
    await autoPage.clock.runFor(7500);
    await autoPage.waitForFunction(previous => document.querySelector('[data-review-platform="trustpilot"] [data-review-current]').textContent !== previous, hoveredPosition);
    await autoplay.locator('[data-review-viewport]').focus();
    const focusedPosition = await autoplay.locator('[data-review-current]').textContent();
    await autoPage.clock.runFor(15000);
    assert.equal(await autoplay.locator('[data-review-current]').textContent(), focusedPosition);
    await autoplay.locator('[data-review-viewport]').evaluate(element => element.blur());
    await autoPage.emulateMedia({ reducedMotion: 'reduce' });
    await autoPage.clock.runFor(15000);
    assert.equal(await autoplay.locator('[data-review-current]').textContent(), focusedPosition);
    await autoPage.close();
    console.log('PASS automatic review sliding, hover/focus hold, and reduced-motion preference without pause controls');

    assert.equal(await page.locator('.hero-backdrop').evaluate(element => getComputedStyle(element).backgroundImage.includes('hero-carnival.webp')), true);
    assert.equal(await page.locator('body').evaluate(element => getComputedStyle(element).colorScheme), 'dark');
    assert.equal(await page.locator('[data-review-platform="trustpilot"] .platform-review-stars').first().evaluate(element => getComputedStyle(element).color), 'rgb(0, 182, 122)');
    assert.equal(await page.locator('[data-review-platform="google"] .platform-review-stars').first().evaluate(element => getComputedStyle(element).color), 'rgb(251, 188, 4)');
    assert.equal(await page.locator('.highlights .slide').count(), 6);
    await page.emulateMedia({ reducedMotion: 'reduce' });
    await page.locator('.slider-btn[data-dir="1"]').click();
    await page.waitForFunction(() => document.querySelector('.highlights .slider').scrollLeft > 10);
    await page.locator('.slider-btn[data-dir="-1"]').click();
    await page.waitForFunction(() => document.querySelector('.highlights .slider').scrollLeft < 2);
    for (const image of await page.locator('.vod img').all()) {
      assert.equal((await page.request.get(new URL(await image.getAttribute('src'), base).href)).status(), 200);
    }
    console.log('PASS local hero backdrop, dark theme, platform star colors, highlights controls, and VOD posters');

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

    await page.locator('#preise').evaluate(section => scrollTo(0, section.getBoundingClientRect().top + scrollY));
    await page.waitForFunction(() => document.querySelector('#nav-links a[href="#preise"]').getAttribute('aria-current') === 'location');
    await page.locator('#bewertungen').evaluate(section => scrollTo(0, section.getBoundingClientRect().top + scrollY));
    await page.waitForFunction(() => document.querySelector('#nav-links a[href="#bewertungen"]').getAttribute('aria-current') === 'location');
    assert.equal(await page.locator('#nav-links [aria-current="location"]').count(), 1);
    console.log('PASS navigation follows the visible section');

    for (const width of [1920, 1440, 1080, 900, 768, 640, 390, 320]) {
      await page.setViewportSize({ width, height: 844 });
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, `Overflow at ${width}px`);
      assert.equal(await page.locator('.review-country-flag').count(), 60);
      assert.equal(await page.locator('.review-country-flag').evaluateAll(images => images.every(image => image.complete && image.naturalWidth > 0 && image.getBoundingClientRect().width === 20 && image.getBoundingClientRect().height === 12)), true, `Flag graphics must load and retain their size at ${width}px`);
      if (width <= 600) {
        assert.equal(await page.locator('.nav-cta .btn-primary').isVisible(), true, `Header action must stay visible at ${width}px`);
        assert.equal(await page.locator('[data-devices]').evaluateAll(buttons => buttons.every(button => button.getBoundingClientRect().height >= 44)), true, `Device controls must have usable touch targets at ${width}px`);
        const photoLayout = await page.evaluate(() => {
          const photo = document.querySelector('.hero-backdrop').getBoundingClientRect();
          const offer = document.querySelector('.hero-offer').getBoundingClientRect();
          return { height: photo.height, ratio: photo.width / photo.height, unobstructed: offer.top >= photo.bottom - 2 };
        });
        assert.ok(photoLayout.height > 150 && Math.abs(photoLayout.ratio - 16 / 9) < .03, `Hero photo must retain its full landscape composition at ${width}px`);
        assert.equal(photoLayout.unobstructed, true, `Price offer must not cover the mobile hero photo at ${width}px`);
        for (const [platform, count] of [['trustpilot', 20], ['whatsapp', 20], ['google', 20]]) {
          await page.waitForFunction(({ platform, count }) => {
            const section = document.querySelector(`[data-review-platform="${platform}"]`);
            return Number(getComputedStyle(section.querySelector('[data-review-viewport]')).getPropertyValue('--per-view')) === 1
              && Number(section.querySelector('[data-review-total]').textContent) === count;
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
    console.log('PASS mobile navigation, FAQ, visible header action, touch targets, and layouts from 320px to 1920px');

    const badAnchors = await page.locator('a[href^="#"]').evaluateAll(links => links.filter(link => !document.getElementById(link.hash.slice(1))).map(link => link.hash));
    assert.deepEqual(badAnchors, []);
    for (const target of ['/impressum.html', '/datenschutz.html', '/404.html', '/assets/main.js', '/assets/template.css', '/assets/base.css', '/assets/brand/iptvkanal-logo.webp', '/assets/fonts/inter-latin-variable.woff2', '/assets/fonts/sora-latin-variable.woff2', '/assets/img/hero-carnival.webp', '/assets/review-platforms.json', '/sitemap.xml', '/robots.txt']) {
      assert.equal((await page.request.get(base + target)).status(), 200, target);
    }
    for (const target of ['/impressum.html', '/datenschutz.html', '/404.html']) {
      await page.goto(base + target);
      await page.evaluate(() => document.fonts.ready);
      for (const wordmark of await page.locator('.brand-wordmark').all()) await wordmark.evaluate(image => image.decode());
    }
    assert.deepEqual(externalRequests, [], 'Pages must not request externally hosted assets');
    console.log('PASS all pages and fonts load locally with no external asset requests');
    const noJS = await browser.newContext({ javaScriptEnabled: false });
    const plain = await noJS.newPage();
    await plain.route('**/*', route => new URL(route.request().url()).origin === new URL(base).origin ? route.continue() : route.abort());
    await plain.goto(base);
    assert.equal(await plain.locator('[data-review-card]').count(), 60);
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
