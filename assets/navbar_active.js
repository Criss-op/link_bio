(() => {
   const scroller =
      document.querySelector("#page-scroll") ||
      document.querySelector(".scroll-container") ||
      document.scrollingElement;

   if (!scroller) return;

   const HERO_LOCK_PX = 120; // arriba de esto: siempre "inicio"

   function boot(attempts = 120) {
      const navLinks = Array.from(document.querySelectorAll(".navbar-link")).filter((el) => {
         const href = el.getAttribute?.("href") || "";
         return href.includes("#"); // sirve para "/#inicio" y "#inicio"
      });

      const sections = Array.from(document.querySelectorAll(".section[id]"));

      if (!navLinks.length || !sections.length) {
         if (attempts > 0) requestAnimationFrame(() => boot(attempts - 1));
         return;
      }

      const getTargetId = (el) => {
         const href = el.getAttribute?.("href") || "";
         const i = href.indexOf("#");
         if (i === -1) return "";
         return href.slice(i + 1); // "/#contacto" -> "contacto"
      };

      const setActive = (id) => {
         navLinks.forEach((el) => {
            el.classList.toggle("is-active", getTargetId(el) === id);
         });
      };

      // Estado inicial
      setActive("inicio");

      // Forzar "inicio" al volver arriba (no dependas del observer)
      const onScroll = () => {
         const y = scroller.scrollTop || 0;
         if (y <= HERO_LOCK_PX) setActive("inicio");
      };

      scroller.addEventListener("scroll", onScroll, { passive: true });
      window.addEventListener("scroll", onScroll, { passive: true });

      // Observer para secciones: decide activo cuando ya saliste del hero
      const io = new IntersectionObserver(
         (entries) => {
            const y = scroller.scrollTop || 0;
            if (y <= HERO_LOCK_PX) {
               setActive("inicio");
               return;
            }

            const visible = entries
               .filter((e) => e.isIntersecting)
               .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

            if (visible?.target?.id) setActive(visible.target.id);
         },
         {
            root: scroller === document.scrollingElement ? null : scroller,
            threshold: [0.25, 0.4, 0.55, 0.7],
            rootMargin: "-25% 0px -60% 0px",
         },
      );

      sections.forEach((s) => io.observe(s));
   }

   if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", () => boot(), { once: true });
   } else {
      boot();
   }
})();
