/**
 * Universal Site Controller for Personal Website
 *
 * Purpose:
 *   - Encapsulates all shared and page-specific UI logic for a modern, educational personal website.
 *   - Teaches OOP principles, clean architecture, and security-first development.
 *
 * Clean Architecture Layer:
 *   - Presentation Layer: Handles UI events and DOM manipulation.
 *
 * Security Considerations:
 *   - No inline scripts (CSP-compliant).
 *   - Defensive coding: Checks for element existence before acting.
 *   - No direct user input handling.
 */

/* ===================== Navbar Controller ===================== */
/**
 * Controls navbar scroll effect for visual feedback.
 *
 * OOP: Encapsulation, Single Responsibility.
 */
class NavbarController {
    constructor(navbarId = 'navbar') {
        this.navbar = document.getElementById(navbarId);
        if (this.navbar) {
            window.addEventListener('scroll', this.handleScroll.bind(this));
        }
    }
    handleScroll() {
        if (window.scrollY > 50) {
            this.navbar.classList.add('scrolled');
        } else {
            this.navbar.classList.remove('scrolled');
        }
    }
}

/* ===================== Mobile Menu Controller ===================== */
/**
 * Controls mobile menu burger for responsive navigation.
 *
 * OOP: Encapsulation, Single Responsibility.
 */
class MobileMenuController {
    constructor(menuBtnId = 'mobileMenuBtn', navLinksSelector = '.nav-links') {
        this.menuBtn = document.getElementById(menuBtnId);
        this.navLinks = document.querySelector(navLinksSelector);
        if (this.menuBtn && this.navLinks) {
            this.menuBtn.addEventListener('click', this.toggleMenu.bind(this));
        }
    }
    toggleMenu() {
        this.navLinks.classList.toggle('active');
    }
}

/* ===================== Animation Controller ===================== */
/**
 * Handles fade-in animations for cards and sections using Intersection Observer.
 *
 * OOP: Encapsulation, Abstraction.
 */
class AnimationController {
    constructor(selectors = []) {
        if ('IntersectionObserver' in window && selectors.length > 0) {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('fade-in-up');
                    }
                });
            }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
            selectors.forEach(selector => {
                document.querySelectorAll(selector).forEach(el => observer.observe(el));
            });
        }
    }
}

/* ===================== Smooth Scroll Controller ===================== */
/**
 * Enables smooth scrolling for anchor links.
 *
 * OOP: Encapsulation.
 */
class SmoothScrollController {
    constructor() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });
    }
}

/* ===================== Lazy Image Controller ===================== */
/**
 * Implements lazy loading for images using Intersection Observer.
 *
 * OOP: Encapsulation.
 */
class LazyImageController {
    constructor() {
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src;
                        img.classList.remove('lazy');
                        imageObserver.unobserve(img);
                    }
                });
            });
            document.querySelectorAll('img[data-src]').forEach(img => imageObserver.observe(img));
        }
    }
}

/* ===================== Education Page Controller ===================== */
/**
 * Handles education page-specific interactions.
 *
 * OOP: Encapsulation, Polymorphism.
 */
class EducationPageController {
    constructor() {
        // Certificate card hover effects
        document.querySelectorAll('.cert-item').forEach(item => {
            item.addEventListener('mouseenter', () => {
                item.style.backgroundColor = 'var(--bg-accent)';
                item.style.transform = 'translateX(5px)';
            });
            item.addEventListener('mouseleave', () => {
                item.style.backgroundColor = 'transparent';
                item.style.transform = 'translateX(0px)';
            });
        });

        // Skill tags interaction
        document.querySelectorAll('.skill-tag').forEach(tag => {
            tag.addEventListener('click', () => {
                console.log('Skill clicked:', tag.textContent);
            });
        });

        // Timeline item progression
        const timelineItems = document.querySelectorAll('.timeline-item');
        timelineItems.forEach((item, index) => {
            item.style.animationDelay = `${index * 0.2}s`;
        });

        // Certificate verification link
        document.querySelectorAll('.verify-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                console.log('Certificate verification requested');
            });
        });
    }
}

/* ===================== Index Page Controller ===================== */
/**
 * Handles index page-specific interactions.
 *
 * OOP: Encapsulation, Polymorphism.
 */
class IndexPageController {
    constructor() {
        // Stat card hover effects
        document.querySelectorAll('.stat-card').forEach(card => {
            card.addEventListener('mouseenter', () => {
                const number = card.querySelector('.stat-number');
                if (number) number.style.transform = 'scale(1.1)';
            });
            card.addEventListener('mouseleave', () => {
                const number = card.querySelector('.stat-number');
                if (number) number.style.transform = 'scale(1)';
            });
        });

        // Hero entrance animation
        const heroContent = document.querySelector('.hero-content');
        if (heroContent) {
            setTimeout(() => {
                heroContent.style.opacity = '100';
                heroContent.style.transform = 'translateY(0)';
            }, 100);
        }
        document.body.classList.remove('loading');
    }
}

/* ===================== Initialization ===================== */
/**
 * Initializes all controllers based on page context.
 *
 * Clean Architecture: Presentation Layer only.
 * Security: Defensive coding, CSP-compliant.
 */
document.addEventListener('DOMContentLoaded', () => {
    new NavbarController();
    new MobileMenuController();
    new AnimationController([
        '.stat-card', '.highlight-card', '.nav-card', // index page
        '.academic-card', '.cert-provider', '.timeline-item' // education page
    ]);
    new SmoothScrollController();
    new LazyImageController();

    // Page-specific initialization
    if (document.body.classList.contains('education-page')) {
        new EducationPageController();
    }
    if (document.body.classList.contains('index-page')) {
        new IndexPageController();
    }
});