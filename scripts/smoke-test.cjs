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
      assert.equal(await wordmark.getAttribute('alt'), 'IPTV Kanal');
    }
    for (const section of ['#bewertungen', '#vod']) {
      assert.equal(await page.locator(section).evaluate(element => getComputedStyle(element).backgroundColor), await page.locator('body').evaluate(element => getComputedStyle(element).backgroundColor));
      assert.equal(await page.locator(section).evaluate(element => getComputedStyle(element).backgroundImage), await page.locator('body').evaluate(element => getComputedStyle(element).backgroundImage));
    }
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

    // Check actual movement, not just a counter changing before scrolling starts.
    for (const mobile of [false, true]) {
      const autoPage = await browser.newPage({ viewport: { width: mobile ? 390 : 1200, height: 700 }, isMobile: mobile, hasTouch: mobile });
      await autoPage.clock.install();
      await autoPage.route('**/*', route => new URL(route.request().url()).origin === new URL(base).origin ? route.continue() : route.abort());
      await autoPage.goto(base);
      await autoPage.evaluate(() => document.fonts.ready);
      for (const platform of ['trustpilot', 'whatsapp', 'google']) {
        const section = autoPage.locator(`[data-review-platform="${platform}"]`);
        const rail = section.locator('[data-review-viewport]');
        await rail.scrollIntoViewIfNeeded();
        if (!mobile) await rail.hover();
        // Let the browser report intersection before advancing its virtual clock.
        await autoPage.waitForFunction(id => document.querySelector(`[data-review-platform="${id}"] [data-review-viewport]`).scrollLeft > 1, platform, { timeout: 3000 });
        const start = await rail.evaluate(element => element.scrollLeft);
        await autoPage.clock.runFor(1200);
        assert.ok(await rail.evaluate((element, start) => element.scrollLeft > start + 15, start), `${platform} must visibly move within 1.2 seconds (${mobile ? 'mobile' : 'desktop'})`);

        if (!mobile) {
          const beforePageScroll = await rail.evaluate(element => element.scrollLeft);
          await autoPage.mouse.wheel(0, 30);
          await autoPage.clock.runFor(1200);
          assert.ok(await rail.evaluate((element, previous) => element.scrollLeft > previous + 15, beforePageScroll), 'Vertical page scrolling must not stop the reviews');
        }
        await section.locator('[data-review-next]').click();
        await autoPage.waitForFunction(id => {
          const rail = document.querySelector(`[data-review-platform="${id}"] [data-review-viewport]`);
          const cards = rail.querySelectorAll('[data-review-card]');
          const perView = Number(getComputedStyle(rail).getPropertyValue('--per-view'));
          return Math.abs(rail.scrollLeft - (cards[perView].offsetLeft - cards[0].offsetLeft)) < 2;
        }, platform);
        const clickedPosition = await rail.evaluate(element => element.scrollLeft);
        await autoPage.clock.runFor(4200);
        assert.ok(await rail.evaluate((element, previous) => element.scrollLeft > previous + 15, clickedPosition), 'An arrow click must not leave autoplay stopped');

        await rail.press('Home');
        await autoPage.waitForFunction(id => document.querySelector(`[data-review-platform="${id}"] [data-review-viewport]`).scrollLeft < 2, platform);
        await autoPage.clock.runFor(2000);
        assert.ok(await rail.evaluate(element => element.scrollLeft < 2), 'Allow a short break after keyboard input');
        await autoPage.clock.runFor(2200);
        assert.ok(await rail.evaluate(element => element.scrollLeft > 15), 'Autoplay must resume even if keyboard focus remains');
        if (mobile) {
          await rail.tap();
          const tappedPosition = await rail.evaluate(element => element.scrollLeft);
          await autoPage.clock.runFor(4200);
          assert.ok(await rail.evaluate((element, previous) => element.scrollLeft > previous + 15, tappedPosition), 'A tap must not leave autoplay stopped');
        }

        // Put the rail just before the loop boundary and watch it join the first card.
        await rail.evaluate(element => {
          element.scrollLeft = element.querySelector('[data-review-clone]').offsetLeft - element.querySelector('[data-review-card]').offsetLeft - 8;
          element.dispatchEvent(new WheelEvent('wheel', { deltaX: 10 }));
        });
        await autoPage.clock.runFor(4200);
        assert.ok(await rail.evaluate(element => element.scrollLeft < 80), 'The last review must wrap seamlessly to the first');

        await rail.press('Home');
        await rail.evaluate(element => element.blur());
        await autoPage.emulateMedia({ reducedMotion: 'reduce' });
        await autoPage.clock.runFor(6500);
        await autoPage.waitForFunction(id => document.querySelector(`[data-review-platform="${id}"] [data-review-current]`).textContent !== '01', platform);
        await autoPage.emulateMedia({ reducedMotion: 'no-preference' });
      }
      await autoPage.close();
    }
    console.log('PASS continuous movement in all three rails on desktop/mobile, automatic recovery after controls/taps/keyboard input, seamless loops and reduced-motion page changes');

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
      assert.equal(await page.locator('[data-review-card] .review-country-flag').count(), 60);
      assert.equal(await page.locator('[data-review-card] .review-country-flag').evaluateAll(images => images.every(image => image.complete && image.naturalWidth > 0 && image.getBoundingClientRect().width === 20 && image.getBoundingClientRect().height === 12)), true, `Flag graphics must load and retain their size at ${width}px`);
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
    for (const target of ['/impressum.html', '/datenschutz.html', '/404.html', '/assets/main.js', '/assets/template.css', '/assets/base.css', '/assets/brand/iptvkanal-supplied-logo.webp', '/assets/fonts/inter-latin-variable.woff2', '/assets/fonts/sora-latin-variable.woff2', '/assets/img/hero-carnival.webp', '/assets/review-platforms.json', '/sitemap.xml', '/robots.txt']) {
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
