(() => {
   const root = document.documentElement;
   if (root.dataset.railsDockInit === "true") return;
   root.dataset.railsDockInit = "true";

   const scrollContainer = document.getElementById("page-scroll");
   const footer = document.getElementById("footer");
   if (!scrollContainer || !footer) return;

   let ticking = false;

   const compute = () => {
      ticking = false;

      const scRect = scrollContainer.getBoundingClientRect();
      const fr = footer.getBoundingClientRect();

      // Cuánto “invade” el footer desde abajo del viewport del scrollContainer
      const overlap = Math.max(0, scRect.bottom - fr.top);

      // Evita valores absurdos si el footer ocupa casi toda la pantalla
      const value = Math.min(overlap, scRect.height);

      root.style.setProperty("--rails-bottom", `${Math.ceil(value)}px`);
   };

   const request = () => {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(compute);
   };

   // init
   request();

   scrollContainer.addEventListener("scroll", request, { passive: true });
   window.addEventListener("resize", request);

   // Si el footer cambia de alto dinámicamente
   if (window.ResizeObserver) {
      const ro = new ResizeObserver(request);
      ro.observe(footer);
   }
})();
