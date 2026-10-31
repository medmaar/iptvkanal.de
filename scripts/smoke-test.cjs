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
      if (new URL(request.url()).origin !== new URL(base).origin && request.url() !== 'https://api.emailjs.com/api/v1.0/email/send') externalRequests.push(request.url());
    });
    page.on('pageerror', error => errors.push(error.message));
    page.on('response', response => {
      if (response.url().startsWith(base) && response.status() >= 400 && !response.url().endsWith('/api/trial')) failures.push(response.url());
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
    // The logo is a text-only wordmark: one bold word with a lighter word attached.
    assert.equal(await page.locator('.wordmark').count(), 2);
    assert.equal(await page.locator('.logo img').count(), 0);
    for (const wordmark of await page.locator('.wordmark').all()) {
      assert.equal(await wordmark.locator('b').textContent(), 'IPTV');
      assert.equal(await wordmark.locator('b').evaluate(element => getComputedStyle(element).fontWeight), '700');
      assert.equal(await wordmark.locator('span').evaluate(element => getComputedStyle(element).fontWeight), '300');
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
      const status = () => section.locator('[data-review-position]').textContent();
      assert.equal(await section.locator('[data-review-controls] button').count(), 0);
      assert.equal(await section.locator('[data-review-total], [data-review-current]').count(), 0);
      assert.equal(await section.locator('[data-review-dots] .review-dot').count(), 9);
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
      await viewport.press('Home');
      await viewport.press('ArrowRight');
      assert.equal(await status(), `Bewertung 2 von ${count}`);
      await viewport.press('End');
      assert.equal(await status(), `Bewertung ${count} von ${count}`);
      await viewport.press('ArrowRight');
      assert.equal(await status(), `Bewertung 1 von ${count}`);
      await viewport.press('ArrowLeft');
      assert.equal(await status(), `Bewertung ${count} von ${count}`);
      await viewport.press('Home');
    }
    console.log('PASS all 60 supplied reviews with original text, names and ratings; separate layouts, fading endless dots and keyboard navigation; no pause buttons');

    // Measure both the stationary reading time and the actual one-review movement.
    for (const mobile of [false, true]) {
      const autoPage = await browser.newPage({ viewport: { width: mobile ? 390 : 1200, height: 700 }, isMobile: mobile, hasTouch: mobile });
      await autoPage.clock.install();
      await autoPage.route('**/*', route => new URL(route.request().url()).origin === new URL(base).origin ? route.continue() : route.abort());
      await autoPage.goto(base);
      await autoPage.evaluate(() => document.fonts.ready);
      for (const [platform, delay] of [['trustpilot', 1900], ['whatsapp', 2300], ['google', 2900]]) {
        const section = autoPage.locator(`[data-review-platform="${platform}"]`);
        const rail = section.locator('[data-review-viewport]');
        await rail.scrollIntoViewIfNeeded();
        if (mobile) await rail.tap();
        else await rail.hover();
        const position = index => rail.evaluate((element, index) => {
          const cards = element.querySelectorAll('[data-review-card]');
          return cards[index].offsetLeft - element.firstElementChild.offsetLeft;
        }, index);
        const at = async index => assert.ok(Math.abs(await rail.evaluate(element => element.scrollLeft) - await position(index)) < 2, `${platform} must show review ${index + 1} (${mobile ? 'mobile' : 'desktop'})`);
        const home = async () => {
          await rail.press('Home');
          await autoPage.clock.runFor(600);
          await at(0);
          await rail.press('Home');
        };
        await home();
        await autoPage.clock.runFor(delay - 150);
        await at(0);
        await autoPage.clock.runFor(850);
        await at(1);
        assert.equal(await section.locator('[data-review-position]').textContent(), 'Bewertung 2 von 20');
        // The second review also gets a full hold after its transition finishes.
        await autoPage.clock.runFor(delay - 250);
        await at(1);
        await autoPage.clock.runFor(850);
        await at(2);

        await rail.press('ArrowRight');
        await autoPage.clock.runFor(600);
        await at(3);
        await autoPage.clock.runFor(delay - 200);
        await at(3);
        await autoPage.clock.runFor(900);
        await at(4);
        if (mobile) {
          await rail.tap();
          await autoPage.clock.runFor(delay - 150);
          await at(4);
          await autoPage.clock.runFor(850);
          await at(5);
        } else {
          await home();
          await autoPage.clock.runFor(delay - 150);
          await autoPage.mouse.wheel(0, 30);
          await autoPage.clock.runFor(850);
          await at(1);
        }

        await rail.press('End');
        await autoPage.clock.runFor(600);
        await at(19);
        await rail.press('End');
        await autoPage.clock.runFor(delay - 150);
        await at(19);
        await autoPage.clock.runFor(350);
        assert.ok(await rail.evaluate((element, last) => element.scrollLeft > last + 2, await position(19)), 'The final review must slide forward into the loop');
        await autoPage.clock.runFor(500);
        await at(0);
        assert.equal(await section.locator('[data-review-position]').textContent(), 'Bewertung 1 von 20');
        // Going back from the first review slides left into the last one, with no jump across the rail.
        await rail.press('ArrowLeft');
        await autoPage.clock.runFor(250);
        assert.ok(await rail.evaluate((element, first) => element.scrollLeft < first - 2, await position(0)), 'The first review must slide backward into the loop');
        await autoPage.clock.runFor(400);
        await at(19);
        await rail.press('Home');
        await autoPage.clock.runFor(600);

        await autoPage.emulateMedia({ reducedMotion: 'reduce' });
        await rail.press('Home');
        await autoPage.clock.runFor(delay - 150);
        await at(0);
        await autoPage.clock.runFor(200);
        await at(1);
        await autoPage.emulateMedia({ reducedMotion: 'no-preference' });
      }
      await autoPage.close();
    }
    console.log('PASS full 1.9s/2.3s/2.9s holds, one-review slides, manual-control recovery, forward loops and matching reduced-motion timing on desktop/mobile');

    assert.equal(await page.locator('.hero-backdrop').evaluate(element => getComputedStyle(element).backgroundImage.includes('hero-carnival.webp')), true);
    assert.equal(await page.locator('body').evaluate(element => getComputedStyle(element).colorScheme), 'dark');
    assert.equal(await page.locator('.hero-offer').getAttribute('href'), '/bestellen/1-jahr/?devices=1');
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
      for (const months of [1, 3, 6, 12]) {
        const choice = new URL(await page.locator(`.plan[data-months="${months}"] [data-plan-link]`).getAttribute('href'), base);
        const slug = { 1: '1-monat', 3: '3-monate', 6: '6-monate', 12: '1-jahr' }[months];
        assert.equal(choice.pathname, '/bestellen/' + slug + '/');
        assert.equal(choice.searchParams.get('devices'), String(devices));
      }
    }
    await page.locator('[data-devices="5"]').press('ArrowRight');
    assert.equal(await page.locator('[data-devices="1"]').getAttribute('aria-pressed'), 'true');
    await page.locator('[data-devices="1"]').press('ArrowLeft');
    assert.equal(await page.locator('[data-devices="5"]').getAttribute('aria-pressed'), 'true');
    console.log('PASS all 20 prices, order details, and keyboard device selection');

    assert.equal(await page.locator('#nav-links a').filter({ hasText: /^Preise$/ }).first().getAttribute('href'), '/preise/');
    await page.locator('#bewertungen').evaluate(section => scrollTo(0, section.getBoundingClientRect().top + scrollY));
    await page.waitForFunction(() => document.querySelector('#nav-links a[href="/#bewertungen"]').getAttribute('aria-current') === 'location');
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
        // The photograph fills the entire first screen on phones.
        const heroLayout = await page.evaluate(() => {
          const stage = document.querySelector('.hero-stage').getBoundingClientRect();
          const photo = document.querySelector('.hero-backdrop').getBoundingClientRect();
          return { top: stage.top + scrollY, width: stage.width, height: stage.height, photoWidth: photo.width, photoHeight: photo.height, viewport: innerHeight };
        });
        assert.equal(heroLayout.width, width, `Hero must be full width at ${width}px`);
        assert.ok(heroLayout.height >= heroLayout.viewport - 1, `Hero must fill the first screen at ${width}px`);
        assert.ok(heroLayout.photoWidth >= heroLayout.width && heroLayout.photoHeight >= heroLayout.height - 1, `Hero photo must cover the whole hero at ${width}px`);
        for (const [platform, count] of [['trustpilot', 20], ['whatsapp', 20], ['google', 20]]) {
          await page.waitForFunction(({ platform, count }) => {
            const section = document.querySelector(`[data-review-platform="${platform}"]`);
            return Number(getComputedStyle(section.querySelector('[data-review-viewport]')).getPropertyValue('--per-view')) === 1
              && section.querySelectorAll('[data-review-card]').length === count;
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
    for (const target of ['/impressum.html', '/datenschutz.html', '/404.html', '/preise/', '/kostenlos-testen/', '/assets/main.js', '/assets/template.css', '/assets/base.css', '/assets/fonts/inter-latin-variable.woff2', '/assets/fonts/sora-latin-variable.woff2', '/assets/img/hero-carnival.webp', '/assets/review-platforms.json', '/sitemap.xml', '/robots.txt']) {
      assert.equal((await page.request.get(base + target)).status(), 200, target);
    }
    for (const target of ['/impressum.html', '/datenschutz.html', '/404.html', '/preise/', '/kostenlos-testen/']) {
      await page.goto(base + target);
      await page.evaluate(() => document.fonts.ready);
      assert.equal(await page.locator('.wordmark').count(), 2, `${target} must show the wordmark`);
    }
    assert.deepEqual(externalRequests, [], 'Pages must not request externally hosted assets');
    console.log('PASS all pages and fonts load locally with no external asset requests');
    // Only Free Trial and Pricing are marketing CTAs on every page.
    const files = ['index.html', 'preise/index.html', 'kostenlos-testen/index.html', 'impressum.html', 'datenschutz.html', '404.html', 'bestellen/1-monat/index.html', 'bestellen/3-monate/index.html', 'bestellen/6-monate/index.html', 'bestellen/1-jahr/index.html'];
    const sourceHome = fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8');
    const sharedHeader = sourceHome.match(/<header class="header"[^>]*>[\s\S]*?<\/header>/)[0];
    const sharedFooter = sourceHome.match(/<footer class="footer">[\s\S]*?<\/footer>/)[0];
    for (const file of files) {
      const source = fs.readFileSync(path.join(__dirname, '..', file), 'utf8');
      assert.equal(source.match(/<header class="header"[^>]*>[\s\S]*?<\/header>/)[0], sharedHeader, `${file}: identical header`);
      assert.equal(source.match(/<footer class="footer">[\s\S]*?<\/footer>/)[0], sharedFooter, `${file}: identical footer`);
      const target = file === 'index.html' ? '/' : file.replace('index.html', '');
      await page.goto(new URL(target, base).href);
      for (const button of await page.locator('a.btn').all()) {
        const destination = new URL(await button.getAttribute('href'), base);
        assert.ok(['/preise/', '/kostenlos-testen/'].includes(destination.pathname));
        assert.ok(['Preise', 'Kostenlos testen'].includes((await button.textContent()).trim()));
      }
      assert.deepEqual(await page.locator('.nav-cta a').evaluateAll(links => links.map(link => link.getAttribute('href'))), ['/preise/', '/kostenlos-testen/']);
    }
    console.log('PASS only two marketing CTA destinations and identical headers/footers on all ten pages');

    await page.goto(base);
    assert.equal(await page.locator('[data-request-form]').count(), 0);
    const homeCards = await page.locator('#plans').evaluate(element => element.innerHTML);
    await page.goto(base + '/preise/');
    assert.equal(await page.locator('#plans').evaluate(element => element.innerHTML), homeCards, 'Pricing cards must match the homepage exactly');
    assert.equal(await page.locator('h1').textContent(), 'Preise & Pakete');
    assert.equal(await page.locator('[data-request-form], #bestellung').count(), 0, 'The catalogue must not contain the order form');
    assert.equal(await page.locator('[data-starting-price]').textContent(), '9');

    const orderRoutes = ['/bestellen/1-monat/', '/bestellen/3-monate/', '/bestellen/6-monate/', '/bestellen/1-jahr/'];
    // Click the body of each card on both catalogues, not only its action link.
    for (const catalogue of ['/', '/preise/']) {
      for (const [index, months] of [1, 3, 6, 12].entries()) {
        const devices = index + 1;
        await page.goto(base + catalogue);
        await page.locator(`[data-devices="${devices}"]`).click();
        await page.locator(`.plan[data-months="${months}"]`).click({ position: { x: 35, y: 45 } });
        await page.waitForURL(base + orderRoutes[index] + '?devices=' + devices);
        assert.equal(await page.locator('[data-order-page]').getAttribute('data-months'), String(months));
        assert.equal(await page.locator('[data-selected-devices]').textContent(), devices + (devices === 1 ? ' Gerät' : ' Geräte'));
        assert.equal(await page.locator('[data-selected-price]').textContent(), String(expected[devices - 1][index]));
        assert.equal(await page.locator('[data-order-form]').count(), 1);
        assert.equal(await page.locator('#plans').count(), 0);
      }
    }
    // All 20 deep links retain the selected quantity and price. The URL path owns the duration.
    for (const [index, route] of orderRoutes.entries()) {
      for (let devices = 1; devices <= 5; devices++) {
        await page.goto(base + route + '?devices=' + devices);
        assert.equal(await page.locator('[data-selected-price]').textContent(), String(expected[devices - 1][index]));
        assert.equal(await page.locator('[data-order-form] [name="devices"]').inputValue(), String(devices));
        assert.equal(await page.locator('[data-order-form] [name="months"]').inputValue(), String([1,3,6,12][index]));
      }
    }
    await page.goto(base + '/bestellen/6-monate/?months=12&devices=4');
    assert.equal(await page.locator('[data-selected-term]').textContent(), '6 Monate');
    assert.equal(await page.locator('[data-selected-price]').textContent(), '140');
    console.log('PASS no catalogue order form, whole-card navigation, four dedicated plan pages and all 20 correct device/price combinations');

    // Both optional forms accept blanks, any single field, and free-form values.
    for (const kind of ['trial', 'order']) {
      const target = kind === 'trial' ? '/kostenlos-testen/' : '/bestellen/1-monat/';
      let posted;
      await page.route('https://api.emailjs.com/api/v1.0/email/send', route => {
        posted = JSON.parse(route.request().postData());
        return route.fulfill({ status: 200, contentType: 'text/plain', body: 'OK' });
      });
      for (const details of [{}, { name: 'Max' }, { email: 'anything at all' }, { phone: '+49 123' }, { note: 'Nur eine Notiz\nVielen Dank!' }, { name: 'Max Mustermann', email: 'max@example.com', phone: '+49 123', note: 'Bitte per WhatsApp antworten.' }]) {
        await page.goto(base + target);
        const form = page.locator('[data-request-form]');
        assert.equal(await form.locator('[required], [aria-required="true"]').count(), 0);
        assert.equal(/\(optional\)/i.test(await form.locator('.field > span').allTextContents().then(text => text.join(' '))), false, 'Field labels must not display optional tags');
        assert.deepEqual(await form.locator('.field input, .field textarea').evaluateAll(fields => fields.map(field => field.name)), ['name', 'email', 'phone', 'note']);
        if (kind === 'trial') assert.equal(await page.locator('.trial-price b').textContent(), '0');
        for (const [field, value] of Object.entries(details)) await form.locator(`[name="${field}"]`).fill(value);
        await form.locator('button[type="submit"]').click();
        await page.locator('[data-request-success]').waitFor();
        assert.equal(posted.service_id, 'service_ehcnxxv');
        assert.equal(posted.template_id, 'template_bfl916q');
        assert.equal(posted.user_id, 'uTqKLVjvvwWeSZxdN');
        const params = posted.template_params;
        assert.equal(params.to_email, 'kontakt@iptvkanal.de');
        for (const field of ['phone', 'note']) assert.equal(params[field], details[field] || '');
        assert.equal(params.customer_email, details.email || '');
        if (details.name) assert.equal(params.from_name, details.name);
        if (details.email) assert.ok(params.message.includes(details.email));
        assert.equal(params.reply_to, details.email === 'max@example.com' ? details.email : 'kontakt@iptvkanal.de');
        if (kind === 'order') { assert.equal(params.months, 1); assert.equal(params.devices, 1); assert.equal(params.price, 9); }
      }
      await page.unroute('https://api.emailjs.com/api/v1.0/email/send');
    }
    await page.goto(base + '/bestellen/1-jahr/?devices=3');
    let orderDetails;
    await page.route('https://api.emailjs.com/api/v1.0/email/send', route => {
      orderDetails = JSON.parse(route.request().postData());
      return route.fulfill({ status: 200, contentType: 'text/plain', body: 'OK' });
    });
    await page.locator('[data-request-form] button[type="submit"]').click();
    await page.locator('[data-request-success]').waitFor();
    assert.equal(orderDetails.template_params.months, 12);
    assert.equal(orderDetails.template_params.devices, 3);
    assert.equal(orderDetails.template_params.price, 135);
    await page.unroute('https://api.emailjs.com/api/v1.0/email/send');

    // A failed submission stays on the page, preserves input, and can be retried.
    await page.goto(base + '/kostenlos-testen/');
    await page.fill('[name="note"]', 'Meine Anfrage bleibt erhalten.');
    await page.route('https://api.emailjs.com/api/v1.0/email/send', route => route.fulfill({ status: 503, contentType: 'application/json', body: '{"ok":false}' }));
    await page.locator('[data-request-form] button[type="submit"]').click();
    await page.locator('[data-form-error]').waitFor();
    assert.equal(page.url(), base + '/kostenlos-testen/');
    assert.equal(await page.locator('[name="note"]').inputValue(), 'Meine Anfrage bleibt erhalten.');
    assert.equal(await page.locator('[data-request-success]').isVisible(), false);
    assert.equal(await page.locator('[data-request-form] button[type="submit"]').isEnabled(), true);
    assert.ok(decodeURIComponent(await page.locator('[data-mail-fallback]').getAttribute('href')).includes('Meine Anfrage bleibt erhalten.'));
    await page.unroute('https://api.emailjs.com/api/v1.0/email/send');
    await page.route('https://api.emailjs.com/api/v1.0/email/send', route => route.fulfill({ status: 200, contentType: 'text/plain', body: 'OK' }));
    await page.locator('[data-request-form] button[type="submit"]').click();
    await page.locator('[data-request-success]').waitFor();
    await page.unroute('https://api.emailjs.com/api/v1.0/email/send');
    console.log('PASS empty/partial/free-form trial and order submissions, plan context, clear failure state and retry');

    for (const width of [1440, 768, 390, 320]) {
      await page.setViewportSize({ width, height: 844 });
      for (const target of ['/kostenlos-testen/', ...orderRoutes]) {
        await page.goto(base + target);
        assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, `${target} overflow at ${width}px`);
        assert.equal(await page.locator('.nav-cta .btn-primary').isVisible(), true);
        await page.locator('[data-request-form] button[type="submit"]').scrollIntoViewIfNeeded();
        assert.equal(await page.locator('[data-request-form] button[type="submit"]').isVisible(), true);
      }
    }
    console.log('PASS responsive request pages and usable forms at 320px–1440px');

    const noJS = await browser.newContext({ javaScriptEnabled: false });
    const plain = await noJS.newPage();
    await plain.route('**/*', route => new URL(route.request().url()).origin === new URL(base).origin ? route.continue() : route.abort());
    await plain.goto(base);
    assert.equal(await plain.locator('[data-review-card]').count(), 60);
    assert.equal(await plain.locator('[data-review-controls]:visible').count(), 0);
    const plainRail = plain.locator('[data-review-viewport]').first();
    await plainRail.evaluate(element => { element.scrollLeft = element.scrollWidth; });
    assert.ok(await plainRail.evaluate(element => element.scrollLeft > 0));
    assert.equal(await plain.locator('[data-plan-link]').count(), 4);
    assert.equal(await plain.locator('[data-plan-link]').nth(2).getAttribute('href'), '/bestellen/6-monate/?devices=1');
    await plain.goto(base + '/bestellen/6-monate/');
    assert.equal(await plain.locator('[data-selected-price]').textContent(), '39');
    assert.equal(await plain.locator('[data-order-form] [name="months"]').inputValue(), '6');
    await noJS.close();
    assert.deepEqual(errors, []);
    assert.deepEqual(failures, []);
    console.log('PASS local routes, anchors, no-JavaScript review scrolling, and no runtime errors');
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
