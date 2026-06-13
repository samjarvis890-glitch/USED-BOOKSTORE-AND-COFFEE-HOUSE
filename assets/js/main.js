/* ==========================================================================
   USED BOOKSTORE & COFFEE HOUSE - PAGE SPECIFIC INTERACTIVITY (main.js)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {

  // ==================== 1. BOOKS PAGE: Live Search & Filter ====================
  const searchInput = document.getElementById('bookSearchInput');
  const genreFilter = document.getElementById('genreFilter');
  const bookGridItems = document.querySelectorAll('.books-grid-container .book-card');

  function filterBooks() {
    if (!searchInput && !genreFilter) return;
    
    const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const selectedGenre = genreFilter ? genreFilter.value.toLowerCase() : 'all';

    bookGridItems.forEach(card => {
      const title = card.querySelector('h3').textContent.toLowerCase();
      const author = card.querySelector('p').textContent.toLowerCase();
      const genre = card.getAttribute('data-genre').toLowerCase();

      const matchesSearch = title.includes(query) || author.includes(query);
      const matchesGenre = selectedGenre === 'all' || genre === selectedGenre;

      if (matchesSearch && matchesGenre) {
        card.parentElement.style.display = 'block';
        card.style.opacity = '1';
        card.style.transform = 'scale(1)';
      } else {
        card.parentElement.style.display = 'none';
      }
    });
  }

  if (searchInput) searchInput.addEventListener('input', filterBooks);
  if (genreFilter) genreFilter.addEventListener('change', filterBooks);


  // ==================== 2. CAFE PAGE: Interactive Menu Tabs ====================
  const menuTabs = document.querySelectorAll('.cafe-menu-tabs button');
  const menuSections = document.querySelectorAll('.menu-category-section');

  if (menuTabs.length > 0 && menuSections.length > 0) {
    menuTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        // Remove active class from all tabs
        menuTabs.forEach(t => t.classList.remove('bg-[#6F4E37]', 'text-white'));
        menuTabs.forEach(t => t.classList.add('bg-[#EADBC8]', 'text-[#6F4E37]'));
        
        // Add active class to clicked tab
        tab.classList.remove('bg-[#EADBC8]', 'text-[#6F4E37]');
        tab.classList.add('bg-[#6F4E37]', 'text-white');

        const category = tab.getAttribute('data-category');

        menuSections.forEach(section => {
          if (category === 'all' || section.id === `menu-${category}`) {
            section.style.display = 'block';
            setTimeout(() => {
              section.style.opacity = '1';
            }, 50);
          } else {
            section.style.display = 'none';
            section.style.opacity = '0';
          }
        });
      });
    });
  }


  // ==================== 3. TRADE-IN PAGE: Credit Calculator ====================
  const calcBtn = document.getElementById('calcCreditBtn');
  const calcResult = document.getElementById('calcResultBox');

  if (calcBtn) {
    calcBtn.addEventListener('click', () => {
      const category = document.getElementById('calcCategory').value;
      const condition = document.getElementById('calcCondition').value;
      const quantity = parseInt(document.getElementById('calcQuantity').value) || 0;

      if (quantity <= 0) {
        alert('Please enter a valid quantity of books.');
        return;
      }

      // Base Rates
      let rate = 2.00; // default base rate
      if (category === 'textbook') rate = 5.00;
      if (category === 'collectible') rate = 8.00;
      if (category === 'fiction') rate = 3.00;

      // Condition Multiplier
      let multiplier = 1.0;
      if (condition === 'new') multiplier = 1.5;
      if (condition === 'likenew') multiplier = 1.2;
      if (condition === 'good') multiplier = 1.0;
      if (condition === 'fair') multiplier = 0.5;

      const estimatedCredit = rate * multiplier * quantity;
      
      if (calcResult) {
        calcResult.innerHTML = `
          <div class="p-4 bg-[#FAF7F2] rounded-2xl border-2 border-[#C4A484] text-center">
            <p class="text-sm text-gray-500 uppercase font-semibold">Estimated Store Credit</p>
            <h4 class="text-3xl font-bold text-[#6F4E37] mt-1">$${estimatedCredit.toFixed(2)}</h4>
            <p class="text-xs text-[#3D8B5C] mt-2 font-medium">✨ Plus a FREE coffee voucher for trading today!</p>
          </div>
        `;
        calcResult.style.opacity = '0';
        calcResult.style.display = 'block';
        setTimeout(() => {
          calcResult.style.opacity = '1';
          calcResult.style.transform = 'translateY(0)';
        }, 100);
      }
    });
  }


  // ==================== 4. LOYALTY PAGE: Punch Card Simulator ====================
  const punchBtn = document.getElementById('addStampBtn');
  const stampSlots = document.querySelectorAll('.punch-stamp-slot');
  const punchStatusText = document.getElementById('punchStatusText');
  let stampsCount = 0;

  if (punchBtn && stampSlots.length > 0) {
    punchBtn.addEventListener('click', () => {
      if (stampsCount < 10) {
        const slot = stampSlots[stampsCount];
        slot.innerHTML = '<i class="fas fa-mug-hot text-2xl text-[#6F4E37] animate-bounce"></i>';
        slot.classList.add('bg-[#EADBC8]', 'border-[#6F4E37]');
        stampsCount++;

        if (punchStatusText) {
          punchStatusText.textContent = `${stampsCount} / 10 Stamps Collected`;
        }

        if (stampsCount === 10) {
          punchBtn.disabled = true;
          punchBtn.innerHTML = '<i class="fas fa-gift me-2"></i>Reward Ready!';
          punchBtn.classList.remove('bg-[#6F4E37]');
          punchBtn.classList.add('bg-[#3D8B5C]');
          
          setTimeout(() => {
            alert('🎉 Congratulations! You have filled your card! Show this screen to the barista to claim your FREE specialty latte!');
          }, 400);
        }
      }
    });
  }


  // ==================== 5. FORM SUBMISSIONS (Newsletter, Contact, Auth) ====================
  const newsletterForm = document.getElementById('footerNewsletter');
  if (newsletterForm) {
    newsletterForm.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('✨ Welcome to the Book Club! Check your inbox soon for premium offers and event news.');
      newsletterForm.reset();
    });
  }

  const contactForm = document.getElementById('contactFormMain');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('📬 Message sent successfully! Our coffee lounge curators will get back to you shortly.');
      contactForm.reset();
    });
  }

  const loginForm = document.getElementById('loginForm');
  if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('🔐 Welcome back to Pages & Perks! Redirecting to your dashboard mock...');
      window.location.href = 'index.html';
    });
  }

  const registerForm = document.getElementById('registerForm');
  if (registerForm) {
    registerForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const pwd = document.getElementById('regPassword').value;
      const confirmPwd = document.getElementById('regConfirmPassword').value;

      if (pwd !== confirmPwd) {
        alert('❌ Passwords do not match. Please verify your password entry.');
        return;
      }

      alert('🎉 Registration successful! Welcome to the family. Logging you in...');
      window.location.href = 'index.html';
    });
  }
});
