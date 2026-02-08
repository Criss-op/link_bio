(() => {
   const $ = (sel, root = document) => root.querySelector(sel);

   let _eduRaf = 0;
   let _eduDeskRaf = 0;

   function scheduleEduLayout() {
      cancelAnimationFrame(_eduRaf);
      _eduRaf = requestAnimationFrame(() => {
         // 1er frame: layout básico
         layoutMobileLine?.();
         layoutDesktopGeometry?.();

         // 2do frame: asegura medidas finales (muy típico con fuentes/scrollbar)
         requestAnimationFrame(() => {
            layoutMobileLine?.();
            layoutDesktopGeometry?.();
         });
      });
   }

   function initWheelToHorizontal(viewport) {
      if (!viewport) return;

      // DESACTIVADO a propósito:
      // - No convertir rueda vertical a scroll horizontal.
      // - No drag-to-scroll.
      //
      // Queda solo:
      // - scroll horizontal nativo (rueda horizontal / trackpad deltaX)
      // - arrastre de la barra inferior.
   }

   function initOverlay() {
      const overlay = $("#edu-overlay");
      if (!overlay) return;

      // Evita problemas de clipping/stacking context dentro de contenedores con overflow.
      if (overlay.parentElement !== document.body) {
         document.body.appendChild(overlay);
      }

      const closeBtn = $("#edu-overlay-close", overlay);
      const oType = $("#edu-o-type", overlay);
      const oTitle = $("#edu-o-title", overlay);
      const oOrg = $("#edu-o-org", overlay);
      const oYear = $("#edu-o-year", overlay);
      const oLogo = $("#edu-o-logo", overlay);
      const oBullets = $("#edu-o-bullets", overlay);

      const close = () => {
         overlay.classList.remove("is-open");
         document.documentElement.classList.remove("edu-modal-open");
         document.body.classList.remove("edu-modal-open");
      };

      const openFromCard = (card) => {
         const d = card.dataset || {};
         const type = d.type || "";
         const title = d.title || "";
         const org = d.org || "";
         const year = d.year || "";
         const logo = d.logo || "";

         let bullets = [];
         try {
            bullets = JSON.parse(d.bullets || "[]");
         } catch {
            bullets = [];
         }

         if (oType) oType.textContent = type;
         if (oTitle) oTitle.textContent = title;
         if (oOrg) oOrg.textContent = org;
         if (oYear) oYear.textContent = year;

         if (oLogo) {
            if (logo) oLogo.src = logo;
            oLogo.alt = org || title || "Logo";
         }

         if (oBullets) {
            oBullets.innerHTML = "";
            bullets.slice(0, 4).forEach((b) => {
               const li = document.createElement("li");
               li.textContent = b;
               oBullets.appendChild(li);
            });
         }

         overlay.classList.add("is-open");
         document.documentElement.classList.add("edu-modal-open");
         document.body.classList.add("edu-modal-open");
      };

      // Delegación: click en cualquier card
      document.addEventListener("click", (e) => {
         const viewport = document.querySelector(".edu-viewport");
         const suppressUntil = Number(viewport?.dataset?.eduSuppressClick || 0);
         if (suppressUntil && Date.now() < suppressUntil) return;

         const card = e.target.closest?.(".edu-card");
         if (card) {
            openFromCard(card);
            return;
         }

         // click fuera del panel => cierra
         if (e.target === overlay) close();
      });

      // Teclado (Enter/Espacio sobre card)
      document.addEventListener("keydown", (e) => {
         if (e.key === "Escape") close();

         const active = document.activeElement;
         const isCard = active && active.classList && active.classList.contains("edu-card");
         if (!isCard) return;

         if (e.key === "Enter" || e.key === " ") {
            e.preventDefault();
            openFromCard(active);
         }
      });

      closeBtn?.addEventListener("click", close);
   }

   // MOBILE: ajusta la línea vertical para que empiece/termine exactamente en los nodos.
   function layoutMobileLine() {
      const list = document.querySelector(".edu-mobile-list");
      if (!list) return;

      const items = Array.from(list.querySelectorAll(".edu-m-item"));
      if (!items.length) return;

      const listRect = list.getBoundingClientRect();

      const getNodeY = (item) => {
         const summary = item.querySelector("summary");
         if (!summary) return null;
         const r = summary.getBoundingClientRect();
         // El nodo está en el centro del summary (50%)
         return r.top + r.height / 2 - listRect.top;
      };

      const startY = getNodeY(items[0]);
      const endY = getNodeY(items[items.length - 1]);
      if (startY == null || endY == null) return;

      const h = list.clientHeight;

      // Ajuste óptico mínimo (si quieres 0, déjalo en 0)
      const TRIM = 0;

      list.style.setProperty("--edu-m-line-top", `${Math.max(0, startY + TRIM)}px`);
      list.style.setProperty("--edu-m-line-bottom", `${Math.max(0, h - (endY - TRIM))}px`);
   }

   // DESKTOP: asegura que las cards queden completamente arriba/abajo y que el nodo caiga sobre la línea.
   function layoutDesktopGeometry() {
      const track = document.querySelector(".edu-track");
      if (!track) return;

      // Solo md+
      const isDesktop = window.matchMedia && window.matchMedia("(min-width: 768px)").matches;
      if (!isDesktop) return;

      // Si el contenedor desktop aún no está visible, no calcules (evita mediciones falsas)
      const desktopWrap = document.querySelector(".edu-desktop");
      if (desktopWrap && desktopWrap.offsetParent === null) return;

      const cards = Array.from(track.querySelectorAll(".edu-card"));
      if (!cards.length) return;

      // 1) Setear Y dinámico
      const GAP = 26;
      cards.forEach((card) => {
         const h = card.offsetHeight || 0;
         const isTop = card.classList.contains("edu-card--top");
         const y = (h / 2 + GAP) * (isTop ? -1 : 1);
         card.style.setProperty("--edu-y", `${y}px`);
      });

      track.classList.add("edu-has-dyn");

      // 2) En el siguiente frame medir y alinear nodos/conectores
      cancelAnimationFrame(_eduDeskRaf);
      _eduDeskRaf = requestAnimationFrame(() => {
         const trackRect = track.getBoundingClientRect();

         // Usa clientHeight (más consistente con top:50% del pseudo-elemento)
         const lineY = trackRect.top + track.clientHeight / 2;

         const DOT_R = 6; // 12px/2

         cards.forEach((card) => {
            const rect = card.getBoundingClientRect();
            const h = card.offsetHeight || 0;
            const isTop = card.classList.contains("edu-card--top");

            const nodeCenterY = lineY - rect.top; // dentro del card
            const nodeTop = nodeCenterY - DOT_R;

            const edgeY = isTop ? h : 0;
            const connectorTop = Math.min(edgeY, nodeCenterY);
            const connectorH = Math.max(8, Math.abs(nodeCenterY - edgeY));

            card.style.setProperty("--edu-node-top", `${nodeTop}px`);
            card.style.setProperty("--edu-connector-top", `${connectorTop}px`);
            card.style.setProperty("--edu-connector-h", `${connectorH}px`);
         });
      });
   }

   function boot() {
      let didWheel = false;
      let didOverlay = false;
      let didMobileToggle = false;

      const raf = window.requestAnimationFrame || ((fn) => setTimeout(fn, 16));

      const poll = (n = 0) => {
         const viewport = document.querySelector(".edu-viewport");
         if (viewport && !didWheel) {
            initWheelToHorizontal(viewport);
            didWheel = true;
         }

         const overlay = document.querySelector("#edu-overlay");
         if (overlay && !didOverlay) {
            initOverlay();
            didOverlay = true;
         }

         // Mobile: escuchar toggles (solo una vez)
         if (!didMobileToggle) {
            const mobileItems = document.querySelectorAll(".edu-m-item");
            if (mobileItems && mobileItems.length) {
               mobileItems.forEach((d) => d.addEventListener?.("toggle", layoutMobileLine));
               didMobileToggle = true;
            }
         }

         scheduleEduLayout();

         // Reintenta un poco por si Reflex hidrata/monta después.
         if ((didWheel && didOverlay) || n > 120) return;
         raf(() => poll(n + 1));
      };

      poll();
      // Re-layout cuando cruzas breakpoints (mobile<->desktop / md<->lg)
      if (window.matchMedia) {
         const mqMd = window.matchMedia("(min-width: 768px)");
         const mqLg = window.matchMedia("(min-width: 1024px)");

         const onBp = () => {
            // pequeño delay para que el display:block/none se asiente
            setTimeout(scheduleEduLayout, 0);
            setTimeout(scheduleEduLayout, 60);
         };

         // Safari antiguo usa addListener
         mqMd.addEventListener?.("change", onBp) || mqMd.addListener?.(onBp);
         mqLg.addEventListener?.("change", onBp) || mqLg.addListener?.(onBp);
      }

      // Burst de estabilización post-montaje (caza el caso “se arregla al mover 1px”)
      [0, 60, 180, 420].forEach((ms) => setTimeout(scheduleEduLayout, ms));

      // Re-layout cuando fuentes estén listas (evita el bug de “se arregla al mover 1px”)
      if (document.fonts && document.fonts.ready) {
         document.fonts.ready.then(scheduleEduLayout).catch(() => {});
      }

      // Re-layout cuando los logos estén decodificados
      const imgs = Array.from(
         document.querySelectorAll(".edu-logo, .edu-overlay__logo, .edu-m-logo"),
      );
      Promise.all(
         imgs.map((img) => (img.decode ? img.decode().catch(() => {}) : Promise.resolve())),
      ).then(scheduleEduLayout);

      // Observa cambios de tamaño del viewport/track (reflows tardíos)
      const viewport = document.querySelector(".edu-viewport");
      const track = document.querySelector(".edu-track");
      if (window.ResizeObserver && (viewport || track)) {
         const ro = new ResizeObserver(() => scheduleEduLayout());
         if (viewport) ro.observe(viewport);
         if (track) ro.observe(track);
      }

      // Re-layout en resize
      window.addEventListener("resize", scheduleEduLayout);

      // Re-layout cuando termina de cargar todo (fonts / imágenes)
      window.addEventListener("load", scheduleEduLayout, { once: true });
   }

   if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", boot);
   } else {
      boot();
   }
})();
