(function () {
  'use strict';

  // Preise in Euro: [1 Monat, 3 Monate, 6 Monate, 1 Jahr]
  var PRICES = {
    1: [9, 29, 39, 49],
    2: [18, 50, 69, 89],
    3: [27, 75, 105, 135],
    4: [36, 99, 140, 180],
    5: [45, 120, 175, 225]
  };
  var TERMS = [
    { label: '1 Monat', months: 1 },
    { label: '3 Monate', months: 3 },
    { label: '6 Monate', months: 6 },
    { label: '1 Jahr', months: 12, best: true }
  ];
  var EMAIL = 'info@iptvkanal.de';

  function euro(n) {
    return n.toLocaleString('de-DE', { minimumFractionDigits: n % 1 ? 2 : 0, maximumFractionDigits: 2 });
  }

  function deviceLabel(n) {
    return n + (n === 1 ? ' Gerät' : ' Geräte');
  }

  function orderLink(devices, term, price) {
    var subject = 'IPTV Bestellung: ' + term.label + ', ' + deviceLabel(devices) + ' (' + price + ' €)';
    var body = 'Hallo,\n\nich möchte folgendes Paket bestellen:\n' +
      '- Laufzeit: ' + term.label + '\n- Geräte: ' + devices + '\n- Preis: ' + price + ' €\n\nMein Gerät: ';
    return 'mailto:' + EMAIL + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
  }

  function renderPlans(devices) {
    var prices = PRICES[devices];
    var monthly = prices[0];
    var html = TERMS.map(function (term, i) {
      var price = prices[i];
      var perMonth = price / term.months;
      var saving = Math.round((1 - price / (monthly * term.months)) * 100);
      return '<article class="plan' + (term.best ? ' plan--best' : '') + '">' +
        (term.best ? '<span class="plan__badge">Bester Preis</span>' : '') +
        '<h3>' + term.label + '</h3>' +
        '<p class="plan__price"><span>' + price + '</span> €</p>' +
        '<p class="plan__per">' + (term.months === 1 ? 'monatlich flexibel' : 'nur ' + euro(perMonth) + ' € / Monat') + '</p>' +
        (saving > 0 ? '<p class="plan__save">Du sparst ' + saving + ' %</p>' : '<p class="plan__save plan__save--none">Ohne Bindung</p>') +
        '<ul class="plan__list">' +
          '<li>' + deviceLabel(devices) + ' gleichzeitig</li>' +
          '<li>20.000+ Sender</li>' +
          '<li>Filme &amp; Serien (VOD)</li>' +
          '<li>HD / FHD / 4K</li>' +
        '</ul>' +
        '<a class="btn btn--block' + (term.best ? '' : ' btn--outline') + '" href="' + orderLink(devices, term, price) + '">Jetzt bestellen</a>' +
      '</article>';
    }).join('');
    document.getElementById('plans').innerHTML = html;
    document.getElementById('devices-hint').innerHTML =
      'Gleichzeitig auf <strong>' + deviceLabel(devices) + '</strong> schauen';
  }

  // Geräte-Auswahl
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.devices__btn'));
  function select(btn) {
    tabs.forEach(function (t) {
      var on = t === btn;
      t.classList.toggle('is-active', on);
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
    });
    renderPlans(Number(btn.dataset.devices));
  }
  tabs.forEach(function (btn, i) {
    btn.addEventListener('click', function () { select(btn); });
    btn.addEventListener('keydown', function (e) {
      var next = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : null;
      if (next === null) return;
      e.preventDefault();
      var target = tabs[(next + tabs.length) % tabs.length];
      target.focus();
      select(target);
    });
  });
  if (tabs.length) select(tabs[0]);

  // Mobile Navigation
  var toggle = document.querySelector('.nav__toggle');
  var links = document.getElementById('nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
      document.body.classList.toggle('no-scroll', open);
    });
    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A' && links.classList.contains('is-open')) toggle.click();
    });
  }

  // Header-Schatten beim Scrollen
  var nav = document.querySelector('.nav');
  function onScroll() { nav.classList.toggle('is-scrolled', window.scrollY > 10); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Einblend-Animationen
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    document.querySelectorAll('.feature, .step, .device-grid li, .section__head').forEach(function (el) {
      el.classList.add('reveal');
      io.observe(el);
    });
  }

  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
