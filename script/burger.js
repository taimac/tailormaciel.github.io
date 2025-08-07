class Navigation {
    constructor() {
        // Store the DOM elements we need to manipulate
        this.burger = document.getElementById('burger');
        this.navMenu = document.getElementById('menu');
        this.cross = document.getElementById('cross');


        // Call this method to initialize event listeners
        this.bindEvents();
    }

    showMenu() {
        this.navMenu.classList.remove('remove');
        this.navMenu.classList.toggle('show');
    }

    hideMenu() {
        this.navMenu.classList.add('remove');
        this.navMenu.classList.remove('show');
    }

    bindEvents() {
        // Toggle menu visibility on burger click
        this.burger.addEventListener('click', () => this.showMenu());

        // Hide menu on cross click
        this.cross.addEventListener('click', () => this.hideMenu());

        // Hide menu when clicking outside of it
        document.addEventListener('click', (event) => {
            if (!this.navMenu.contains(event.target) && !this.burger.contains(event.target)) {
                this.hideMenu();
            }
        });
    }

}

// Initialize the navigation
const navigation = new Navigation();
