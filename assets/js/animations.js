/* ==========================================================================
   USED BOOKSTORE & COFFEE HOUSE - ANIMATIONS MODULE (animations.js)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // Inject scroll reveal transition styles programmatically
  const style = document.createElement('style');
  style.innerHTML = `
    .scroll-reveal {
      opacity: 0;
      transform: translateY(30px);
      transition: opacity 0.8s cubic-bezier(0.25, 1, 0.5, 1), 
                  transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);
    }
    .scroll-reveal.revealed {
      opacity: 1;
      transform: translateY(0);
    }
    .delay-100 { transition-delay: 100ms; }
    .delay-200 { transition-delay: 200ms; }
    .delay-300 { transition-delay: 300ms; }
    .delay-400 { transition-delay: 400ms; }
  `;
  document.head.appendChild(style);

  // Setup Intersection Observer
  const revealElements = document.querySelectorAll('.scroll-reveal');
  const observerOptions = {
    root: null, // viewport
    rootMargin: '0px',
    threshold: 0.1 // triggers when 10% of element is visible
  };

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        // Stop observing once animated
        obs.unobserve(entry.target);
      }
    });
  }, observerOptions);

  revealElements.forEach(el => {
    observer.observe(el);
  });

  // Floating book mouse interaction (tilt effect for hero visual)
  const heroImage = document.querySelector('.hero-main-img');
  if (heroImage) {
    const parent = heroImage.parentElement;
    parent.addEventListener('mousemove', (e) => {
      const { width, height, left, top } = parent.getBoundingClientRect();
      const x = e.clientX - left - width / 2;
      const y = e.clientY - top - height / 2;
      const tiltX = (y / (height / 2)) * -10; // Max tilt 10deg
      const tiltY = (x / (width / 2)) * 10;
      
      heroImage.style.transform = `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) scale(1.02)`;
      heroImage.style.transition = 'transform 0.1s ease';
    });

    parent.addEventListener('mouseleave', () => {
      heroImage.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale(1)';
      heroImage.style.transition = 'transform 0.6s ease';
    });
  }
});
