/* ui_effects.js
   1) Hero snap + datasets (inHero / inFooter)
   2) Global stars (WORLD field): seeded across whole page, world-wrap, stream anchored to avatar, ping-pong, clipped at footer
*/

// =====================
// 1) HERO SNAP + DATASETS
// =====================
(() => {
   const root = document.documentElement;
   const scrollContainer = document.getElementById("page-scroll");
   if (!scrollContainer) return;

   const hero = document.getElementById("inicio");
   const profile = document.getElementById("perfil");
   const footer = document.getElementById("footer");
   if (!hero) return;

   let inHero = true;
   let isSnapping = false;

   const HERO_TOP_PX = 120;

   const updateHeroTopState = () => {
      const atTop = scrollContainer.scrollTop <= HERO_TOP_PX;
      inHero = atTop;
      root.dataset.inHero = atTop ? "true" : "false";
   };

   updateHeroTopState();
   scrollContainer.addEventListener("scroll", updateHeroTopState, { passive: true });

   if (footer) {
      const footerObserver = new IntersectionObserver(
         ([entry]) => {
            root.dataset.inFooter = entry.isIntersecting ? "true" : "false";
         },
         { root: scrollContainer, threshold: 0.4 },
      );
      footerObserver.observe(footer);
   }

   const snapToProfile = () => {
      if (!profile || isSnapping) return;
      isSnapping = true;
      profile.scrollIntoView({ behavior: "smooth", block: "start" });
      window.setTimeout(() => (isSnapping = false), 700);
   };

   const onWheel = (event) => {
      if (!inHero) return;
      if (event.deltaY > 0) {
         event.preventDefault();
         snapToProfile();
      }
   };

   let touchStartY = 0;
   const onTouchStart = (event) => {
      touchStartY = event.touches[0].clientY;
   };

   const onTouchEnd = (event) => {
      if (!inHero) return;
      const touchEndY = event.changedTouches[0].clientY;
      if (touchStartY - touchEndY > 40) snapToProfile();
   };

   scrollContainer.addEventListener("wheel", onWheel, { passive: false });
   scrollContainer.addEventListener("touchstart", onTouchStart, { passive: true });
   scrollContainer.addEventListener("touchend", onTouchEnd, { passive: true });
})();

// =====================
// 2) GLOBAL STARS (WORLD FIELD)
// =====================
(() => {
   const GLOBAL_KEY = "__LB_SITE_STARS__";

   // Hot-reload: limpia instancia anterior si existe
   if (window[GLOBAL_KEY] && typeof window[GLOBAL_KEY].cleanup === "function") {
      window[GLOBAL_KEY].cleanup();
   }

   const root = document.documentElement;
   const scrollerEl = document.getElementById("page-scroll");
   const scrollTop = () => (scrollerEl ? scrollerEl.scrollTop : window.scrollY || 0);

   const reduceMotion =
      window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

   // Host fijo de fondo
   let host = document.getElementById("site-stars");
   if (!host) {
      host = document.createElement("div");
      host.id = "site-stars";
      document.body.appendChild(host);
   }

   // Canvas
   let canvas = host.querySelector("canvas");
   if (!canvas) {
      canvas = document.createElement("canvas");
      canvas.id = "site-stars-canvas";
      host.appendChild(canvas);
   }

   const ctx = canvas.getContext("2d", { alpha: true });
   if (!ctx) return;

   // =====================
   // STATE
   // =====================
   const S = {
      raf: 0,
      w: 1,
      h: 1,
      dpr: 1,
      lastT: performance.now(),
      stars: [],
      originWorld: { x: 0, y: 0 },
      footerCutWorld: Infinity,
      lastMeasuredWorldH: 0,
      bootTimer: 0,
      bootTimeouts: [],
      listeners: [],
      drawerObserver: null,
   };

   window[GLOBAL_KEY] = { cleanup };

   // =====================
   // TUNING (tu look)
   // =====================
   const STAR_DENSITY = 8.6;
   const MIN_STARS = 900;
   const MAX_STARS = 10300;

   const DENSE_RATIO = 0.95;

   const SLOPE_ABS = 0.45; // diagonal general
   const WAVE_FREQ = 0.01;

   const SIGMA_SPAWN_MOBILE = 120;
   const SIGMA_SPAWN_DESKTOP = 435;

   // =====================
   // HELPERS
   // =====================
   const rand = (a, b) => a + Math.random() * (b - a);

   const randn = () => {
      let u = 0,
         v = 0;
      while (u === 0) u = Math.random();
      while (v === 0) v = Math.random();
      return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
   };

   const clamp = (x, a, b) => Math.max(a, Math.min(b, x));

   // ping-pong 0..range
   const tri = (x, range) => {
      if (range <= 0) return 0;
      let m = x % (2 * range);
      if (m < 0) m += 2 * range;
      return m <= range ? m : 2 * range - m;
   };

   const pickColor = () => {
      const r = Math.random();
      if (r < 0.78) return [100, 255, 218];
      if (r < 0.97) return [191, 253, 243];
      return [255, 255, 255];
   };

   const worldHeight = () =>
      scrollerEl ? scrollerEl.scrollHeight : document.documentElement.scrollHeight;

   // ===== drawer state -> baja opacidad del fondo =====
   const updateDrawerState = () => {
      const open = !!document.querySelector(".mobile-menu-overlay");
      root.dataset.drawerOpen = open ? "true" : "false";
   };

   const updateFooterCutWorld = () => {
      const footer = document.getElementById("footer");
      if (!footer || !scrollerEl) {
         S.footerCutWorld = worldHeight();
         return;
      }
      const st = scrollTop();
      const scRect = scrollerEl.getBoundingClientRect();
      const fr = footer.getBoundingClientRect();
      // top del footer en coords del scroller
      S.footerCutWorld = st + (fr.top - scRect.top);
   };

   const computeOriginWorld = () => {
      const st = scrollTop();
      const avatar =
         document.getElementById("cris-avatar-wrap") || document.getElementById("cris-avatar");
      if (!avatar || !scrollerEl) {
         return { x: S.w * 0.28, y: st + S.h * 0.38 };
      }

      const ar = avatar.getBoundingClientRect();
      const scRect = scrollerEl.getBoundingClientRect();

      const x = ar.left + ar.width * 0.52; // host ocupa viewport completo
      const yInScroller = ar.top - scRect.top + ar.height * 0.46;

      return { x, y: st + yInScroller };
   };

   const updateOrigin = () => {
      S.originWorld = computeOriginWorld();
   };

   // corriente: diagonal + onda, con “rebote” (ping-pong) en márgenes
   const streamXAtY = (yWorld, t) => {
      const o = S.originWorld || { x: S.w * 0.28, y: scrollTop() + S.h * 0.38 };

      const pad = S.w < 700 ? 22 : 48;
      const range = Math.max(1, S.w - pad * 2);

      const amp = S.w < 700 ? 48 : 74;
      const wave = Math.sin(yWorld * WAVE_FREQ + t * 0.9) * amp;

      const raw = o.x - pad + (yWorld - o.y) * SLOPE_ABS + wave;
      return pad + tri(raw, range);
   };

   // =====================
   // BUILD STARS (WORLD SEEDED)
   // =====================
   const buildStars = () => {
      S.stars = [];
      updateOrigin();
      updateFooterCutWorld();

      const maxWorld = Math.max(1, Math.min(worldHeight(), S.footerCutWorld));

      const area = S.w * S.h;
      const baseCount = Math.floor((area / 900) * STAR_DENSITY);

      // sube cantidad según largo de página, pero cap con MAX_STARS
      const factor = Math.max(1, maxWorld / S.h);
      let count = Math.floor(baseCount * factor);
      count = clamp(count, MIN_STARS, MAX_STARS);

      const sigmaSpawn = S.w < 700 ? SIGMA_SPAWN_MOBILE : SIGMA_SPAWN_DESKTOP;

      for (let i = 0; i < count; i++) {
         const layer = Math.random() < 0.65 ? 0 : Math.random() < 0.85 ? 1 : 2;

         const radius =
            layer === 0 ? rand(0.35, 0.85) : layer === 1 ? rand(0.45, 1.05) : rand(0.55, 1.2);

         const baseA =
            layer === 0 ? rand(0.1, 0.26) : layer === 1 ? rand(0.12, 0.3) : rand(0.16, 0.42);

         const sp = layer === 0 ? rand(10, 22) : layer === 1 ? rand(16, 30) : rand(22, 38);

         // WORLD y: desde el primer frame por toda la página
         const y = Math.random() * maxWorld;

         let x;
         if (Math.random() < DENSE_RATIO) {
            const cx = streamXAtY(y, 0);
            x = cx + randn() * sigmaSpawn;
         } else {
            x = Math.random() * S.w;
         }

         x = ((x % S.w) + S.w) % S.w;

         S.stars.push({
            x,
            y,
            r: radius,
            a: baseA,
            sp,
            phase: Math.random() * Math.PI * 2,
            col: pickColor(),
         });
      }
   };

   const resizeCanvas = () => {
      const r = host.getBoundingClientRect();
      S.w = Math.max(1, Math.floor(r.width));
      S.h = Math.max(1, Math.floor(r.height));
      S.dpr = window.devicePixelRatio || 1;

      canvas.width = Math.floor(S.w * S.dpr);
      canvas.height = Math.floor(S.h * S.dpr);
      canvas.style.width = `${S.w}px`;
      canvas.style.height = `${S.h}px`;

      ctx.setTransform(S.dpr, 0, 0, S.dpr, 0, 0);

      buildStars();
   };

   const maybeRebuildForHeightChange = () => {
      updateFooterCutWorld();
      const wh = Math.max(1, Math.min(worldHeight(), S.footerCutWorld));
      if (Math.abs(wh - S.lastMeasuredWorldH) > 120) {
         S.lastMeasuredWorldH = wh;
         resizeCanvas(); // rebuild incluida
         updateOrigin();
      }
   };

   const step = (now) => {
      const dt = Math.min(0.04, (now - S.lastT) / 1000);
      S.lastT = now;

      ctx.clearRect(0, 0, S.w, S.h);

      const t = now / 1000;
      updateOrigin();
      updateFooterCutWorld();

      const st = scrollTop();
      const cutScreen = S.footerCutWorld - st; // borde superior del footer en pantalla

      const maxWorld = Math.max(1, Math.min(worldHeight(), S.footerCutWorld));

      const sigmaW = S.w < 700 ? 105 : 150;
      const sigmaRespawn = S.w < 700 ? SIGMA_SPAWN_MOBILE : SIGMA_SPAWN_DESKTOP;

      for (let i = 0; i < S.stars.length; i++) {
         const s = S.stars[i];

         // ===== Movimiento WORLD continuo (no respawn por viewport) =====
         s.y += s.sp * dt;
         if (s.y >= maxWorld) s.y -= maxWorld;

         // y en pantalla (mundo)
         const yScreen = s.y - st;

         // no dibujar si está fuera del viewport
         if (yScreen < -80 || yScreen > S.h + 80) continue;

         // clip footer (no invade)
         if (yScreen >= cutScreen) continue;

         // drift x + onda transversal
         const waveMove = Math.sin(yScreen * 0.013 + t * 1.25 + s.phase) * (S.w < 700 ? 14 : 18);
         s.x += s.sp * 0.55 * dt + waveMove * dt;

         // wrap x
         if (s.x > S.w + 40) s.x = -40;
         if (s.x < -40) s.x = S.w + 40;

         // concentración según cercanía a la corriente (WORLD y)
         const cx = streamXAtY(s.y, t);
         const d = Math.abs(s.x - cx);
         const weight = Math.exp(-(d * d) / (2 * sigmaW * sigmaW));

         const tw = 0.86 + 0.14 * Math.sin(t * 2.0 + s.phase);

         const alpha = s.a * (0.22 + 0.95 * weight) * tw;
         const alphaBoost = Math.min(1, alpha * (1 + 2.2 * weight));

         // tinte cian en corriente
         const ACCENT = [100, 255, 218];
         const tint = Math.min(1, 2.5 * weight);
         const bright = 1 + 0.6 * weight;

         let rr = s.col[0] * (1 - tint) + ACCENT[0] * tint;
         let gg = s.col[1] * (1 - tint) + ACCENT[1] * tint;
         let bb = s.col[2] * (1 - tint) + ACCENT[2] * tint;

         rr = Math.min(255, rr * bright);
         gg = Math.min(255, gg * bright);
         bb = Math.min(255, bb * bright);

         ctx.beginPath();
         ctx.fillStyle = `rgba(${rr | 0},${gg | 0},${bb | 0},${alphaBoost.toFixed(3)})`;
         ctx.arc(s.x, yScreen, s.r, 0, Math.PI * 2);
         ctx.fill();
      }

      if (!reduceMotion) S.raf = requestAnimationFrame(step);
   };

   // =====================
   // EVENTS
   // =====================
   const onResize = () => {
      requestAnimationFrame(() => {
         resizeCanvas();
         updateOrigin();
         maybeRebuildForHeightChange();
      });
   };

   const onScroll = () => {
      updateOrigin();
      updateFooterCutWorld();
      maybeRebuildForHeightChange();
   };

   window.addEventListener("resize", onResize, { passive: true });
   S.listeners.push([window, "resize", onResize]);

   (scrollerEl || window).addEventListener("scroll", onScroll, { passive: true });
   S.listeners.push([scrollerEl || window, "scroll", onScroll]);

   // Drawer observer (para atenuar)
   updateDrawerState();
   S.drawerObserver = new MutationObserver(updateDrawerState);
   S.drawerObserver.observe(document.body, { childList: true, subtree: true });

   // =====================
   // INIT + BOOT CHECKS
   // =====================
   resizeCanvas();
   updateOrigin();
   updateFooterCutWorld();

   requestAnimationFrame(() => {
      resizeCanvas();
      updateOrigin();
      updateFooterCutWorld();
   });

   S.lastMeasuredWorldH = Math.max(1, Math.min(worldHeight(), S.footerCutWorld));

   let checks = 0;
   S.bootTimer = setInterval(() => {
      maybeRebuildForHeightChange();
      checks += 1;
      if (checks >= 10) {
         clearInterval(S.bootTimer);
         S.bootTimer = 0;
      }
   }, 600);

   S.bootTimeouts.push(setTimeout(maybeRebuildForHeightChange, 250));
   S.bootTimeouts.push(setTimeout(maybeRebuildForHeightChange, 1200));

   if (!reduceMotion) {
      S.raf = requestAnimationFrame(step);
   } else {
      step(performance.now());
   }

   function cleanup() {
      try {
         if (S.raf) cancelAnimationFrame(S.raf);
      } catch (_) {}
      try {
         if (S.bootTimer) clearInterval(S.bootTimer);
      } catch (_) {}
      try {
         for (const t of S.bootTimeouts) clearTimeout(t);
      } catch (_) {}
      try {
         if (S.drawerObserver) S.drawerObserver.disconnect();
      } catch (_) {}
      for (const [target, evt, fn] of S.listeners) {
         try {
            target.removeEventListener(evt, fn);
         } catch (_) {}
      }
      S.listeners = [];
   }
})();
