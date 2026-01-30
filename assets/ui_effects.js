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

   // ESTADOS (faltaban)
   let inHero = true;
   let isSnapping = false;

   // Navbar/rails: "modo hero" solo cuando estás realmente arriba
   const HERO_TOP_PX = 120; // ajusta este número (80–160 suele ser lo correcto)

   const updateHeroTopState = () => {
      const atTop = scrollContainer.scrollTop <= HERO_TOP_PX;
      inHero = atTop;
      root.dataset.inHero = atTop ? "true" : "false";
   };

   updateHeroTopState();
   scrollContainer.addEventListener("scroll", updateHeroTopState, { passive: true });

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
