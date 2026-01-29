(() => {
  const root = document.documentElement;
  const scrollContainer = document.getElementById("page-scroll");
  if (!scrollContainer) {
    return;
  }

  const hero = document.getElementById("inicio");
  const profile = document.getElementById("perfil");
  const footer = document.getElementById("footer");
  if (!hero) {
    return;
  }

  root.dataset.inHero = "true";

  let inHero = true;
  let isSnapping = false;

  const setHeroState = (isVisible) => {
    inHero = isVisible;
    root.dataset.inHero = isVisible ? "true" : "false";
  };

  const heroObserver = new IntersectionObserver(
    ([entry]) => {
      setHeroState(entry.isIntersecting);
    },
    {
      root: scrollContainer,
      threshold: 0.4,
    },
  );

  heroObserver.observe(hero);

  if (footer) {
    const footerObserver = new IntersectionObserver(
      ([entry]) => {
        root.dataset.inFooter = entry.isIntersecting ? "true" : "false";
      },
      {
        root: scrollContainer,
        threshold: 0.4,
      },
    );
    footerObserver.observe(footer);
  }

  const snapToProfile = () => {
    if (!profile || isSnapping) {
      return;
    }
    isSnapping = true;
    profile.scrollIntoView({ behavior: "smooth", block: "start" });
    window.setTimeout(() => {
      isSnapping = false;
    }, 700);
  };

  const onWheel = (event) => {
    if (!inHero) {
      return;
    }
    if (event.deltaY > 0) {
      event.preventDefault();
      snapToProfile();
    }
  };

  let touchStartY = 0;
  const onTouchStart = (event) => {
    touchStartY = event.touches[0].clientY;
  };

  const onTouchEnd = (event) => {
    if (!inHero) {
      return;
    }
    const touchEndY = event.changedTouches[0].clientY;
    if (touchStartY - touchEndY > 40) {
      snapToProfile();
    }
  };

  scrollContainer.addEventListener("wheel", onWheel, { passive: false });
  scrollContainer.addEventListener("touchstart", onTouchStart, { passive: true });
  scrollContainer.addEventListener("touchend", onTouchEnd, { passive: true });
})();
