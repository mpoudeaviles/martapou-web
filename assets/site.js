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


  // ---- vídeos de YouTube / Vimeo: se reproducen solos (sin sonido) cuando los ves,
  //      se pausan al salir de pantalla, con botón para activar el sonido.
  //      Se tapa con la miniatura mientras no está reproduciendo, para que no se vea
  //      el nombre del canal ni el logo de YouTube / Vimeo.
  var ICON_OFF = '<svg viewBox="0 0 24 24"><path d="M4 9h4l5-4v14l-5-4H4z" fill="currentColor"/><path d="M16 9l5 6M21 9l-5 6" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/></svg>';
  var ICON_ON = '<svg viewBox="0 0 24 24"><path d="M4 9h4l5-4v14l-5-4H4z" fill="currentColor"/><path d="M16 8.5a5 5 0 0 1 0 7M18.5 6a8.5 8.5 0 0 1 0 12" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/></svg>';
  var videos = document.querySelectorAll('.video[data-yt], .video[data-vimeo]');
  var apiWaiters = { yt: [], vimeo: [] }, apiLoading = {};
  function loadScript(src, cb) { var s = document.createElement('script'); s.src = src; s.onload = cb || null; document.head.appendChild(s); }
  function whenYT(cb) {
    if (window.YT && YT.Player) return cb();
    apiWaiters.yt.push(cb);
    if (!apiLoading.yt) {
      apiLoading.yt = true;
      window.onYouTubeIframeAPIReady = function () { apiWaiters.yt.forEach(function (f) { f(); }); };
      loadScript('https://www.youtube.com/iframe_api');
    }
  }
  function whenVimeo(cb) {
    if (window.Vimeo && Vimeo.Player) return cb();
    apiWaiters.vimeo.push(cb);
    if (!apiLoading.vimeo) {
      apiLoading.vimeo = true;
      loadScript('https://player.vimeo.com/api/player.js', function () { apiWaiters.vimeo.forEach(function (f) { f(); }); });
    }
  }
  videos.forEach(function (box) {
    box.innerHTML = '<div class="v-frame"><div></div></div><div class="v-poster"></div>' +
                    '<button class="v-sound" aria-label="Sound on/off">' + ICON_OFF + '</button>';
    var poster = box.querySelector('.v-poster'), frame = box.querySelector('.v-frame > div');
    var btn = box.querySelector('.v-sound');
    var player = null, visible = false, muted = true, showTimer;

    // miniatura
    if (box.dataset.yt) {
      var hi = 'https://i.ytimg.com/vi/' + box.dataset.yt + '/maxresdefault.jpg';
      var test = new Image();
      test.onload = function () { poster.style.backgroundImage = 'url(' + (test.naturalWidth > 200 ? hi : 'https://i.ytimg.com/vi/' + box.dataset.yt + '/hqdefault.jpg') + ')'; };
      test.src = hi;
    } else {
      fetch('https://vimeo.com/api/oembed.json?width=1280&url=' + encodeURIComponent('https://vimeo.com/' + box.dataset.vimeo + (box.dataset.h ? '/' + box.dataset.h : '')))
        .then(function (r) { return r.json(); })
        .then(function (d) { if (d.thumbnail_url) poster.style.backgroundImage = 'url(' + d.thumbnail_url.replace(/_\d+x\d+/, '_1280') + ')'; })
        .catch(function () {});
    }
    function playing(on) {
      clearTimeout(showTimer);
      if (on) showTimer = setTimeout(function () { box.classList.add('playing'); }, 900);
      else box.classList.remove('playing');
    }

    function create() {
      if (box.dataset.yt) {
        whenYT(function () {
          var id = box.dataset.yt;
          player = new YT.Player(frame, {
            videoId: id,
            playerVars: { autoplay: 1, mute: 1, controls: 0, loop: 1, playlist: id, playsinline: 1,
                          rel: 0, iv_load_policy: 3, disablekb: 1, fs: 0, modestbranding: 1, cc_load_policy: 0 },
            events: {
              onReady: function (e) { try { e.target.unloadModule('captions'); e.target.unloadModule('cc'); } catch (x) {} e.target.mute(); if (visible) e.target.playVideo(); else e.target.pauseVideo(); },
              onStateChange: function (e) {
                if (e.data === 1) { try { e.target.unloadModule('captions'); } catch (x) {} playing(true); }
                else if (e.data === 2 || e.data === -1) playing(false);
                else if (e.data === 0) { e.target.seekTo(0); e.target.playVideo(); }
              }
            }
          });
          player.kind = 'yt';
        });
      } else {
        whenVimeo(function () {
          var iframe = document.createElement('iframe');
          iframe.allow = 'autoplay; fullscreen; picture-in-picture';
          iframe.src = 'https://player.vimeo.com/video/' + box.dataset.vimeo + '?' + (box.dataset.h ? 'h=' + box.dataset.h + '&' : '') +
                       'autoplay=1&muted=1&loop=1&controls=0&title=0&byline=0&portrait=0&dnt=1&playsinline=1&autopause=0';
          frame.parentNode.replaceChild(iframe, frame);
          player = new Vimeo.Player(iframe);
          player.kind = 'vimeo';
          player.on('playing', function () { playing(true); });
          player.on('pause', function () { playing(false); });
          player.ready().then(function () { if (!visible) player.pause(); });
        });
      }
    }
    function play() { if (!player) return create(); player.kind === 'yt' ? player.playVideo && player.playVideo() : player.play().catch(function () {}); }
    function pause() { if (!player) return; player.kind === 'yt' ? player.pauseVideo && player.pauseVideo() : player.pause().catch(function () {}); }

    btn.addEventListener('click', function () {
      if (!player) return;
      muted = !muted;
      if (player.kind === 'yt') { if (muted) player.mute(); else { player.unMute(); player.setVolume(100); } }
      else { player.setMuted(muted); if (!muted) player.setVolume(1); }
      btn.innerHTML = muted ? ICON_OFF : ICON_ON;
      box.classList.toggle('sound-on', !muted);
    });

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { visible = en.intersectionRatio >= 0.5; visible ? play() : pause(); });
      }, { threshold: [0, 0.5, 1] }).observe(box);
    } else { visible = true; play(); }
  });

  // ---- resumen amarillo junto al ratón al pasar por un proyecto
  var tipEl = document.createElement('div');
  tipEl.id = 'tip';
  document.body.appendChild(tipEl);
  document.addEventListener('mouseover', function (e) {
    var t = e.target.closest && e.target.closest('[data-tip]');
    if (t) { tipEl.textContent = t.getAttribute('data-tip'); tipEl.classList.add('on'); }
    else tipEl.classList.remove('on');
  });
  document.addEventListener('mousemove', function (e) {
    var x = e.clientX + 18, y = e.clientY + 20;
    var w = tipEl.offsetWidth;
    if (x + w > window.innerWidth - 8) x = e.clientX - w - 12;
    tipEl.style.transform = 'translate(' + x + 'px,' + y + 'px)';
  });

  // ---- portada: scroll infinito que no para; si haces scroll a mano sigue desde ahí
  var list = document.getElementById('home-scroll');
  if (list) {
    var originals = Array.prototype.slice.call(list.children);
    function addCopy() {
      originals.forEach(function (n) {
        var c = n.cloneNode(true);
        c.setAttribute('aria-hidden', 'true'); c.setAttribute('tabindex', '-1');
        list.appendChild(c);
      });
    }
    addCopy();
    var loopH = 0;
    function measure() {
      loopH = list.children[originals.length].offsetTop - originals[0].offsetTop;
      // asegurar que siempre hay imágenes por debajo de la pantalla
      while (list.offsetHeight - loopH < window.innerHeight * 1.5 && list.children.length < originals.length * 6) {
        addCopy();
      }
    }
    measure();
    window.addEventListener('resize', measure);
    window.addEventListener('load', measure);
    list.querySelectorAll('img').forEach(function (im) { im.addEventListener('load', measure); });

    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var SPEED = 1;             // píxeles por fotograma
    var pos = window.scrollY;
    (function step() {
      if (Math.abs(window.scrollY - pos) > 2) pos = window.scrollY;   // el usuario ha movido el scroll
      if (!reduce) pos += SPEED;
      var start = originals[0].offsetTop;
      if (loopH > 0 && pos >= start + loopH) pos -= loopH;          // vuelve a empezar sin salto
      if (!reduce || Math.abs(window.scrollY - pos) > 1) window.scrollTo(0, pos);
      requestAnimationFrame(step);
    })();
  }
})();
