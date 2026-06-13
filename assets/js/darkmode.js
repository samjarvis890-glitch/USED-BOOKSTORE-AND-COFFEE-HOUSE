/* ==========================================================================
   USED BOOKSTORE & COFFEE HOUSE - DARK MODE MODULE v3.0 (darkmode.js)
   Handles data-theme="dark" for main pages + syncs with login/register
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  const darkModeToggle = document.getElementById('darkModeToggle');

  /* ── Apply saved theme on page load ── */
  const currentTheme = localStorage.getItem('theme') || 'light';
  applyTheme(currentTheme === 'dark');

  /* ── Toggle on button click ── */
  if (darkModeToggle) {
    darkModeToggle.addEventListener('click', () => {
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      applyTheme(!isDark);
      localStorage.setItem('theme', !isDark ? 'dark' : 'light');
    });
  }

  function applyTheme(isDark) {
    if (isDark) {
      document.documentElement.setAttribute('data-theme', 'dark');
    } else {
      document.documentElement.removeAttribute('data-theme');
    }
    updateIcon(isDark);
  }

  function updateIcon(isDark) {
    if (!darkModeToggle) return;
    const icon = darkModeToggle.querySelector('i');
    if (icon) {
      icon.className = isDark ? 'fas fa-sun' : 'far fa-moon';
    }
    // Update text label if present (e.g. ltrToggleBtn-style button)
    const span = darkModeToggle.querySelector('span');
    if (span) {
      span.textContent = isDark ? 'Light' : 'Dark';
    }
  }

});
