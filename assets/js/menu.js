/* ==========================================================================
   USED BOOKSTORE & COFFEE HOUSE — MENU & NAV MODULE v2.0 (menu.js)
   Hover dropdown nav with page-section scroll, active link, RTL/LTR
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {

  /* ── 1. NAVBAR SCROLL BEHAVIOR ── */
  const navbar = document.getElementById('mainNavbar');
  if (navbar) {
    const handleNavbarScroll = () => {
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      if (window.scrollY > 60) {
        navbar.classList.add('scrolled');
        navbar.style.backgroundColor = isDark
          ? 'rgba(17, 10, 8, 0.99)'
          : 'rgba(250, 247, 242, 0.99)';
        navbar.style.padding = '0.2rem 0';
      } else {
        navbar.classList.remove('scrolled');
        navbar.style.backgroundColor = isDark
          ? 'rgba(17, 10, 8, 0.97)'
          : 'rgba(250, 247, 242, 0.97)';
        navbar.style.padding = '0.6rem 0';
      }
    };
    window.addEventListener('scroll', handleNavbarScroll, { passive: true });
    handleNavbarScroll(); // run once on load
  }


  /* ── 2. ACTIVE NAVIGATION LINK HIGHLIGHTER ── */
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
  navLinks.forEach(link => {
    const linkHref = link.getAttribute('href');
    if (linkHref === currentPath || (currentPath === '' && linkHref === 'index.html')) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });


  /* ── 3. HOVER DROPDOWN — SECTION-SCROLL BEHAVIOR ── */
  // Map of page -> sections. When hovering a nav link and hovering a dropdown
  // section anchor, clicking scrolls to it (on that page) or navigates + scrolls.
  const pageMap = {
    'index.html':   [
      { label: 'Hero',         anchor: '#hero-section',         icon: 'fa-home' },
      { label: 'Featured Books', anchor: '#featured-books',     icon: 'fa-book' },
      { label: 'Coffee Experience', anchor: '#coffee-experience', icon: 'fa-mug-hot' },
      { label: 'Community',    anchor: '#community',            icon: 'fa-users' },
      { label: 'Events',       anchor: '#events-section',       icon: 'fa-calendar' },
      { label: 'Trade & Loyalty', anchor: '#cta-section',       icon: 'fa-star' },
    ],
    'about.html':   [
      { label: 'Our Story',    anchor: '#about-hero',           icon: 'fa-scroll' },
      { label: 'Timeline',     anchor: '#story-timeline',       icon: 'fa-timeline' },
      { label: 'Mission',      anchor: '#about-mission',        icon: 'fa-bullseye' },
      { label: 'Values',       anchor: '#about-values',         icon: 'fa-gem' },
      { label: 'Team',         anchor: '#about-team',           icon: 'fa-people-group' },
    ],
    'books.html':   [
      { label: 'Browse Books', anchor: '#books-hero',           icon: 'fa-book-open' },
      { label: 'Genres',       anchor: '#books-genres',         icon: 'fa-layer-group' },
      { label: 'Bestsellers',  anchor: '#books-bestsellers',    icon: 'fa-fire' },
      { label: 'Rare Editions', anchor: '#books-rare',          icon: 'fa-award' },
      { label: 'Search Shelf', anchor: '#search-preview-section', icon: 'fa-search' },
    ],
    'cafe.html':    [
      { label: 'Cafe Home',    anchor: '#cafe-hero',            icon: 'fa-mug-hot' },
      { label: 'Signature Drinks', anchor: '#signature-drinks', icon: 'fa-coffee' },
      { label: 'Full Menu',    anchor: '#cafe-menu',            icon: 'fa-list' },
      { label: 'Seating',      anchor: '#cafe-seating',         icon: 'fa-couch' },
      { label: 'Gallery',      anchor: '#cafe-gallery',         icon: 'fa-images' },
    ],
    'events.html':  [
      { label: 'Events Home',  anchor: '#events-hero',          icon: 'fa-calendar-star' },
      { label: 'Upcoming',     anchor: '#upcoming-events',      icon: 'fa-clock' },
      { label: 'Workshops',    anchor: '#workshops',            icon: 'fa-chalkboard' },
      { label: 'Community',    anchor: '#events-community',     icon: 'fa-handshake' },
    ],
    'tradein.html': [
      { label: 'Trade-In Home', anchor: '#tradein-hero',        icon: 'fa-arrow-right-arrow-left' },
      { label: 'How It Works', anchor: '#tradein-steps',        icon: 'fa-list-ol' },
      { label: 'Categories',   anchor: '#tradein-categories',   icon: 'fa-tags' },
      { label: 'Calculator',   anchor: '#credit-calculator',    icon: 'fa-calculator' },
    ],
    'loyalty.html': [
      { label: 'Loyalty Home', anchor: '#loyalty-hero',         icon: 'fa-crown' },
      { label: 'Stamp Card',   anchor: '#punch-card',           icon: 'fa-stamp' },
      { label: 'Rewards',      anchor: '#loyalty-rewards',      icon: 'fa-gift' },
      { label: 'VIP Ranks',    anchor: '#loyalty-ranks',        icon: 'fa-medal' },
    ],
    'contact.html': [
      { label: 'Contact',      anchor: '#contact-hero',         icon: 'fa-envelope' },
      { label: 'Get In Touch', anchor: '#contact-form-section', icon: 'fa-paper-plane' },
      { label: 'Location',     anchor: '#store-location',       icon: 'fa-map-pin' },
      { label: 'Hours',        anchor: '#opening-hours',        icon: 'fa-clock' },
    ],
  };

  // Map nav link hrefs to their dropdown config
  const navLinkPageMap = {};

  // Build dropdown menus dynamically
  navLinks.forEach(link => {
    const linkText = link.textContent.trim();
    const targetPage = navLinkPageMap[linkText];
    if (!targetPage || !pageMap[targetPage]) return;

    const sections = pageMap[targetPage];
    const navItem = link.closest('.nav-item');
    if (!navItem) return;

    navItem.classList.add('has-dropdown');

    const dropdown = document.createElement('div');
    dropdown.className = 'nav-dropdown';
    dropdown.setAttribute('role', 'menu');

    const arrow = document.createElement('div');
    arrow.className = 'nav-dropdown-arrow';
    dropdown.appendChild(arrow);

    sections.forEach(section => {
      const a = document.createElement('a');
      a.href = `${targetPage}${section.anchor}`;
      a.innerHTML = `<i class="fas ${section.icon}"></i> ${section.label}`;
      a.setAttribute('role', 'menuitem');

      a.addEventListener('click', (e) => {
        e.preventDefault();
        const isCurrentPage = currentPath === targetPage || 
          (currentPath === '' && targetPage === 'index.html');

        if (isCurrentPage) {
          // Same page: smooth scroll
          const target = document.querySelector(section.anchor);
          if (target) {
            const navH = navbar ? navbar.offsetHeight : 80;
            const top = target.getBoundingClientRect().top + window.scrollY - navH - 12;
            window.scrollTo({ top, behavior: 'smooth' });
          }
        } else {
          // Different page: navigate with anchor
          window.location.href = `${targetPage}${section.anchor}`;
        }
      });

      dropdown.appendChild(a);
    });

    navItem.appendChild(dropdown);

    // Touch-friendly: toggle on tap
    let isMobile = () => window.innerWidth < 992;
    link.addEventListener('click', (e) => {
      if (isMobile()) {
        const isOpen = dropdown.classList.contains('mobile-open');
        // Close all other dropdowns
        document.querySelectorAll('.nav-dropdown.mobile-open').forEach(d => {
          d.classList.remove('mobile-open');
        });
        if (!isOpen) {
          e.preventDefault();
          dropdown.classList.add('mobile-open');
        }
      }
    });
  });

  // Handle anchor scrolling on page load (if navigated with #anchor)
  if (window.location.hash) {
    setTimeout(() => {
      const target = document.querySelector(window.location.hash);
      if (target) {
        const navH = navbar ? navbar.offsetHeight : 80;
        const top = target.getBoundingClientRect().top + window.scrollY - navH - 12;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    }, 400);
  }


  /* ── 4. MOBILE NAV AUTO-CLOSE ── */
  const navCollapse = document.getElementById('navbarMain');
  if (navCollapse && navbar) {
    // Close on nav-link clicks (that navigate to the page)
    const mobileLinks = navCollapse.querySelectorAll('.nav-link:not(.dropdown-toggle)');
    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        if (navCollapse.classList.contains('show')) {
          const inst = bootstrap.Collapse.getInstance(navCollapse)
            || new bootstrap.Collapse(navCollapse, { toggle: false });
          inst.hide();
        }
      });
    });

    // Close when clicking outside
    document.addEventListener('click', (e) => {
      if (!navbar.contains(e.target) && navCollapse.classList.contains('show')) {
        const inst = bootstrap.Collapse.getInstance(navCollapse)
          || new bootstrap.Collapse(navCollapse, { toggle: false });
        inst.hide();
      }
    });

    // Close on scroll > 30px
    window.addEventListener('scroll', () => {
      if (navCollapse.classList.contains('show') && window.scrollY > 30) {
        const inst = bootstrap.Collapse.getInstance(navCollapse)
          || new bootstrap.Collapse(navCollapse, { toggle: false });
        inst.hide();
      }
    }, { passive: true });
  }


  /* ── 5. LTR / RTL DIRECTION TOGGLE ── */
  const ltrToggleBtn = document.getElementById('ltrToggleBtn');
  const savedDir = localStorage.getItem('pp-dir') || 'ltr';
  setDirection(savedDir);

  if (ltrToggleBtn) {
    ltrToggleBtn.addEventListener('click', () => {
      const curr = document.documentElement.getAttribute('dir') || 'ltr';
      setDirection(curr === 'ltr' ? 'rtl' : 'ltr');
    });
  }

  function setDirection(dir) {
    document.documentElement.setAttribute('dir', dir);
    localStorage.setItem('pp-dir', dir);
    if (ltrToggleBtn) {
      // Update text nodes inside the button
      ltrToggleBtn.childNodes.forEach(n => {
        if (n.nodeType === 3 && n.textContent.trim()) {
          n.textContent = ' ' + (dir === 'rtl' ? 'RTL' : 'LTR');
        }
      });
      const icon = ltrToggleBtn.querySelector('i');
      if (icon) {
        icon.className = dir === 'rtl'
          ? 'fas fa-arrow-left-arrow-right'
          : 'fas fa-language';
      }
      ltrToggleBtn.title = dir === 'rtl' ? 'Switch to LTR' : 'Switch to RTL';
    }
  }


  /* ── 6. BACK TO TOP BUTTON ── */
  const backToTop = document.getElementById('backToTop');
  if (backToTop) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        backToTop.classList.add('visible');
      } else {
        backToTop.classList.remove('visible');
      }
    }, { passive: true });

    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

});
