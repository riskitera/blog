/**
 * Riskitera Blog - Main JavaScript
 * Mobile menu, search modal (Ctrl+K), Fuse.js integration
 */
(function () {
  'use strict';

  // -------------------------------------------------------
  // Mobile menu toggle
  // -------------------------------------------------------
  const menuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const hamburgerIcon = document.getElementById('hamburger-icon');
  const closeIcon = document.getElementById('close-icon');

  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', function () {
      const isOpen = !mobileMenu.classList.contains('hidden');
      mobileMenu.classList.toggle('hidden');
      if (hamburgerIcon && closeIcon) {
        hamburgerIcon.classList.toggle('hidden', !isOpen);
        closeIcon.classList.toggle('hidden', isOpen);
      }
      menuBtn.setAttribute('aria-expanded', String(!isOpen));
    });
  }

  // -------------------------------------------------------
  // Search modal
  // -------------------------------------------------------
  const searchModal = document.getElementById('search-modal');
  const searchBackdrop = document.getElementById('search-backdrop');
  const searchInput = document.getElementById('search-input');
  const searchResults = document.getElementById('search-results');
  const searchEmpty = document.getElementById('search-empty');
  const searchBtn = document.getElementById('search-btn');
  const searchBtnMobile = document.getElementById('search-btn-mobile');

  function openSearch() {
    if (!searchModal) return;
    searchModal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    if (searchInput) {
      searchInput.value = '';
      searchInput.focus();
    }
    if (searchEmpty) searchEmpty.style.display = '';
    if (searchResults) {
      // Clear previous results but keep the empty hint
      var items = searchResults.querySelectorAll('.search-result-item');
      items.forEach(function (item) { item.remove(); });
    }
  }

  function closeSearch() {
    if (!searchModal) return;
    searchModal.classList.add('hidden');
    document.body.style.overflow = '';
  }

  // Open triggers
  if (searchBtn) searchBtn.addEventListener('click', openSearch);
  if (searchBtnMobile) searchBtnMobile.addEventListener('click', openSearch);

  // Close on backdrop click
  if (searchBackdrop) {
    searchBackdrop.addEventListener('click', closeSearch);
  }

  // Ctrl+K / Cmd+K shortcut
  document.addEventListener('keydown', function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      if (searchModal && searchModal.classList.contains('hidden')) {
        openSearch();
      } else {
        closeSearch();
      }
    }
    if (e.key === 'Escape') {
      closeSearch();
    }
  });

  // -------------------------------------------------------
  // Fuse.js search integration
  // -------------------------------------------------------
  var fuseInstance = null;
  var searchIndex = null;
  var indexLoading = false;

  function loadSearchIndex(callback) {
    if (searchIndex) {
      callback(searchIndex);
      return;
    }
    if (indexLoading) return;
    indexLoading = true;

    // Determine base URL from the <link rel="canonical"> or fallback
    var baseEl = document.querySelector('link[rel="canonical"]');
    var baseURL = baseEl ? new URL(baseEl.href).origin : '';

    // Try language-specific index first, fallback to root
    var lang = document.documentElement.lang || 'es';
    var indexURL = baseURL + '/' + lang + '/index.json';

    fetch(indexURL)
      .then(function (res) {
        if (!res.ok) {
          // Fallback to root index.json
          return fetch(baseURL + '/index.json');
        }
        return res;
      })
      .then(function (res) {
        if (!res.ok) throw new Error('Search index not found');
        return res.json();
      })
      .then(function (data) {
        searchIndex = data;
        indexLoading = false;
        callback(data);
      })
      .catch(function (err) {
        console.warn('Search index load failed:', err);
        indexLoading = false;
      });
  }

  function getFuse(data) {
    if (fuseInstance) return fuseInstance;
    if (typeof Fuse === 'undefined') {
      console.warn('Fuse.js not loaded');
      return null;
    }
    fuseInstance = new Fuse(data, {
      keys: [
        { name: 'title', weight: 0.4 },
        { name: 'description', weight: 0.2 },
        { name: 'content', weight: 0.2 },
        { name: 'tags', weight: 0.1 },
        { name: 'categories', weight: 0.1 }
      ],
      includeScore: true,
      includeMatches: true,
      threshold: 0.4,
      minMatchCharLength: 2,
      ignoreLocation: true
    });
    return fuseInstance;
  }

  function renderResults(results) {
    if (!searchResults) return;

    // Remove previous result items
    var items = searchResults.querySelectorAll('.search-result-item');
    items.forEach(function (item) { item.remove(); });

    if (!results || results.length === 0) {
      if (searchEmpty) {
        searchEmpty.style.display = '';
        searchEmpty.textContent = searchInput && searchInput.value.length > 0
          ? 'No results found.'
          : 'Type to search across all articles...';
      }
      return;
    }

    if (searchEmpty) searchEmpty.style.display = 'none';

    var fragment = document.createDocumentFragment();
    var max = Math.min(results.length, 10);

    for (var i = 0; i < max; i++) {
      var item = results[i].item;
      var el = document.createElement('a');
      el.href = item.permalink || item.url || '#';
      el.className = 'search-result-item block px-5 py-4 hover:bg-rk-card-hover border-b border-rk-border last:border-b-0 transition-colors no-underline';

      var title = document.createElement('div');
      title.className = 'text-rk-text font-medium text-sm';
      title.textContent = item.title || 'Untitled';

      var desc = document.createElement('div');
      desc.className = 'text-rk-text-secondary text-xs mt-1 line-clamp-2';
      desc.textContent = item.description || item.summary || '';

      el.appendChild(title);
      el.appendChild(desc);
      fragment.appendChild(el);
    }

    searchResults.appendChild(fragment);
  }

  // Debounce helper
  function debounce(fn, delay) {
    var timer;
    return function () {
      var args = arguments;
      var ctx = this;
      clearTimeout(timer);
      timer = setTimeout(function () { fn.apply(ctx, args); }, delay);
    };
  }

  if (searchInput) {
    searchInput.addEventListener('input', debounce(function () {
      var query = searchInput.value.trim();
      if (query.length < 2) {
        renderResults([]);
        return;
      }

      loadSearchIndex(function (data) {
        var fuse = getFuse(data);
        if (!fuse) return;
        var results = fuse.search(query);
        renderResults(results);
      });
    }, 200));
  }

  // -------------------------------------------------------
  // Keyboard navigation in search results
  // -------------------------------------------------------
  if (searchInput) {
    searchInput.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        e.preventDefault();
        if (!searchResults) return;
        var items = searchResults.querySelectorAll('.search-result-item');
        if (items.length === 0) return;

        var focused = searchResults.querySelector('.search-result-item:focus');
        var index = Array.prototype.indexOf.call(items, focused);

        if (e.key === 'ArrowDown') {
          index = index < items.length - 1 ? index + 1 : 0;
        } else {
          index = index > 0 ? index - 1 : items.length - 1;
        }
        items[index].focus();
      }
      if (e.key === 'Enter') {
        var focused = searchResults && searchResults.querySelector('.search-result-item:focus');
        if (focused) {
          e.preventDefault();
          focused.click();
        }
      }
    });
  }

})();
