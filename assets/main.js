(function () {
  'use strict';

  // Existing IPTV Kanal prices, in euros: 1, 3, 6 and 12 months.
  var PRICES = {
    1: [9, 29, 39, 49],
    2: [18, 50, 69, 89],
    3: [27, 75, 105, 135],
    4: [36, 99, 140, 180],
    5: [45, 120, 175, 225]
  };
  var TERMS = ['1 Monat', '3 Monate', '6 Monate', '1 Jahr'];
  var tabs = Array.from(document.querySelectorAll('.device-switch [data-devices]'));
  var plans = Array.from(document.querySelectorAll('#plans .plan'));

  function deviceLabel(n) { return n + (n === 1 ? ' Gerät' : ' Geräte'); }
  function euro(n) { return n.toLocaleString('de-DE', { minimumFractionDigits: 2, maximumFractionDigits: 2 }); }

  function selectDevices(button) {
    var devices = Number(button.dataset.devices);
    tabs.forEach(function (tab) {
      var active = tab === button;
      tab.classList.toggle('active', active);
      tab.setAttribute('aria-pressed', String(active));
      tab.tabIndex = active ? 0 : -1;
    });
    plans.forEach(function (plan, index) {
      var price = PRICES[devices][index];
      var months = Number(plan.dataset.months);
      var saving = Math.round((1 - price / (PRICES[devices][0] * months)) * 100);
      plan.querySelector('.plan-price b').textContent = price;
      plan.querySelector('.plan-devices').textContent = deviceLabel(devices) + ' gleichzeitig';
      plan.querySelector('.plan-monthly').textContent = months === 1 ? 'einmalig, ohne Verlängerung' : 'nur ' + euro(price / months) + ' pro Monat';
      plan.querySelector('.plan-save').textContent = saving > 0 ? 'Sie sparen ' + saving + ' %' : '';
      var subject = 'IPTV Bestellung: ' + TERMS[index] + ', ' + deviceLabel(devices) + ' (' + price + ' €)';
      var body = 'Hallo,\n\nich möchte folgendes Paket bestellen:\n- Laufzeit: ' + TERMS[index] + '\n- Geräte: ' + devices + '\n- Preis: ' + price + ' €\n\nMein Gerät: ';
      plan.querySelector('.plan-btn').href = 'mailto:info@iptvkanal.de?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    });
    document.getElementById('devices-hint').textContent = 'Gleichzeitig auf ' + deviceLabel(devices) + ' schauen. Wählen Sie Ihre passende Laufzeit.';
  }

  tabs.forEach(function (button, index) {
    button.addEventListener('click', function () { selectDevices(button); });
    button.addEventListener('keydown', function (event) {
      var next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next === undefined) return;
      event.preventDefault();
      selectDevices(tabs[next]);
      tabs[next].focus();
    });
  });
  if (tabs.length) selectDevices(tabs[0]);

  var menu = document.querySelector('.menu-btn');
  var links = document.getElementById('nav-links');
  if (menu && links) {
    function setMenu(open) {
      links.classList.toggle('is-open', open);
      menu.setAttribute('aria-expanded', String(open));
      menu.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
      document.body.classList.toggle('no-scroll', open);
      document.body.classList.toggle('menu-open', open);
    }
    menu.addEventListener('click', function () { setMenu(menu.getAttribute('aria-expanded') !== 'true'); });
    links.addEventListener('click', function (event) { if (event.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
        setMenu(false);
        menu.focus();
      }
    });
    window.matchMedia('(min-width: 901px)').addEventListener('change', function (event) { if (event.matches) setMenu(false); });
  }

  var header = document.querySelector('.header');
  if (header) {
    function updateHeader() { header.classList.toggle('scrolled', window.scrollY > 10); }
    window.addEventListener('scroll', updateHeader, { passive: true });
    updateHeader();
  }

  var slider = document.querySelector('.highlights .slider');
  if (slider) {
    var arrows = Array.from(document.querySelectorAll('.highlights .slider-btn'));
    var progress = document.querySelector('.slider-progress i');
    function updateSlider() {
      var maxScroll = slider.scrollWidth - slider.clientWidth;
      if (progress) progress.style.width = (maxScroll > 0 ? slider.scrollLeft / maxScroll * 100 : 100) + '%';
      arrows.forEach(function (arrow) {
        arrow.disabled = Number(arrow.dataset.dir) < 0 ? slider.scrollLeft < 2 : slider.scrollLeft >= maxScroll - 2;
      });
    }
    function moveSlider(direction) {
      var slide = slider.querySelector('.slide');
      slider.scrollBy({ left: direction * (slide.getBoundingClientRect().width + 18), behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' });
    }
    arrows.forEach(function (arrow) { arrow.addEventListener('click', function () { moveSlider(Number(arrow.dataset.dir)); }); });
    slider.addEventListener('keydown', function (event) {
      if (event.key !== 'ArrowRight' && event.key !== 'ArrowLeft') return;
      event.preventDefault();
      moveSlider(event.key === 'ArrowRight' ? 1 : -1);
    });
    slider.addEventListener('scroll', updateSlider, { passive: true });
    window.addEventListener('resize', updateSlider);
    updateSlider();
  }

  var planStrip = document.getElementById('plans');
  var planDots = Array.from(document.querySelectorAll('.plans-dots i'));
  if (planStrip && planDots.length) {
    function updatePlanDots() {
      var inVisualOrder = plans.slice().sort(function (a, b) { return a.offsetLeft - b.offsetLeft; });
      var nearest = 0;
      var distance = Infinity;
      inVisualOrder.forEach(function (plan, index) {
        var center = plan.getBoundingClientRect().left + plan.getBoundingClientRect().width / 2;
        var delta = Math.abs(center - (planStrip.getBoundingClientRect().left + planStrip.clientWidth / 2));
        if (delta < distance) { nearest = index; distance = delta; }
      });
      planDots.forEach(function (dot, index) { dot.classList.toggle('active', index === nearest); });
    }
    planStrip.addEventListener('scroll', updatePlanDots, { passive: true });
    window.addEventListener('resize', updatePlanDots);
    updatePlanDots();
  }

  // Reviews are static HTML for accessibility and no-JavaScript use.
  // Enhancement adds filtering, text search, and progressive disclosure.
  var cards = Array.from(document.querySelectorAll('[data-review-id]'));
  if (cards.length) {
    var filter = 'all';
    var limit = 6;
    var search = document.getElementById('review-search');
    var status = document.getElementById('review-status');
    var more = document.getElementById('reviews-more');
    var filters = Array.from(document.querySelectorAll('[data-review-filter]'));
    function normalize(text) { return text.toLocaleLowerCase('de-DE').normalize('NFD').replace(/[\u0300-\u036f]/g, ''); }
    var searchText = new Map(cards.map(function (card) {
      return [card, normalize((card.querySelector('h3') ? card.querySelector('h3').textContent : '') + ' ' + card.querySelector('blockquote').textContent + ' ' + card.querySelector('.review-author strong').textContent)];
    }));
    function updateReviews() {
      var query = normalize(search.value.trim());
      var matches = cards.filter(function (card) {
        return (filter === 'all' || card.dataset.reviewGroup === filter) && searchText.get(card).includes(query);
      });
      var visible = new Set(matches.slice(0, limit));
      cards.forEach(function (card) { card.hidden = !visible.has(card); });
      filters.forEach(function (button) { button.setAttribute('aria-pressed', String(button.dataset.reviewFilter === filter)); });
      status.textContent = matches.length ? visible.size + ' von ' + matches.length + ' Einträgen angezeigt' : 'Keine passenden Bewertungen gefunden. Versuchen Sie einen anderen Suchbegriff oder Filter.';
      more.hidden = visible.size >= matches.length;
    }
    filters.forEach(function (button) {
      button.addEventListener('click', function () { filter = button.dataset.reviewFilter; limit = 6; updateReviews(); });
    });
    search.addEventListener('input', function () { limit = 6; updateReviews(); });
    more.addEventListener('click', function () { limit += 6; updateReviews(); });
    document.querySelector('.review-toolbar').hidden = false;
    document.querySelector('.review-actions').hidden = false;
    updateReviews();
  }

  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
