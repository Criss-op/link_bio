(() => {
  const isFinePointer = window.matchMedia("(pointer: fine)").matches;
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!isFinePointer || prefersReducedMotion) {
    return;
  }

  const wrap = document.getElementById("cris-avatar-wrap");
  const img = document.getElementById("cris-avatar");
  if (!wrap || !img) {
    return;
  }

  let raf = null;
  let rect = null;

  const reset = () => {
    img.style.transform = "translate3d(0, 0, 0) rotateX(0deg) rotateY(0deg)";
  };

  const applyTransform = (x, y) => {
    if (!rect) {
      rect = wrap.getBoundingClientRect();
    }
    const dx = x - rect.left - rect.width / 2;
    const dy = y - rect.top - rect.height / 2;
    const moveX = (dx / rect.width) * 12;
    const moveY = (dy / rect.height) * 12;
    const rotateY = (dx / rect.width) * 6;
    const rotateX = (-dy / rect.height) * 6;
    img.style.transform = `translate3d(${moveX}px, ${moveY}px, 0) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    raf = null;
  };

  const onMove = (event) => {
    const { clientX, clientY } = event;
    if (!raf) {
      raf = requestAnimationFrame(() => applyTransform(clientX, clientY));
    }
  };

  const onLeave = () => {
    rect = null;
    reset();
  };

  wrap.addEventListener("mousemove", onMove);
  wrap.addEventListener("mouseleave", onLeave);
  wrap.addEventListener("mouseenter", () => {
    rect = wrap.getBoundingClientRect();
  });
})();
