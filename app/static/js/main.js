/**
 * Aurocous — Main JavaScript
 * Vanilla JS: scroll animations, navigation, form validation, counters
 */
document.addEventListener('DOMContentLoaded', () => {

    /* ======================================================
       1. Smooth Scrolling for Anchor Links
    ====================================================== */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const targetId = anchor.getAttribute('href');
            if (targetId === '#') return;
            const target = document.querySelector(targetId);
            if (!target) return;
            e.preventDefault();
            const headerOffset = 80;
            const elementPosition = target.getBoundingClientRect().top + window.pageYOffset;
            window.scrollTo({
                top: elementPosition - headerOffset,
                behavior: 'smooth'
            });
        });
    });

    /* ======================================================
       2. Sticky Header — Add .scrolled Class
    ====================================================== */
    const siteHeader = document.querySelector('.site-header');
    if (siteHeader) {
        const onScroll = () => {
            siteHeader.classList.toggle('scrolled', window.scrollY > 50);
        };
        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();
    }

    /* ======================================================
       3. Mobile Menu Toggle
    ====================================================== */
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('nav-menu');

    if (hamburger && navMenu) {
        hamburger.addEventListener('click', () => {
            const isOpen = hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
            hamburger.setAttribute('aria-expanded', isOpen);
            document.body.classList.toggle('menu-open', isOpen);
        });

        /* 4. Close mobile menu on link click */
        navMenu.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
                hamburger.setAttribute('aria-expanded', 'false');
                document.body.classList.remove('menu-open');
            });
        });
    }

    /* ======================================================
       5. Scroll Animations — Intersection Observer
    ====================================================== */
    const animatedElements = document.querySelectorAll('[data-animate]');

    if (animatedElements.length && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const el = entry.target;
                    el.classList.add('is-visible');

                    // Stagger children in grid containers
                    const gridChildren = el.querySelectorAll(
                        '.service-card, .industry-card, .product-card, .reason-card, .stat-card, .approach-step'
                    );
                    gridChildren.forEach((child, index) => {
                        child.style.transitionDelay = `${index * 0.08}s`;
                        child.classList.add('is-visible');
                    });

                    observer.unobserve(el);
                }
            });
        }, { threshold: 0.05, rootMargin: '100px 0px 100px 0px' });

        animatedElements.forEach(el => observer.observe(el));
    }

    /* ======================================================
       6. Back-to-Top Button
    ====================================================== */
    const backToTop = document.getElementById('back-to-top');
    if (backToTop) {
        const toggleBackToTop = () => {
            backToTop.classList.toggle('visible', window.scrollY > 500);
        };
        window.addEventListener('scroll', toggleBackToTop, { passive: true });
        toggleBackToTop();

        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    /* ======================================================
       7. Contact Form Client-Side Validation (Progressive Enhancement)
    ====================================================== */
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            let isValid = true;

            // Clear previous errors
            contactForm.querySelectorAll('.form-error').forEach(el => el.remove());
            contactForm.querySelectorAll('.input-error').forEach(el => el.classList.remove('input-error'));

            const requiredFields = contactForm.querySelectorAll('[required]');
            requiredFields.forEach(field => {
                const value = field.value.trim();
                if (!value) {
                    isValid = false;
                    showFieldError(field, 'This field is required.');
                }
            });

            // Validate email format
            const emailField = contactForm.querySelector('#business_email');
            if (emailField && emailField.value.trim()) {
                const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailPattern.test(emailField.value.trim())) {
                    isValid = false;
                    showFieldError(emailField, 'Please enter a valid email address.');
                }
            }

            if (!isValid) {
                e.preventDefault();
                // Focus the first field with an error
                const firstError = contactForm.querySelector('.input-error');
                if (firstError) firstError.focus();
            }
        });

        function showFieldError(field, message) {
            field.classList.add('input-error');
            const errorEl = document.createElement('span');
            errorEl.className = 'form-error';
            errorEl.textContent = message;
            field.parentNode.appendChild(errorEl);
        }
    }

    /* ======================================================
       8. Active Nav Link Highlighting
    ====================================================== */
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');

    if (sections.length && navLinks.length) {
        const highlightNav = () => {
            const scrollPos = window.scrollY + 120;

            sections.forEach(section => {
                const top = section.offsetTop;
                const height = section.offsetHeight;
                const id = section.getAttribute('id');

                if (scrollPos >= top && scrollPos < top + height) {
                    navLinks.forEach(link => {
                        link.classList.remove('active');
                        if (link.getAttribute('href') === `#${id}`) {
                            link.classList.add('active');
                        }
                    });
                }
            });
        };
        window.addEventListener('scroll', highlightNav, { passive: true });
        highlightNav();
    }

    /* ======================================================
       9. Counter Animation for Stat Numbers
    ====================================================== */
    const statValues = document.querySelectorAll('.stat-value');

    if (statValues.length && 'IntersectionObserver' in window) {
        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    counterObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        statValues.forEach(el => counterObserver.observe(el));
    }

    function animateCounter(el) {
        const raw = el.getAttribute('data-count') || el.textContent;
        const suffix = raw.replace(/[0-9]/g, ''); // e.g. "+"
        const target = parseInt(raw, 10);
        if (isNaN(target)) return;

        const duration = 1600; // ms
        const startTime = performance.now();

        function update(now) {
            const elapsed = now - startTime;
            const progress = Math.min(elapsed / duration, 1);
            // Ease-out quad
            const eased = 1 - (1 - progress) * (1 - progress);
            const current = Math.round(eased * target);
            el.textContent = current + suffix;
            if (progress < 1) {
                requestAnimationFrame(update);
            }
        }

        el.textContent = '0' + suffix;
        requestAnimationFrame(update);
    }

});
