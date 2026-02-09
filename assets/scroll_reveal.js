function initScrollReveal() {
   (() => {
      const root = document.documentElement;
      if (root.dataset.srInit === "true") return;
      root.dataset.srInit = "true";

      // Respeta reduced motion
      const reduce =
         window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      if (reduce) return;

      const scroller = document.getElementById("page-scroll");
      if (!scroller) return;

      const waitForSR = (tries = 0) => {
         if (window.ScrollReveal) return init();
         if (tries > 90) return;
         requestAnimationFrame(() => waitForSR(tries + 1));
      };

      const init = () => {
         const sr = window.ScrollReveal({
            container: scroller, // viewport real del contenido
            reset: false,
            opacity: 0,
            distance: "18px",
            duration: 900,
            easing: "cubic-bezier(0.22, 1, 0.36, 1)",
            viewFactor: 0.25,
            viewOffset: { top: 0, right: 0, bottom: 80, left: 0 },
            mobile: true,
            cleanup: true,
         });

         // Helper: delay por elemento via data-sr-delay (custom_attrs en Reflex)
         const revealWithOptionalDelay = (baseSelector, baseOptions) => {
            const normalSelector = `${baseSelector}:not([data-sr-delay])`;
            const delayed = Array.from(document.querySelectorAll(`${baseSelector}[data-sr-delay]`));

            // Elementos sin delay: reveal normal (puede usar interval)
            if (document.querySelector(normalSelector)) {
               sr.reveal(normalSelector, baseOptions);
            }

            // Elementos con delay explícito: reveal individual
            delayed.forEach((el) => {
               const d = parseInt(el.getAttribute("data-sr-delay") || "0", 10) || 0;
               sr.reveal(el, { ...baseOptions, delay: d, interval: 0 });
            });
         };

         // 1) Base: fade-up (secuencia moderada)
         revealWithOptionalDelay(".sr-fade-up", {
            origin: "bottom",
            distance: "18px",
            duration: 900,
            scale: 0.985,
            interval: 120,
         });

         // 2) Cards: stagger
         revealWithOptionalDelay(".sr-card", {
            origin: "bottom",
            distance: "22px",
            duration: 950,
            scale: 0.985,
            interval: 110,
         });

         // 3) Fade puro
         revealWithOptionalDelay(".sr-fade", {
            distance: "0px",
            duration: 650,
         });
         // 4) Post-it: fade + dispara apertura del .postit interno
         revealWithOptionalDelay(".sr-postit", {
            distance: "0px",
            duration: 650,
            beforeReveal: (el) => {
               const note =
                  el.classList && el.classList.contains("postit")
                     ? el
                     : el.querySelector && el.querySelector(".postit");
               if (note && !note.classList.contains("is-open")) {
                  note.classList.add("is-open");
               }
            },
         });

         sr.sync();
      };

      waitForSR();
   })();
}

window.addEventListener("app:ready", initScrollReveal, { once: true });
