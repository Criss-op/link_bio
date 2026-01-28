(() => {
  const root = document.documentElement;
  const scrollContainer = document.getElementById("page-scroll");
  if (!scrollContainer) {
    return;
  }

  const updateScrollState = () => {
    const scrolled = scrollContainer.scrollTop > 10;
    if (scrolled) {
      root.dataset.scrolled = "true";
    } else {
      delete root.dataset.scrolled;
    }
  };

  updateScrollState();
  scrollContainer.addEventListener("scroll", updateScrollState, { passive: true });
})();
