(() => {
   const $ = (sel, root = document) => root.querySelector(sel);

   function initWheelToHorizontal(viewport) {
      if (!viewport) return;

      // Convierte rueda vertical en scroll horizontal SOLO cuando el cursor está encima.
      const onWheel = (e) => {
         if (!viewport.matches(":hover")) return;
         if (viewport.scrollWidth <= viewport.clientWidth) return;

         // Si el dispositivo ya manda deltaX (trackpad/horizontal wheel), no lo estorbes.
         if (Math.abs(e.deltaX) > Math.abs(e.deltaY)) return;

         e.preventDefault();
         const speed = 1.2;
         viewport.scrollLeft += e.deltaY * speed;
      };

      viewport.addEventListener("wheel", onWheel, { passive: false });

      // Drag-to-scroll (mouse)
      let isDown = false;
      let startX = 0;
      let startScrollLeft = 0;

      const onDown = (e) => {
         // solo botón izquierdo
         if (e.pointerType === "mouse" && e.button !== 0) return;
         isDown = true;
         startX = e.clientX;
         startScrollLeft = viewport.scrollLeft;
         viewport.setPointerCapture?.(e.pointerId);
         viewport.classList.add("is-dragging");
      };

      const onMove = (e) => {
         if (!isDown) return;
         const dx = e.clientX - startX;
         viewport.scrollLeft = startScrollLeft - dx;
      };

      const onUp = (e) => {
         if (!isDown) return;
         isDown = false;
         viewport.releasePointerCapture?.(e.pointerId);
         viewport.classList.remove("is-dragging");
      };

      viewport.addEventListener("pointerdown", onDown);
      viewport.addEventListener("pointermove", onMove);
      viewport.addEventListener("pointerup", onUp);
      viewport.addEventListener("pointercancel", onUp);
      viewport.addEventListener("pointerleave", onUp);
   }

   function initOverlay() {
      const overlay = $("#edu-overlay");
      if (!overlay) return;

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

   function boot() {
      const viewport = document.querySelector(".edu-viewport");
      initWheelToHorizontal(viewport);
      initOverlay();
   }

   if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", boot);
   } else {
      boot();
   }
})();
