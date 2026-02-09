(() => {
   const root = document.getElementById("preloader");
   if (!root) return;

   const pctEl = document.getElementById("pl-pct");
   const bar = root.querySelector(".ring__bar");
   const lines = Array.from(root.querySelectorAll(".pl-line"));

   const CIRC = 289;
   const MIN_TOTAL_MS = 4000; // mínimo visible aunque cargue “al toque”
   const DONE_HOLD_MS = 2000; // “Listo” mínimo 2s
   const FADE_MS = 900; // coincide con CSS

   let pct = 0;
   let target = 0;
   let finished = false;

   // Si el script carga tarde, esto evita quedar pegado en 90
   let loaded = document.readyState === "complete";

   const t0 = performance.now();

   function setActive(step) {
      lines.forEach((l) => l.classList.toggle("is-active", l.dataset.step === step));
   }

   function render() {
      const clamped = Math.max(0, Math.min(100, Math.round(pct)));

      if (pctEl) pctEl.textContent = String(clamped);

      if (bar) {
         const off = CIRC - CIRC * (clamped / 100);
         bar.style.strokeDashoffset = String(off);
      }

      if (clamped < 30) setActive("css");
      else if (clamped < 70) setActive("img");
      else if (clamped < 95) setActive("js");
      else setActive("done");
   }

   // Progreso suave: sube hasta 92 mientras no haya load.
   // Cuando hay load, completa lento hacia 100.
   function tick() {
      if (!loaded) {
         target = Math.min(92, target + (Math.random() * 5 + 1.5));
         pct += (target - pct) * 0.1;
      } else {
         target = 100;
         pct += (target - pct) * 0.08;

         // clave: fuerza cierre real cuando ya está loaded
         if (pct >= 99.0) pct = 100;
      }

      render();

      if (pct >= 100 && !finished) {
         finishSequence();
         return;
      }

      requestAnimationFrame(tick);
   }

   // Secuencia final con tiempos mínimos
   function finishSequence() {
      if (finished) return;
      finished = true;
      const now = performance.now();
      const elapsed = now - t0;

      const WAIT_MIN_TOTAL = Math.max(0, MIN_TOTAL_MS - elapsed);

      // tiempos que tú pediste:
      const SHOW_DONE_MS = 2000; // “Listo” visible 2s
      const AFTER_DONE_MS = 2000; // después de desaparecer, esperar 2s para mostrar la página

      setTimeout(() => {
         // 1) Mostrar “Listo” inmediatamente al terminar
         root.classList.add("is-done");

         // 2) Mantener “Listo” 2s, luego ocultar preloader
         setTimeout(() => {
            root.classList.add("is-hidden");

            // 3) 2s después de que se fue el preloader, recién mostrar la página + disparar animaciones
            setTimeout(() => {
               document.body.classList.remove("app-preloading");
               document.body.classList.add("app-ready");

               window.dispatchEvent(new Event("app:ready"));
            }, AFTER_DONE_MS);
         }, SHOW_DONE_MS);
      }, WAIT_MIN_TOTAL);
   }

   // Arranca animación
   requestAnimationFrame(tick);

   window.addEventListener(
      "load",
      () => {
         loaded = true;
      },
      { once: true },
   );
})();
