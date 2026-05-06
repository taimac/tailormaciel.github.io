class NavbarController {
    constructor(navbarId = 'navbar') {
        this.navbar = document.getElementById(navbarId);
        if (this.navbar) {
            window.addEventListener('scroll', this._handleScroll.bind(this));
            this._setActiveLink();
        }
    }

    _handleScroll() {
        this.navbar.classList.toggle('scrolled', window.scrollY > 50);
    }

    _setActiveLink() {
        const current = window.location.pathname.split('/').pop() || 'index.html';
        this.navbar.querySelectorAll('.nav-links a').forEach(link => {
            const href = link.getAttribute('href') || '';
            if (href && href.includes(current)) link.classList.add('active');
        });
    }
}

class MobileMenuController {
    constructor(btnId = 'mobileMenuBtn', navSelector = '.nav-links') {
        this.btn = document.getElementById(btnId);
        this.nav = document.querySelector(navSelector);
        if (this.btn && this.nav) {
            this.btn.addEventListener('click', this._toggle.bind(this));
            document.addEventListener('click', this._closeOutside.bind(this));
        }
    }

    _toggle() {
        const open = this.nav.classList.toggle('active');
        this.btn.setAttribute('aria-expanded', open);
    }

    _closeOutside(e) {
        if (
            this.nav.classList.contains('active') &&
            !this.nav.contains(e.target) &&
            !this.btn.contains(e.target)
        ) {
            this.nav.classList.remove('active');
            this.btn.setAttribute('aria-expanded', 'false');
        }
    }
}

class AnimationController {
    constructor(selectors = []) {
        if (!('IntersectionObserver' in window) || selectors.length === 0) return;
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in-up');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
        selectors.forEach(sel => {
            document.querySelectorAll(sel).forEach(el => observer.observe(el));
        });
    }
}

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

class LanguageSwitcherController {
    constructor(storageKey = 'tm-lang', defaultLang = 'pt') {
        this.storageKey = storageKey;
        this.defaultLang = defaultLang;
        this.btn = document.getElementById('langToggle');
        if (!this.btn || typeof TM_TRANSLATIONS === 'undefined') return;

        const saved = localStorage.getItem(storageKey);
        const lang = saved || defaultLang;
        if (lang !== defaultLang) this._apply(lang);
        this._updateBtn(lang);

        this.btn.addEventListener('click', () => {
            const current = localStorage.getItem(this.storageKey) || this.defaultLang;
            const next = current === 'pt' ? 'en' : 'pt';
            this._apply(next);
            this._updateBtn(next);
            localStorage.setItem(this.storageKey, next);
        });
    }

    _resolve(obj, path) {
        return path.split('.').reduce((acc, k) => acc && acc[k], obj);
    }

    _apply(lang) {
        const dict = TM_TRANSLATIONS[lang];
        if (!dict) return;

        document.documentElement.lang = lang === 'pt' ? 'pt-BR' : 'en';

        document.querySelectorAll('[data-i18n]').forEach(el => {
            const val = this._resolve(dict, el.dataset.i18n);
            if (val !== undefined) el.textContent = val;
        });

        document.querySelectorAll('[data-i18n-html]').forEach(el => {
            const val = this._resolve(dict, el.dataset.i18nHtml);
            if (val !== undefined) el.innerHTML = val;
        });

        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const val = this._resolve(dict, el.dataset.i18nPlaceholder);
            if (val !== undefined) el.placeholder = val;
        });

        document.querySelectorAll('[data-i18n-aria]').forEach(el => {
            const val = this._resolve(dict, el.dataset.i18nAria);
            if (val !== undefined) el.setAttribute('aria-label', val);
        });

        const titleEl = document.querySelector('title[data-i18n]');
        if (titleEl) {
            const val = this._resolve(dict, titleEl.dataset.i18n);
            if (val) document.title = val;
        }

        const metaEl = document.querySelector('meta[name="description"][data-i18n-content]');
        if (metaEl) {
            const val = this._resolve(dict, metaEl.dataset.i18nContent);
            if (val) metaEl.content = val;
        }
    }

    _updateBtn(lang) {
        if (this.btn) this.btn.textContent = lang === 'pt' ? 'EN' : 'PT';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new NavbarController();
    new MobileMenuController();
    new SmoothScrollController();
    new LanguageSwitcherController();
    new AnimationController([
        '.stat-item',
        '.card',
        '.degree-card',
        '.cert-card',
        '.timeline__item',
        '.prose-grid',
    ]);
});
