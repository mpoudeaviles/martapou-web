// martapou.com — slideshows, menú móvil y scroll automático de la home
(function () {
  // ---- menú en móvil
  var nav = document.getElementById('side-nav');
  var btn = nav && nav.querySelector('.menu-toggle');
  if (btn) btn.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open);
    if (!btn.dataset.open) btn.dataset.open = btn.textContent;
    btn.textContent = open ? btn.dataset.close : btn.dataset.open;
  });

  // ---- slideshows (autoplay 2.5 s, flechas, clic = siguiente)
  document.querySelectorAll('.image-gallery').forEach(function (g) {
    var slides = Array.prototype.slice.call(g.children);
    if (slides.length < 2) return;
    // altura: la proporción de la imagen más alta, limitada a 80% de la pantalla
    var ratio = 0;
    slides.forEach(function (s) {
      var img = s.tagName === 'IMG' ? s : s.querySelector('img');
      if (img) ratio = Math.max(ratio, (+img.getAttribute('height') || 1) / (+img.getAttribute('width') || 1));
    });
    function size() {
      var h = Math.min(g.clientWidth * (ratio || 0.66), window.innerHeight * 0.8);
      g.style.height = h + 'px';
    }
    size();
    window.addEventListener('resize', size);
    if (g.dataset.transition === 'slide') g.classList.add('slide');
    if (g.querySelector('a')) g.classList.add('links');
    g.classList.add('ready');

    var i = 0;
    slides[0].classList.add('on');
    function show(n) {
      slides[i].classList.remove('on');
      slides.forEach(function (s) { s.classList.remove('prev'); });
      var forward = n > i || (i === slides.length - 1 && n === 0);
      if (forward) slides[i].classList.add('prev');
      i = (n + slides.length) % slides.length;
      slides[i].classList.add('on');
    }
    var speed = (parseFloat(g.dataset.speed) || 2.5) * 1000;
    var timer = setInterval(function () { show(i + 1); }, speed);
    function restart() { clearInterval(timer); timer = setInterval(function () { show(i + 1); }, speed); }

    var prev = document.createElement('button');
    prev.className = 'gallery-arrow prev-btn'; prev.setAttribute('aria-label', 'Previous'); prev.textContent = '←';
    var next = document.createElement('button');
    next.className = 'gallery-arrow next'; next.setAttribute('aria-label', 'Next'); next.textContent = '→';
    prev.addEventListener('click', function () { show(i - 1); restart(); });
    next.addEventListener('click', function () { show(i + 1); restart(); });
    g.appendChild(prev); g.appendChild(next);
  });

  // ---- home: la columna de imágenes baja sola y vuelve arriba al final
  if (document.getElementById('home-scroll') &&
      !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var paused = false, t;
    function pause() { paused = true; clearTimeout(t); t = setTimeout(function () { paused = false; }, 2500); }
    ['wheel', 'touchstart', 'keydown'].forEach(function (ev) { window.addEventListener(ev, pause, { passive: true }); });
    (function step() {
      if (!paused) {
        window.scrollBy(0, 1);
        if (window.innerHeight + window.scrollY >= document.body.scrollHeight - 1) window.scrollTo(0, 0);
      }
      requestAnimationFrame(step);
    })();
  }
})();
