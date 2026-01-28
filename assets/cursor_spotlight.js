(() => {
  const isFinePointer = window.matchMedia("(pointer: fine)").matches;
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!isFinePointer || prefersReducedMotion) {
    return;
  }

  const root = document.documentElement;
  let raf = null;
  let targetX = window.innerWidth / 2;
  let targetY = window.innerHeight / 3;

  const update = () => {
    root.style.setProperty("--mx", `${targetX}px`);
    root.style.setProperty("--my", `${targetY}px`);
    raf = null;
  };

  const onMove = (event) => {
    targetX = event.clientX;
    targetY = event.clientY;
    if (!raf) {
      raf = requestAnimationFrame(update);
    }
  };

  window.addEventListener("mousemove", onMove);
})();
