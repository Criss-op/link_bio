(() => {
  const root = document.documentElement;
  const scrollContainer = document.getElementById("page-scroll");
  if (!scrollContainer) {
    return;
  }

  const hero = document.getElementById("inicio");
  if (!hero) {
    return;
  }

  root.dataset.inHero = "true";

  const observer = new IntersectionObserver(
    ([entry]) => {
      root.dataset.inHero = entry.isIntersecting ? "true" : "false";
    },
    {
      root: scrollContainer,
      threshold: 0.4,
    },
  );

  observer.observe(hero);
})();
