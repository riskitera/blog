/**
 * Riskitera Blog - PostHog Custom Tracking
 * Article views, CTA clicks, scroll depth, newsletter signups
 */
(function () {
  'use strict';

  // Bail if PostHog not loaded (dev mode)
  if (typeof posthog === 'undefined') return;

  // -------------------------------------------------------
  // Helpers
  // -------------------------------------------------------
  var page = document.querySelector('article');
  var isArticle = !!page;

  function getMeta(name) {
    var el = document.querySelector('meta[name="' + name + '"]');
    return el ? el.getAttribute('content') : null;
  }

  function getArticleData() {
    var title = document.title.split(' | ')[0] || document.title;
    var slug = window.location.pathname;
    var tags = document.querySelectorAll('[data-tag]');
    var tagList = [];
    tags.forEach(function (t) { tagList.push(t.dataset.tag || t.textContent.trim()); });

    // Detect funnel stage from tags or categories
    var funnel = 'tofu';
    var bodyText = (document.body.className + ' ' + slug).toLowerCase();
    if (bodyText.indexOf('comparativa') > -1 || bodyText.indexOf('mejores') > -1 || bodyText.indexOf('roi') > -1) {
      funnel = 'bofu';
    } else if (bodyText.indexOf('guia-completa') > -1 || bodyText.indexOf('pillar') > -1 || bodyText.indexOf('como-elegir') > -1) {
      funnel = 'mofu';
    }

    // Reading time (approx)
    var content = page ? page.textContent : '';
    var words = content.split(/\s+/).length;
    var readingTime = Math.round(words / 200);

    return {
      title: title,
      slug: slug,
      funnel: funnel,
      tags: tagList,
      reading_time_min: readingTime,
      word_count: words
    };
  }

  // -------------------------------------------------------
  // Article View
  // -------------------------------------------------------
  if (isArticle) {
    var data = getArticleData();
    posthog.capture('blog_article_view', data);
  }

  // -------------------------------------------------------
  // CTA Click Tracking
  // -------------------------------------------------------
  document.addEventListener('click', function (e) {
    var link = e.target.closest('a[href*="riskitera.com"], a[data-cta-type], .cta-block a, .btn-primary');
    if (!link) return;

    var ctaType = link.dataset.ctaType || 'general';
    var destination = link.getAttribute('href') || '';

    // Classify CTA
    if (destination.indexOf('/demo') > -1 || destination.indexOf('/contacto') > -1) {
      ctaType = 'demo';
    } else if (destination.indexOf('lead-magnet') > -1 || destination.indexOf('download') > -1) {
      ctaType = 'lead_magnet';
    }

    posthog.capture('blog_cta_click', {
      cta_type: ctaType,
      cta_text: link.textContent.trim().substring(0, 100),
      destination: destination,
      article: isArticle ? getArticleData().title : document.title,
      page_url: window.location.pathname
    });
  });

  // -------------------------------------------------------
  // Scroll Depth (articles only)
  // -------------------------------------------------------
  if (isArticle) {
    var scrollMarks = { 25: false, 50: false, 75: false, 100: false };
    var articleData = getArticleData();
    var ticking = false;

    function checkScroll() {
      var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      var docHeight = document.documentElement.scrollHeight - window.innerHeight;
      if (docHeight <= 0) return;

      var percent = Math.round((scrollTop / docHeight) * 100);

      [25, 50, 75, 100].forEach(function (mark) {
        if (percent >= mark && !scrollMarks[mark]) {
          scrollMarks[mark] = true;
          posthog.capture('blog_scroll_depth', {
            depth: mark + '%',
            title: articleData.title,
            slug: articleData.slug
          });
        }
      });
    }

    window.addEventListener('scroll', function () {
      if (!ticking) {
        window.requestAnimationFrame(function () {
          checkScroll();
          ticking = false;
        });
        ticking = true;
      }
    });
  }

  // -------------------------------------------------------
  // Newsletter Signup Tracking
  // -------------------------------------------------------
  document.addEventListener('submit', function (e) {
    var form = e.target.closest('form');
    if (!form) return;

    // Detect newsletter forms by action or class
    var action = form.getAttribute('action') || '';
    var isNewsletter = action.indexOf('brevo') > -1
      || action.indexOf('newsletter') > -1
      || form.classList.contains('newsletter-form')
      || form.closest('.newsletter-section');

    if (isNewsletter) {
      posthog.capture('blog_newsletter_signup', {
        source: form.dataset.source || 'footer',
        page_url: window.location.pathname
      });
    }
  });

  // -------------------------------------------------------
  // Search Usage Tracking
  // -------------------------------------------------------
  var searchInput = document.getElementById('search-input');
  if (searchInput) {
    var searchTimeout;
    searchInput.addEventListener('input', function () {
      clearTimeout(searchTimeout);
      var query = searchInput.value.trim();
      if (query.length >= 3) {
        searchTimeout = setTimeout(function () {
          posthog.capture('blog_search', {
            query: query,
            page_url: window.location.pathname
          });
        }, 1500);
      }
    });
  }

  // -------------------------------------------------------
  // Outbound Link Tracking
  // -------------------------------------------------------
  document.addEventListener('click', function (e) {
    var link = e.target.closest('a[href^="http"]');
    if (!link) return;
    var href = link.getAttribute('href');
    if (href.indexOf('riskitera.com') > -1 || href.indexOf('blog.riskitera.com') > -1) return;

    posthog.capture('blog_outbound_click', {
      url: href,
      text: link.textContent.trim().substring(0, 100),
      page_url: window.location.pathname
    });
  });

})();
