(function () {
  'use strict';

  /* menu mobilne */
  var burger = document.querySelector('.burger'), panel = document.getElementById('panel');
  function zamknij() { if (!panel) return; panel.classList.remove('otw'); burger.setAttribute('aria-expanded', 'false'); document.body.classList.remove('menu-otw'); }
  if (burger && panel) {
    burger.addEventListener('click', function () {
      var o = !panel.classList.contains('otw');
      panel.classList.toggle('otw', o); burger.setAttribute('aria-expanded', String(o)); document.body.classList.toggle('menu-otw', o);
    });
    panel.addEventListener('click', function (e) { if (e.target.closest('a')) zamknij(); });
    window.addEventListener('resize', function () { if (innerWidth > 1024) zamknij(); });
  }

  /* pasek mobilny po przewinieciu */
  var mob = document.getElementById('mob');
  var cel = document.getElementById('hero-cta') || document.querySelector('.ph-hero');
  if (mob && cel && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (w) {
      var e = w[0]; mob.classList.toggle('widac', !e.isIntersecting && e.boundingClientRect.top < 0);
    }).observe(cel);
  }

  /* termin -> KW Hotel */
  function iso(d) { return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0'); }
  var f = document.getElementById('termin');
  if (f) {
    var od = f.querySelector('#t-od'), dO = f.querySelector('#t-do'), os = f.querySelector('#t-os'), info = f.querySelector('.termin-info');
    var dzis = new Date(); dzis.setHours(12, 0, 0, 0);
    var a = new Date(dzis); a.setDate(a.getDate() + 1); var b = new Date(dzis); b.setDate(b.getDate() + 3);
    od.min = iso(dzis); od.value = iso(a); dO.min = iso(a); dO.value = iso(b);
    var infoTxt = info.innerHTML;
    od.addEventListener('change', function () {
      if (!od.value) return;
      var n = new Date(od.value + 'T12:00'); n.setDate(n.getDate() + 1); dO.min = iso(n);
      if (!dO.value || dO.value <= od.value) { var m = new Date(od.value + 'T12:00'); m.setDate(m.getDate() + 2); dO.value = iso(m); }
    });
    var occ = f.querySelector('#t-occ');
    function ustawOcc() { occ.value = '[{"count":' + os.value + '}]'; }
    os.addEventListener('change', ustawOcc); ustawOcc();
    f.addEventListener('submit', function (e) {
      if (!od.value || !dO.value || dO.value <= od.value) { e.preventDefault(); info.innerHTML = '<span class="termin-blad">Wybierz datę wyjazdu późniejszą niż przyjazd.</span>'; return; }
      info.innerHTML = infoTxt; ustawOcc();
    });
  }

  /* obecny sezon w cenniku */
  function dt(s) { var p = s.split('.'); return new Date(+p[2], +p[1] - 1, +p[0]); }
  var teraz = new Date(); teraz.setHours(0, 0, 0, 0);
  var wiersze = Array.prototype.slice.call(document.querySelectorAll('[data-od][data-do]'));
  var aktualne = wiersze.filter(function (r) { return teraz <= dt(r.dataset.do); });
  wiersze.forEach(function (r) {
    if (aktualne.length && teraz > dt(r.dataset.do)) { r.classList.add('minelo'); return; }
    if (teraz >= dt(r.dataset.od) && teraz <= dt(r.dataset.do)) {
      r.classList.add('teraz');
      var h = r.querySelector('h3'); if (h) { var s = document.createElement('small'); s.textContent = 'obecny sezon'; h.appendChild(s); }
    }
  });

  /* mapa na klikniecie */
  var mb = document.getElementById('mapa-btn');
  if (mb) mb.addEventListener('click', function () {
    var m = document.getElementById('mapa'), fr = document.createElement('iframe');
    fr.title = 'Mapa: Willa Leśna Polana, Krynica-Zdrój';
    fr.loading = 'lazy';
    fr.src = 'https://www.openstreetmap.org/export/embed.html?bbox=20.9500%2C49.4190%2C20.9800%2C49.4310&layer=mapnik&marker=49.42529%2C20.96470';
    m.appendChild(fr); m.querySelector('.mapa-in').remove();
  });

  /* lightbox */
  var lb = document.getElementById('lb');
  if (lb) {
    var lImg = lb.querySelector('img'), lCap = lb.querySelector('figcaption'), lLicz = lb.querySelector('.lb-licz');
    var grupa = [], idx = 0, ostatni = null;
    function pokaz(i) {
      idx = (i + grupa.length) % grupa.length; var a = grupa[idx];
      lImg.src = a.getAttribute('href'); lImg.alt = a.dataset.cap || '';
      lCap.textContent = a.dataset.cap || ''; lLicz.textContent = (idx + 1) + ' / ' + grupa.length;
      var nast = grupa[(idx + 1) % grupa.length]; if (nast) { var im = new Image(); im.src = nast.getAttribute('href'); }
    }
    function otworz(a) {
      grupa = Array.prototype.slice.call(document.querySelectorAll('[data-lb="' + a.dataset.lb + '"]'));
      ostatni = a; pokaz(grupa.indexOf(a)); lb.classList.add('otw'); document.body.classList.add('menu-otw'); lb.querySelector('.lb-x').focus();
    }
    function zamk() { lb.classList.remove('otw'); document.body.classList.remove('menu-otw'); lImg.removeAttribute('src'); if (ostatni) ostatni.focus(); }
    document.addEventListener('click', function (e) {
      var a = e.target.closest('[data-lb]'); if (!a) return; e.preventDefault(); otworz(a);
    });
    lb.querySelector('.lb-x').addEventListener('click', zamk);
    lb.querySelector('.lb-p').addEventListener('click', function () { pokaz(idx - 1); });
    lb.querySelector('.lb-n').addEventListener('click', function () { pokaz(idx + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) zamk(); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && panel && panel.classList.contains('otw')) zamknij();
      if (!lb.classList.contains('otw')) return;
      if (e.key === 'Escape') zamk(); if (e.key === 'ArrowLeft') pokaz(idx - 1); if (e.key === 'ArrowRight') pokaz(idx + 1);
    });
    var x0 = null;
    lb.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) {
      if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 45) pokaz(idx + (dx < 0 ? 1 : -1));
    });
  }
})();
