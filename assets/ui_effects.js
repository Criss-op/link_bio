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

   const getScrollTop = () => {
      const a = scrollContainer ? scrollContainer.scrollTop : 0;
      const b = window.scrollY || 0;
      return Math.max(a, b); // usa el scroller que realmente se está moviendo
   };

   const updateHeroTopState = () => {
      const atTop = getScrollTop() <= HERO_TOP_PX;
      inHero = atTop;
      root.dataset.inHero = atTop ? "true" : "false";
   };

   updateHeroTopState();
   scrollContainer.addEventListener("scroll", updateHeroTopState, { passive: true });
   window.addEventListener("scroll", updateHeroTopState, { passive: true });

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
      window.setTimeout(() => {
         isSnapping = false;
      }, 700);
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
      if (touchStartY - touchEndY > 40) {
         snapToProfile();
      }
   };

   scrollContainer.addEventListener("wheel", onWheel, { passive: false });
   scrollContainer.addEventListener("touchstart", onTouchStart, { passive: true });
   scrollContainer.addEventListener("touchend", onTouchEnd, { passive: true });
})();

// ===== Stars: world-based + ping-pong stream + no footer intrusion =====
(() => {
   const root = document.documentElement;
   const scrollerEl = document.getElementById("page-scroll");
   if (!scrollerEl) return;

   // Detecta drawer abierto (overlay siempre montado; usamos clase is-open)
   const syncDrawerState = () => {
      const overlay = document.querySelector(".mobile-menu-overlay");
      if (!overlay) {
         root.dataset.drawerOpen = "false";
         return;
      }

      const cs = window.getComputedStyle(overlay);
      const open =
         overlay.classList.contains("is-open") &&
         cs.display !== "none" &&
         cs.visibility !== "hidden";

      root.dataset.drawerOpen = open ? "true" : "false";
   };

   syncDrawerState();

   // Observa cambios de clase del overlay (no childList)
   const attachOverlayObserver = () => {
      const overlay = document.querySelector(".mobile-menu-overlay");
      if (!overlay) return;

      const obs = new MutationObserver(syncDrawerState);
      obs.observe(overlay, { attributes: true, attributeFilter: ["class", "style"] });
   };

   attachOverlayObserver();
   window.addEventListener("resize", syncDrawerState, { passive: true });

   let host = document.getElementById("site-stars");
   if (!host) {
      host = document.createElement("div");
      host.id = "site-stars";

      // Montar dentro del contenedor REAL del sitio, no en body
      const scroller = document.getElementById("page-scroll");
      const mountPoint = scroller ? scroller.parentElement : document.body;

      mountPoint.appendChild(host);
   }

   // anti-duplicado (hot reload)
   if (host.dataset.starsInit === "true") return;
   host.dataset.starsInit = "true";

   let canvas = host.querySelector("canvas");
   if (!canvas) {
      canvas = document.createElement("canvas");
      canvas.id = "site-stars-canvas";
      host.appendChild(canvas);
   }

   const ctx = canvas.getContext("2d", { alpha: true });
   if (!ctx) return;

   const reduceMotion =
      window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

   // tuning
   const STAR_DENSITY = 23;
   const MIN_STARS = 2100;
   const MAX_STARS = 26600;
   const FAR_STARS_MAX = 20;
   const FAR_STAR_RADIUS = 6;

   const DENSE_RATIO = 0.95;
   const SIGMA_SPAWN_MOBILE = 105;
   const SIGMA_SPAWN_DESKTOP = 170;

   let w = 1,
      h = 1,
      dpr = 1;
   let stars = [];
   let rafId = 0;
   let lastT = performance.now();

   const rand = (a, b) => a + Math.random() * (b - a);
   const clamp = (x, a, b) => Math.max(a, Math.min(b, x));

   const randn = () => {
      let u = 0,
         v = 0;
      while (u === 0) u = Math.random();
      while (v === 0) v = Math.random();
      return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
   };

   const scrollTop = () => (scrollerEl ? scrollerEl.scrollTop : window.scrollY || 0);

   // footer cut in WORLD coords
   let footerCutWorld = Infinity;

   const updateFooterCutWorld = () => {
      const footer = document.getElementById("footer");
      if (!footer || !scrollerEl) {
         footerCutWorld = scrollerEl
            ? scrollerEl.scrollHeight
            : document.documentElement.scrollHeight;
         return;
      }
      const st = scrollTop();
      const scRect = scrollerEl.getBoundingClientRect();
      const fr = footer.getBoundingClientRect();
      footerCutWorld = st + (fr.top - scRect.top);
   };

   const worldHeight = () =>
      scrollerEl ? scrollerEl.scrollHeight : document.documentElement.scrollHeight;

   let originWorld = { x: 0, y: 0 };

   const updateOrigin = () => {
      const avatar =
         document.getElementById("cris-avatar-wrap") || document.getElementById("cris-avatar");
      if (!avatar || !scrollerEl) {
         originWorld = { x: w * 0.28, y: scrollTop() + h * 0.38 };
         return;
      }
      const st = scrollTop();
      const scRect = scrollerEl.getBoundingClientRect();
      const ar = avatar.getBoundingClientRect();

      originWorld = {
         x: ar.left + ar.width * 0.52,
         y: st + (ar.top - scRect.top) + ar.height * 0.46,
      };
   };

   // triangular wave to bounce inside [0..range]
   const tri = (x, range) => {
      const p = 2 * range;
      let t = x % p;
      if (t < 0) t += p;
      return t <= range ? t : p - t;
   };

   // stream center in WORLD-Y
   const streamXAtY = (yWorld, t) => {
      const slope = 0.45;
      const base = originWorld.x + (yWorld - originWorld.y) * slope;

      const amp = w < 700 ? 48 : 74;
      const freq = 0.01;

      const wave = Math.sin(yWorld * freq + t * 0.9) * amp;

      const margin = 64;
      const range = Math.max(1, w - 2 * margin);
      const raw = base + wave - margin;
      return margin + tri(raw, range);
   };

   // CAMBIO: 17% blancas del TOTAL. El 83% restante conserva la proporción original acento/hielo.
   // Original: 78% acento, 19% hielo, 3% blanco.
   // Nuevo: 66.742268% acento, 16.257732% hielo, 17% blanco.
   const pickColor = () => {
      const r = Math.random();
      if (r < 0.6674226804123711) return [100, 255, 218];
      if (r < 0.83) return [191, 253, 243];
      return [255, 255, 255];
   };

   const pickFarColor = () => {
      const r = Math.random();
      if (r < 0.9) return [255, 255, 255]; // casi siempre blanco
      return [191, 253, 243]; // a veces hielo suave
   };

   const resizeCanvas = () => {
      const r = host.getBoundingClientRect();
      w = Math.max(1, Math.floor(r.width));
      h = Math.max(1, Math.floor(r.height));
      dpr = window.devicePixelRatio || 1;

      canvas.width = Math.floor(w * dpr);
      canvas.height = Math.floor(h * dpr);
      canvas.style.width = `${w}px`;
      canvas.style.height = `${h}px`;

      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
   };

   const buildStars = () => {
      stars = [];
      updateOrigin();
      updateFooterCutWorld();

      const maxWorld = Math.max(1, Math.min(worldHeight(), footerCutWorld));
      const area = w * h;

      let baseCount = Math.floor((area / 900) * STAR_DENSITY);
      baseCount = clamp(baseCount, MIN_STARS, MAX_STARS);

      // distribuimos por todo el WORLD (hasta el footer)
      const sigmaSpawn = w < 700 ? SIGMA_SPAWN_MOBILE : SIGMA_SPAWN_DESKTOP;

      for (let i = 0; i < baseCount; i++) {
         const layer = Math.random() < 0.65 ? 0 : Math.random() < 0.85 ? 1 : 2;

         // Tamaños originales por layer
         let radius =
            layer === 0 ? rand(0.35, 0.85) : layer === 1 ? rand(0.45, 1.05) : rand(0.55, 1.2);

         if (layer === 2 && Math.random() < 0.15) {
            radius *= 1.8;
         }

         const baseA =
            layer === 0 ? rand(0.1, 0.26) : layer === 1 ? rand(0.12, 0.3) : rand(0.16, 0.42);

         const sp = layer === 0 ? rand(10, 22) : layer === 1 ? rand(16, 30) : rand(22, 38);

         const yWorld = Math.random() * maxWorld;
         let x;

         if (Math.random() < DENSE_RATIO) {
            const cx = streamXAtY(yWorld, 0);
            x = cx + randn() * sigmaSpawn;
         } else {
            x = Math.random() * w;
         }

         x = ((x % w) + w) % w;

         stars.push({
            x,
            y: yWorld, // WORLD y
            r: radius,
            a: baseA,
            sp,
            phase: Math.random() * Math.PI * 2,
            col: pickColor(),
         });
      }
   };

   let lastMeasuredWorldH = 0;

   const maybeRebuildForHeightChange = () => {
      updateFooterCutWorld();
      const m = Math.max(1, Math.min(worldHeight(), footerCutWorld));
      if (!lastMeasuredWorldH) {
         lastMeasuredWorldH = m;
         return;
      }
      const rel = Math.abs(m - lastMeasuredWorldH) / lastMeasuredWorldH;
      if (rel > 0.12) {
         lastMeasuredWorldH = m;
         buildStars();
      }
   };

   const step = (now) => {
      const dt = Math.min(0.04, (now - lastT) / 1000);
      lastT = now;

      const st = scrollTop();

      updateOrigin();
      updateFooterCutWorld();

      const cutScreen = footerCutWorld - st; // borde del footer en coords pantalla

      ctx.clearRect(0, 0, w, h);

      const t = now / 1000;
      const sigmaW = w < 700 ? 105 : 150;
      const sigmaRespawn = w < 700 ? SIGMA_SPAWN_MOBILE : SIGMA_SPAWN_DESKTOP;

      const maxWorld = Math.max(1, Math.min(worldHeight(), footerCutWorld));

      for (let i = 0; i < stars.length; i++) {
         const s = stars[i];

         // movimiento propio
         const waveMove = Math.sin((s.y - st) * 0.013 + t * 1.25 + s.phase) * (w < 700 ? 14 : 18);
         s.x += s.sp * 0.55 * dt + waveMove * dt;
         s.y += s.sp * dt;

         // wrap world y (no depende del viewport -> no “cortes” al subir rápido)
         if (s.y > maxWorld + 80) {
            s.y = -rand(0, 120);
            const cx = streamXAtY(s.y, t);
            s.x = (((cx + randn() * sigmaRespawn) % w) + w) % w;
            s.phase = Math.random() * Math.PI * 2;
         }

         // wrap x
         if (s.x > w + 40) s.x = -40;
         if (s.x < -40) s.x = w + 40;

         const yScreen = s.y - st;

         // fuera del viewport
         if (yScreen < -80) continue;
         if (yScreen > h + 80) continue;

         // no invadir footer
         if (yScreen >= cutScreen) continue;

         // corriente y brillo
         const cx2 = streamXAtY(s.y, t);
         const d = Math.abs(s.x - cx2);
         const weight = Math.exp(-(d * d) / (2 * sigmaW * sigmaW));

         const tw = 0.86 + 0.14 * Math.sin(t * 2.0 + s.phase);

         const alpha = s.a * (0.22 + 0.95 * weight) * tw;
         const alphaBoost = Math.min(1, alpha * (1 + 2.2 * weight));

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

      if (!reduceMotion) rafId = requestAnimationFrame(step);
   };

   const schedule = (() => {
      let queued = false;
      return () => {
         if (queued) return;
         queued = true;
         requestAnimationFrame(() => {
            queued = false;
            resizeCanvas();
            buildStars();
         });
      };
   })();

   window.addEventListener("resize", schedule, { passive: true });
   scrollerEl.addEventListener(
      "scroll",
      () => {
         // solo para mantener coherente origin/footer cut y detectar cambios de altura
         maybeRebuildForHeightChange();
      },
      { passive: true },
   );

   // init
   resizeCanvas();
   updateOrigin();
   updateFooterCutWorld();
   buildStars();

   lastMeasuredWorldH = Math.max(1, Math.min(worldHeight(), footerCutWorld));

   // algunos checks de arranque (montaje/scrollHeight)
   let checks = 0;
   const bootCheck = setInterval(() => {
      maybeRebuildForHeightChange();
      checks += 1;
      if (checks >= 10) clearInterval(bootCheck);
   }, 600);

   setTimeout(maybeRebuildForHeightChange, 250);
   setTimeout(maybeRebuildForHeightChange, 1200);

   if (!reduceMotion) {
      rafId = requestAnimationFrame(step);
   } else {
      lastT = performance.now();
      step(lastT);
      cancelAnimationFrame(rafId);
   }
})();
