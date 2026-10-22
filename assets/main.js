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
    document.addEventListener('click', function (event) {
      if (menu.getAttribute('aria-expanded') === 'true' && !event.target.closest('.nav')) setMenu(false);
    });
    window.matchMedia('(min-width: 901px)').addEventListener('change', function (event) { if (event.matches) setMenu(false); });
  }

  var header = document.querySelector('.header');
  if (header) {
    var destinations = links ? Array.from(links.querySelectorAll('a[href^="#"]')).map(function (link) {
      return { link: link, section: document.getElementById(link.hash.slice(1)) };
    }).filter(function (item) { return item.section; }) : [];
    var headerFrame = false;
    var currentDestination;
    function updateHeader() {
      headerFrame = false;
      header.classList.toggle('scrolled', window.scrollY > 10);
      var active = destinations.find(function (item) {
        var bounds = item.section.getBoundingClientRect();
        return bounds.top <= 160 && bounds.bottom > 160;
      });
      if (active !== currentDestination) {
        destinations.forEach(function (item) { item.link.removeAttribute('aria-current'); });
        if (active) active.link.setAttribute('aria-current', 'location');
        currentDestination = active;
      }
    }
    function scheduleHeader() {
      if (!headerFrame) { headerFrame = true; window.requestAnimationFrame(updateHeader); }
    }
    window.addEventListener('scroll', scheduleHeader, { passive: true });
    window.addEventListener('resize', scheduleHeader);
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

  function initReviewCarousels() {
    var motion = window.matchMedia('(prefers-reduced-motion: reduce)');
    document.querySelectorAll('[data-review-platform]').forEach(function (section) {
      var viewport = section.querySelector('[data-review-viewport]');
      var cards = Array.from(viewport.querySelectorAll('[data-review-card]'));
      var controls = section.querySelector('[data-review-controls]');
      var currentPage = section.querySelector('[data-review-current]');
      var totalPages = section.querySelector('[data-review-total]');
      var position = section.querySelector('[data-review-position]');
      var starts = [];
      var current = 0;
      var focused = false;
      var interacting = false;
      var visible = !('IntersectionObserver' in window);
      var scrollTarget = null;
      var timer;

      function canAutoSlide() {
        return starts.length > 1 && !focused && !interacting && visible && !document.hidden;
      }

      function schedule() {
        window.clearTimeout(timer);
        if (!canAutoSlide()) return;
        timer = window.setTimeout(function () {
          if (canAutoSlide()) goTo((current + 1) % starts.length, false);
        }, 6000);
      }

      function updateControls() {
        currentPage.textContent = String(current + 1).padStart(2, '0');
        totalPages.textContent = String(starts.length).padStart(2, '0');
        var text = 'Seite ' + (current + 1) + ' von ' + starts.length;
        if (position.textContent !== text) position.textContent = text;
      }

      function goTo(page, announce) {
        current = (page + starts.length) % starts.length;
        position.setAttribute('aria-live', announce ? 'polite' : 'off');
        scrollTarget = starts[current];
        viewport.scrollTo({ left: scrollTarget, behavior: motion.matches ? 'instant' : 'smooth' });
        updateControls();
        schedule();
      }

      function measure() {
        var perView = Math.max(1, Number(window.getComputedStyle(viewport).getPropertyValue('--per-view')) || 1);
        var maxScroll = Math.max(0, viewport.scrollWidth - viewport.clientWidth);
        starts = [];
        for (var index = 0; index < cards.length; index += perView) {
          starts.push(Math.min(cards[index].offsetLeft - cards[0].offsetLeft, maxScroll));
        }
        starts = starts.filter(function (start, index) { return index === 0 || Math.abs(start - starts[index - 1]) > 1; });
        controls.hidden = starts.length < 2;
        current = Math.min(current, starts.length - 1);
        scrollTarget = starts[current] || 0;
        viewport.scrollTo({ left: scrollTarget, behavior: 'instant' });
        updateControls();
        schedule();
      }

      section.querySelector('[data-review-prev]').addEventListener('click', function () { goTo(current - 1, true); });
      section.querySelector('[data-review-next]').addEventListener('click', function () { goTo(current + 1, true); });
      viewport.addEventListener('keydown', function (event) {
        var page;
        if (event.key === 'ArrowRight') page = current + 1;
        if (event.key === 'ArrowLeft') page = current - 1;
        if (event.key === 'Home') page = 0;
        if (event.key === 'End') page = starts.length - 1;
        if (page === undefined) return;
        event.preventDefault();
        goTo(page, true);
      });
      viewport.addEventListener('scroll', function () {
        // An animated transition passes other pages on its way to the target.
        // Keep its destination stable so focus or reduced motion cannot rewind it.
        if (scrollTarget !== null) {
          if (Math.abs(viewport.scrollLeft - scrollTarget) > 2) return;
          scrollTarget = null;
        }
        var closest = starts.reduce(function (best, start, index) {
          return Math.abs(start - viewport.scrollLeft) < Math.abs(starts[best] - viewport.scrollLeft) ? index : best;
        }, 0);
        if (closest !== current) { current = closest; updateControls(); }
      }, { passive: true });
      viewport.addEventListener('pointerdown', function () {
        scrollTarget = null;
        interacting = true;
        focused = false;
        schedule();
      });
      viewport.addEventListener('wheel', function () { scrollTarget = null; schedule(); }, { passive: true });
      window.addEventListener('pointerup', function () { if (interacting) { interacting = false; schedule(); } });
      viewport.addEventListener('pointercancel', function () { interacting = false; schedule(); });
      section.addEventListener('pointerdown', function () { focused = false; schedule(); });
      section.addEventListener('keydown', function () { focused = true; schedule(); });
      section.addEventListener('focusin', function (event) {
        focused = event.target.matches(':focus-visible');
        schedule();
      });
      section.addEventListener('focusout', function (event) {
        focused = Boolean(event.relatedTarget && section.contains(event.relatedTarget) && event.relatedTarget.matches(':focus-visible'));
        schedule();
      });
      document.addEventListener('visibilitychange', schedule);
      motion.addEventListener('change', function (event) {
        if (event.matches) viewport.scrollTo({ left: starts[current] || 0, behavior: 'instant' });
        schedule();
      });
      if ('IntersectionObserver' in window) {
        new IntersectionObserver(function (entries) {
          visible = entries[0].isIntersecting;
          schedule();
        }, { threshold: .2 }).observe(section);
      }
      if ('ResizeObserver' in window) new ResizeObserver(measure).observe(viewport);
      else window.addEventListener('resize', measure);
      measure();
    });
  }

  // Each platform has an independent, progressively enhanced carousel.
  initReviewCarousels();

  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
