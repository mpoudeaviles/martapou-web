// martapou.com — título, menú móvil, viudas, slideshows y scroll automático de la portada
(function () {
  // ---- título: "Pou de Avilés" ocupa todo el ancho de la columna; "Marta" usa el mismo tamaño
  var title = document.querySelector('.site-title');
  function fitTitle() {
    if (!title) return;
    var line = title.querySelector('.t2');
    var max = window.innerWidth <= 800 ? 64 : 96;
    var avail = title.clientWidth;
    title.style.fontSize = '100px';
    var w = line.scrollWidth || 1;
    title.style.fontSize = Math.min(max, Math.floor(100 * avail / w * 0.98)) + 'px';
  }
  fitTitle();
  window.addEventListener('resize', fitTitle);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitTitle);

  // ---- menú en móvil
  var nav = document.getElementById('side-nav');
  var btn = nav && nav.querySelector('.menu-toggle');
  if (btn) btn.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open);
    if (!btn.dataset.open) btn.dataset.open = btn.textContent;
    btn.textContent = open ? btn.dataset.close : btn.dataset.open;
  });

  // ---- evitar viudas: une la última palabra de cada línea de texto con la anterior
  var BLOCK = /^(BR|DIV|P|LI|H1|H2|OL|UL|SMALL|IMG|IFRAME|VIDEO)$/;
  function lastOfLine(node) {
    var n = node.nextSibling;
    while (n && n.nodeType === 3 && !n.nodeValue.trim()) n = n.nextSibling;
    if (!n) {
      var p = node.parentNode;
      return p && !BLOCK.test(p.tagName) && p !== document.body ? lastOfLine(p) : true;
    }
    return n.nodeType === 1 && BLOCK.test(n.tagName);
  }
  document.querySelectorAll('.bodycopy, .side-nav').forEach(function (root) {
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (t) {
      var v = t.nodeValue;
      if (!v.trim() || !lastOfLine(t)) return;
      t.nodeValue = v.replace(/ (\S{1,14})(\s*)$/, ' $1$2');
    });
  });

  // ---- slideshows (autoplay 2.5 s, flechas)
  document.querySelectorAll('.image-gallery').forEach(function (g) {
    var slides = Array.prototype.slice.call(g.children);
    if (slides.length < 2) return;
    var ratio = 0;
    slides.forEach(function (s) {
      var img = s.tagName === 'IMG' ? s : s.querySelector('img');
      if (img) ratio = Math.max(ratio, (+img.getAttribute('height') || 1) / (+img.getAttribute('width') || 1));
    });
    function size() {
      g.style.height = Math.min(g.clientWidth * (ratio || 0.66), window.innerHeight * 0.8) + 'px';
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
    var timer;
    function restart() { clearInterval(timer); timer = setInterval(function () { show(i + 1); }, speed); }
    restart();

    var prev = document.createElement('button');
    prev.className = 'gallery-arrow prev-btn'; prev.setAttribute('aria-label', 'Previous'); prev.textContent = '←';
    var next = document.createElement('button');
    next.className = 'gallery-arrow next'; next.setAttribute('aria-label', 'Next'); next.textContent = '→';
    prev.addEventListener('click', function () { show(i - 1); restart(); });
    next.addEventListener('click', function () { show(i + 1); restart(); });
    g.appendChild(prev); g.appendChild(next);
  });

  // ---- portada: las imágenes bajan solas; si haces scroll a mano se para
  //      y a los 2 segundos sigue desde donde lo has dejado
  if (document.getElementById('home-scroll') &&
      !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var SPEED = 1;            // píxeles por fotograma
    var pos = window.scrollY;
    var pausedUntil = 0;
    function userScrolled() { pausedUntil = performance.now() + 2000; }
    ['wheel', 'touchstart', 'touchmove', 'keydown', 'mousedown'].forEach(function (ev) {
      window.addEventListener(ev, userScrolled, { passive: true });
    });
    (function step(now) {
      if (now < pausedUntil) {
        pos = window.scrollY;                 // seguir desde donde se ha quedado
      } else if (Math.abs(window.scrollY - pos) > 3) {
        pos = window.scrollY;                 // la barra de scroll también cuenta
        userScrolled();
      } else {
        pos += SPEED;
        var maxY = document.documentElement.scrollHeight - window.innerHeight;
        if (pos >= maxY - 1) pos = 0;
        window.scrollTo(0, pos);
      }
      requestAnimationFrame(step);
    })(performance.now());
  }
})();
