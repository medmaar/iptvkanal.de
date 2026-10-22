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
    var delays = { trustpilot: 1900, whatsapp: 2300, google: 2900 };
    document.querySelectorAll('[data-review-platform]').forEach(function (section) {
      var viewport = section.querySelector('[data-review-viewport]');
      var cards = Array.from(viewport.querySelectorAll('[data-review-card]'));
      var controls = section.querySelector('[data-review-controls]');
      var dotsTrack = section.querySelector('[data-review-dots-track]');
      var status = section.querySelector('[data-review-position]');
      var delay = delays[section.dataset.reviewPlatform] || 5000;
      var starts = [];
      var current = 0;
      var base = 0;
      var loopWidth = 0;
      var interacting = false;
      var manualScroll = false;
      var visible = !('IntersectionObserver' in window);
      var transition = null;
      var dotTimer;
      var timer;
      var frame;

      // Visual-only copies on both ends let the rail keep moving in either direction.
      function copy(card) {
        var clone = card.cloneNode(true);
        clone.removeAttribute('data-review-card');
        clone.setAttribute('data-review-clone', '');
        clone.setAttribute('aria-hidden', 'true');
        clone.setAttribute('inert', '');
        return clone;
      }
      var copies = cards.slice(0, 3).map(function (card) { return viewport.appendChild(copy(card)); });
      cards.slice(-3).reverse().forEach(function (card) { viewport.insertBefore(copy(card), viewport.firstElementChild); });
      viewport.classList.add('review-autoplay');

      function wrap(value, size) { return ((value % size) + size) % size; }
      function position(index) { return base + starts[index]; }

      function updateControls() {
        var text = 'Bewertung ' + (current + 1) + ' von ' + starts.length;
        if (status.textContent !== text) status.textContent = text;
      }

      // The dots never count pages: they drift one step per review and fade out at the edges.
      function resetDots() {
        window.clearTimeout(dotTimer);
        dotsTrack.classList.remove('is-moving');
        dotsTrack.style.removeProperty('--dot-shift');
        dotsTrack.removeAttribute('data-direction');
      }
      function stepDots(direction) {
        if (!dotsTrack || !direction) return;
        resetDots();
        if (motion.matches) return;
        void dotsTrack.offsetWidth;
        dotsTrack.setAttribute('data-direction', direction > 0 ? 'next' : 'prev');
        dotsTrack.classList.add('is-moving');
        dotsTrack.style.setProperty('--dot-shift', String(-direction));
        dotTimer = window.setTimeout(resetDots, 560);
      }

      function setCurrent(index) {
        var next = wrap(index, starts.length);
        var diff = next - current;
        if (diff > starts.length / 2) diff -= starts.length;
        if (diff < -starts.length / 2) diff += starts.length;
        current = next;
        if (diff) stepDots(diff > 0 ? 1 : -1);
        updateControls();
      }

      function updatePage() {
        var offset = loopWidth ? wrap(viewport.scrollLeft - base, loopWidth) : 0;
        setCurrent(starts.reduce(function (best, start, index) {
          return Math.abs(start - offset) < Math.abs(starts[best] - offset) ? index : best;
        }, 0));
      }

      function schedule() {
        window.clearTimeout(timer);
        if (!visible || document.hidden || interacting || transition || starts.length < 2) return;
        timer = window.setTimeout(function () { goTo(current + 1, false); }, delay);
      }

      function settle() {
        window.cancelAnimationFrame(frame);
        transition = null;
        manualScroll = false;
        viewport.scrollTo({ left: starts.length ? position(current) : 0, behavior: 'instant' });
      }

      function animate(time) {
        if (!transition) return;
        var progress = Math.min(1, (time - transition.started) / 550);
        var eased = 1 - Math.pow(1 - progress, 3);
        viewport.scrollTo({ left: transition.from + (transition.to - transition.from) * eased, behavior: 'instant' });
        if (progress < 1) frame = window.requestAnimationFrame(animate);
        else {
          settle();
          // Give the next review its full reading time after the slide finishes.
          schedule();
        }
      }

      function goTo(review, announce) {
        window.clearTimeout(timer);
        window.cancelAnimationFrame(frame);
        transition = null;
        setCurrent(review);
        // Past either end the rail slides into the copies, then quietly re-centres.
        var target = position(current) + (review >= starts.length ? loopWidth : review < 0 ? -loopWidth : 0);
        status.setAttribute('aria-live', announce ? 'polite' : 'off');
        manualScroll = false;
        if (motion.matches || Math.abs(viewport.scrollLeft - target) < 1) {
          settle();
          schedule();
        } else {
          transition = { from: viewport.scrollLeft, to: target, started: performance.now() };
          frame = window.requestAnimationFrame(animate);
        }
      }

      function measure() {
        var previousWidth = loopWidth;
        var previousCount = starts.length;
        // Every advance moves one review, including the multi-card desktop rows.
        starts = cards.map(function (card) { return card.offsetLeft - cards[0].offsetLeft; });
        base = cards.length ? cards[0].offsetLeft - viewport.firstElementChild.offsetLeft : 0;
        loopWidth = copies.length ? copies[0].offsetLeft - cards[0].offsetLeft : 0;
        controls.hidden = starts.length < 2;
        if (loopWidth === previousWidth && starts.length === previousCount) return;
        current = Math.min(current, Math.max(0, starts.length - 1));
        settle();
        updateControls();
        schedule();
      }

      function beginManualScroll() {
        window.clearTimeout(timer);
        window.cancelAnimationFrame(frame);
        transition = null;
        manualScroll = true;
        updatePage();
      }

      viewport.addEventListener('keydown', function (event) {
        var review;
        if (event.key === 'ArrowRight') review = current + 1;
        if (event.key === 'ArrowLeft') review = current - 1;
        if (event.key === 'Home') review = 0;
        if (event.key === 'End') review = starts.length - 1;
        if (review === undefined) return;
        event.preventDefault();
        goTo(review, true);
      });
      viewport.addEventListener('scroll', function () {
        if (transition || !manualScroll || !loopWidth) return;
        // Swiping into the copies jumps to the identical real cards, so there is no end.
        var edge = (starts[1] || 0) / 2;
        var max = viewport.scrollWidth - viewport.clientWidth;
        if (viewport.scrollLeft < edge) viewport.scrollLeft += loopWidth;
        else if (viewport.scrollLeft > max - edge) viewport.scrollLeft -= loopWidth;
        updatePage();
        schedule();
      }, { passive: true });
      viewport.addEventListener('pointerdown', function () { interacting = true; beginManualScroll(); });
      window.addEventListener('pointerup', function () { if (interacting) { interacting = false; schedule(); } });
      viewport.addEventListener('pointercancel', function () { interacting = false; schedule(); });
      viewport.addEventListener('wheel', function (event) {
        if (Math.abs(event.deltaX) > Math.abs(event.deltaY) || event.shiftKey) { beginManualScroll(); schedule(); }
      }, { passive: true });
      section.addEventListener('keydown', schedule);
      window.addEventListener('blur', function () { interacting = false; schedule(); });
      document.addEventListener('visibilitychange', function () {
        if (document.hidden) { interacting = false; if (transition) settle(); }
        schedule();
      });
      motion.addEventListener('change', function () { if (transition) settle(); resetDots(); schedule(); });
      if ('IntersectionObserver' in window) {
        new IntersectionObserver(function (entries) {
          visible = entries[0].isIntersecting;
          if (!visible && transition) settle();
          schedule();
        }, { threshold: 0 }).observe(viewport);
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
