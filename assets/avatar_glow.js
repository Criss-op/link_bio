function initAvatarGlow() {
   (() => {
      const reduceMotion = window.matchMedia?.("(prefers-reduced-motion: reduce)")?.matches;
      if (reduceMotion) return;

      const finePointer = window.matchMedia?.("(pointer: fine)")?.matches ?? true;
      if (!finePointer) return;

      const el = document.querySelector(".avatar-frame");
      if (!el) return;

      let rafId = null;
      let last = null;

      function clamp(v, a, b) {
         return Math.max(a, Math.min(b, v));
      }

      // suavizado (evita jitter)
      let sx = 60; // %
      let sy = 25; // %
      const SMOOTH = 0.18; // 0.1 más suave, 0.3 más rápido

      function setVars(clientX, clientY) {
         const r = el.getBoundingClientRect();

         const cx = r.left + r.width / 2;
         const cy = r.top + r.height / 2;

         const dx = clientX - cx;
         const dy = clientY - cy;

         // Distancia al rectángulo (0 si estás encima)
         const outX =
            clientX < r.left ? r.left - clientX : clientX > r.right ? clientX - r.right : 0;
         const outY =
            clientY < r.top ? r.top - clientY : clientY > r.bottom ? clientY - r.bottom : 0;
         const dOut = Math.hypot(outX, outY);

         // Umbral: cerca = modo preciso, lejos = modo por ángulo (suave)
         const THRESH = 90; // px (sube si quieres que use "preciso" desde más lejos)

         let ax, ay;

         if (dOut <= THRESH) {
            // Modo preciso (lo que te gusta cuando estás cerca)
            const xPct = ((clientX - r.left) / r.width) * 100;
            const yPct = ((clientY - r.top) / r.height) * 100;
            ax = clamp(xPct, 0, 100);
            ay = clamp(yPct, 0, 100);
         } else {
            // Modo estable (dirección/ángulo). Recorre el contorno sin saltos.
            const theta = Math.atan2(dy, dx); // -pi..pi
            ax = 50 + 50 * Math.cos(theta);
            ay = 50 + 50 * Math.sin(theta);
         }

         // Suavizado para evitar vibración
         sx = sx + (ax - sx) * SMOOTH;
         sy = sy + (ay - sy) * SMOOTH;

         el.style.setProperty("--ax", `${sx.toFixed(2)}%`);
         el.style.setProperty("--ay", `${sy.toFixed(2)}%`);

         // Intensidad constante (no se “pierde” de lejos)
         el.style.setProperty("--glow-o", "1");
         el.style.setProperty("--glow-gain", "1"); // si lo habías subido a 3, déjalo en 1 por ahora
      }

      function schedule(x, y) {
         last = { x, y };
         if (rafId) return;
         rafId = requestAnimationFrame(() => {
            rafId = null;
            if (!last) return;
            setVars(last.x, last.y);
         });
      }

      window.addEventListener("pointermove", (e) => schedule(e.clientX, e.clientY), {
         passive: true,
      });

      // Si sales de la ventana, no “apagues” (eso también se siente como pérdida)
      // Si igual quieres apagarlo, lo hacemos después con una caída suave.
   })();
}

window.addEventListener("app:ready", initAvatarGlow, { once: true });
