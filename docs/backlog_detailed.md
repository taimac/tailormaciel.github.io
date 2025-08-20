# 📋 Development Backlog

Repository: taimac/tailormaciel.github.io

Exported: 2025-08-20 03:11 UTC

Total items fetched: 67 | Issues: 61 | PRs: 6

---

## Active Pull Requests (1)

🔄 **[#90](https://github.com/taimac/tailormaciel.github.io/pull/90)** feat(B01): scaffold hybrid project structure
  _author: taimac • created: 2025-08-16T17:26:22Z • comments: 0_

Implements B01: frontend scaffold, assets, setup docs. See docs/SETUP.md for usage.

## Open Issues (43)

🚀 **[#94](https://github.com/taimac/tailormaciel.github.io/issues/94)** B04.4 — Certificate Verification System Implementation `priority-medium, type-feature, learning-security, component-ui, backlog-import-2025-08`
  _milestone: Milestone 0_

  _author: taimac • created: 2025-08-19T02:46:38Z • comments: 0_

**Backlog ID**: B04.4

**Issue #4.4: Certificate Verification System Implementation**

**Description**
Replace placeholder certificate verification with functional system. Address Copilot feedback about non-functional verification links and incomplete certificate validation features.

**Learning Goals**
- External API integration security and error handling
- URL validation patterns and security considerations
- User feedback systems for asynchronous operations
- Error handling for third-party service failures
- HTTP request security and data validation

**Security Considerations**
- Validate all certificate verification URLs to prevent redirect attacks
- Implement proper error handling without exposing sensitive information
- Secure HTTP requests with proper headers and timeouts
- Prevent certificate data injection through input validation

**Architecture Notes**
- Uses Strategy pattern for different certificate providers
- Implements Circuit Breaker pattern for external service failures
- Follows Repository pattern for certificate data access
- Demonstrates proper error boundary implementation

**Acceptance Criteria**
- [ ] Replace `href='#'` with actual certificate verification URLs
- [ ] Implement certificate validation API integration
- [ ] Add user feedback for verification status (loading, success, error)
- [ ] Create comprehensive error handling for network failures
- [ ] Add certificate authenticity validation
- [ ] Open verification links in new tabs with proper security attributes

**Subtasks**
- [ ] Create `CertificateVerificationService` class
- [ ] Implement URL validation and sanitization
- [ ] Add loading states and user feedback components
- [ ] Create error handling for various failure scenarios
- [ ] Add certificate provider configuration system
- [ ] Implement caching for verification results

**Depends On**: B04.2

**Suggested Branch**: `feature/issue-4_4-certificate-verification`

🚀 **[#93](https://github.com/taimac/tailormaciel.github.io/issues/93)** B04.3 — Mobile Navigation Component Implementation `priority-high, type-feature, component-ui, learning-frontend, backlog-import-2025-08`
  _milestone: Milestone 0_

  _author: taimac • created: 2025-08-19T02:46:37Z • comments: 0_

**Backlog ID**: B04.3

**Issue #4.3: Mobile Navigation Component Implementation**

**Description**
Implement professional mobile menu with accessibility, progressive enhancement, and smooth animations. Address Copilot feedback about incomplete mobile menu functionality by creating a fully functional component.

**Learning Goals**
- Progressive enhancement implementation (works without JS, enhanced with JS)
- Touch and keyboard interaction patterns for mobile interfaces
- CSS animation performance optimization techniques
- Accessibility-first component design with ARIA attributes
- Component state management and user interaction handling

**Security Considerations**
- Prevent navigation manipulation through secure route validation
- Implement safe event handling to prevent injection attacks
- Ensure focus management doesn't expose sensitive information

**Architecture Notes**
- Follows Strategy pattern for different menu animation types
- Uses Template Method pattern for consistent menu behavior
- Implements Observer pattern for menu state notifications
- Demonstrates polymorphism through interface-based design

**Acceptance Criteria**
- [ ] Implement hamburger menu with smooth CSS animations
- [ ] Add comprehensive keyboard navigation support (Tab, Enter, Escape)
- [ ] Include ARIA attributes and screen reader announcements
- [ ] Create touch gesture support for mobile devices
- [ ] Test across different viewport sizes and orientations
- [ ] Implement focus trap when menu is open
- [ ] Add animation performance monitoring

**Subtasks**
- [ ] Create `MobileMenuComponent` class extending base Component
- [ ] Implement CSS animations using transforms for performance
- [ ] Add ARIA live regions for screen reader updates
- [ ] Create keyboard navigation event handlers
- [ ] Add touch gesture recognition for swipe interactions
- [ ] Implement body scroll lock when menu is open
- [ ] Add comprehensive accessibility testing documentation

**Depends On**: B04.2

**Suggested Branch**: `feature/issue-4_3-mobile-navigation`

🚀 **[#92](https://github.com/taimac/tailormaciel.github.io/issues/92)** B04.2 — JavaScript Component Architecture Foundation `priority-critical, type-feature, learning-architecture, component-ui, backlog-import-2025-08`
  _milestone: Milestone 0_

  _author: taimac • created: 2025-08-19T02:46:35Z • comments: 0_

**Backlog ID**: B04.2

**Issue #4.2: JavaScript Component Architecture Foundation**

**Description**
Establish ES6 module system and component base classes to prevent embedded JavaScript issues. Create architectural foundation for maintainable, testable UI components before implementing business logic.

**Learning Goals**
- ES6 module system patterns and import/export best practices
- Component lifecycle management (mount, update, unmount)
- Event-driven architecture and component communication
- Clean separation of presentation logic from business logic
- Abstract base classes and inheritance in JavaScript

**Security Considerations**
- Prevent XSS through safe DOM manipulation patterns
- Implement input validation at component boundaries
- Secure event handling to prevent event injection

**Architecture Notes**
- Implements Abstract Factory pattern for component creation
- Uses Observer pattern for component communication
- Follows Single Responsibility: each component has one clear purpose
- Demonstrates Dependency Injection for better testability

**Acceptance Criteria**
- [ ] Create base `Component` class with lifecycle methods (`mount`, `update`, `unmount`)
- [ ] Implement event system for component communication
- [ ] Set up ES6 module import/export patterns throughout frontend
- [ ] Create component registration system for automatic initialization
- [ ] Add development-time component validation and warnings
- [ ] Document component architecture patterns in `docs/component-architecture.md`

**Subtasks**
- [ ] Create `frontend/js/base/Component.js` with abstract base class
- [ ] Create `frontend/js/utils/EventBus.js` for component communication
- [ ] Create `frontend/js/utils/DOM.js` for safe DOM manipulation
- [ ] Create `frontend/js/base/ComponentRegistry.js` for component management
- [ ] Add component lifecycle documentation with examples
- [ ] Set up module bundling configuration for development

**Depends On**: B04.1

**Suggested Branch**: `feature/issue-4_2-js-architecture`

🚀 **[#91](https://github.com/taimac/tailormaciel.github.io/issues/91)** B04.1 — Frontend CSS Architecture Setup `priority-critical, type-feature, learning-architecture, component-ui, backlog-import-2025-08`
  _milestone: Milestone 0_

  _author: taimac • created: 2025-08-19T02:46:33Z • comments: 0_

**Backlog ID**: B04.1

**Issue #4.1: Frontend CSS Architecture Setup**

**Description**
Refactor monolithic CSS into modular, component-based architecture following BEM methodology and Clean Architecture principles. Establish scalable stylesheet organization before implementing business logic components.

**Learning Goals**
- BEM methodology implementation and naming conventions
- CSS custom properties system for consistent theming
- Component-based styling patterns vs monolithic approaches
- Responsive design architecture and breakpoint systems
- CSS performance optimization and maintainability

**Security Considerations**
- Prevent CSS injection through proper sanitization
- Implement Content Security Policy for style sources
- Validate CSS custom property values

**Architecture Notes**
- Follows Single Responsibility Principle: each CSS file serves one purpose
- Implements Open/Closed Principle: easy to add new components without modifying existing
- Demonstrates separation of concerns: presentation separated from behavior

**Acceptance Criteria**
- [ ] Break `style.css` into modular structure: `base/`, `components/`, `layouts/`
- [ ] Implement CSS custom properties for colors, spacing, typography
- [ ] Add CSS naming conventions documentation following BEM
- [ ] Create responsive breakpoint system with mobile-first approach
- [ ] Validate no style regressions across existing components
- [ ] Document CSS architecture decisions in `docs/css-architecture.md`

**Subtasks**
- [ ] Create `styles/base/reset.css` for cross-browser normalization
- [ ] Create `styles/base/variables.css` for design tokens
- [ ] Create `styles/base/typography.css` for text styling
- [ ] Create `styles/components/` directory with component-specific styles
- [ ] Create `styles/layouts/` for grid systems and page layouts
- [ ] Update `styles/style.css` to import all modules
- [ ] Add CSS linting configuration (stylelint)

**Depends On**: B01

**Suggested Branch**: `feature/issue-4_1-css-architecture`

🚀 **[#89](https://github.com/taimac/tailormaciel.github.io/issues/89)** B39 — Static Site Deployment & Hosting Configuration `priority-high, type-feature, component-performance, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:43:43Z • comments: 0_

**Backlog ID**: B39

**Issue #39: Static Site Deployment & Hosting Configuration**

**Description**
Harden production deploy: static CDN hosting for frontend, optional backend host, security headers, HTTPS, and monitoring/analytics.

**Learning Goals**
- Static hosting configs and headers.  
- Basic monitoring/analytics wiring.

**Acceptance Criteria**
- [ ] GitHub Pages/Netlify config committed; custom domain optional.  
- [ ] Security headers and HTTPS enforced.  
- [ ] Monitoring enabled; baseline error budget defined.  
- [ ] Deployment guide finalized in `docs/`.

**Subtasks**
- [ ] Healthcheck route + uptime check.

**Depends On**: #23, #27

**Suggested Branch**: `feature/issue-39-deploy-config`

🚀 **[#88](https://github.com/taimac/tailormaciel.github.io/issues/88)** B38 — Asset Optimization & Lazy Loading `priority-medium, type-feature, component-performance, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:43:40Z • comments: 0_

**Backlog ID**: B38

**Issue #38: Asset Optimization & Lazy Loading**

**Description**
Implement lazy loading for images/PDFs, compress assets, and defer non-critical JS.

**Learning Goals**
- Modern image formats, responsive images.  
- Defer/async scripts best practices.

**Acceptance Criteria**
- [ ] Lazy load non-critical assets with placeholders.  
- [ ] Lighthouse performance ≥ 90 on homepage.  
- [ ] Compression pipeline documented.

**Subtasks**
- [ ] Generate thumbnails for large images.

**Depends On**: #20, #23

**Suggested Branch**: `feature/issue-38-asset-opt`

🚀 **[#87](https://github.com/taimac/tailormaciel.github.io/issues/87)** B37 — Graph Rendering Optimization `priority-medium, type-feature, component-performance, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:43:38Z • comments: 0_

**Backlog ID**: B37

**Issue #37: Graph Rendering Optimization**

**Description**
Optimize the graph visualization for large node counts with batching and level-of-detail.

**Learning Goals**
- Rendering pipelines and throttling.  
- LOD techniques.

**Acceptance Criteria**
- [ ] Stable ≥ 50 FPS for 1k nodes on mid-tier laptop.  
- [ ] LOD reduces labels/edges when zoomed out.  
- [ ] Perf diagnostics overlay.

**Subtasks**
- [ ] Frame scheduler utility.

**Depends On**: #14

**Suggested Branch**: `feature/issue-37-graph-perf`

🚀 **[#86](https://github.com/taimac/tailormaciel.github.io/issues/86)** B36 — Search Index Compression `priority-medium, type-feature, component-performance, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:43:35Z • comments: 0_

**Backlog ID**: B36

**Issue #36: Search Index Compression**

**Description**
Compact index data structures; optionally gzip/brotli via hosting.

**Learning Goals**
- Data compaction techniques.  
- Measuring size vs accuracy.

**Acceptance Criteria**
- [ ] Memory footprint reduced by ≥ 30% without accuracy loss.  
- [ ] Load time improvement reported.  
- [ ] Configurable compression toggle.

**Subtasks**
- [ ] Benchmark script.

**Depends On**: #10, #9

**Suggested Branch**: `feature/issue-36-index-compress`

🚀 **[#85](https://github.com/taimac/tailormaciel.github.io/issues/85)** B35 — Client‑Side Caching & Prefetching `priority-medium, type-feature, component-performance, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:43:33Z • comments: 0_

**Backlog ID**: B35

**Issue #35: Client‑Side Caching & Prefetching**

**Description**
Cache indexes and metadata with versioning; prefetch likely-next content on hover/idle.

**Learning Goals**
- Cache invalidation strategies.  
- UX vs bandwidth trade-offs.

**Acceptance Criteria**
- [ ] Versioned cache with purge controls.  
- [ ] Prefetch heuristics (hover, idle).  
- [ ] Metrics: cache hit rate logged.

**Subtasks**
- [ ] Toggle prefetch via settings.

**Depends On**: #10, #19

**Suggested Branch**: `feature/issue-35-caching`

🚀 **[#84](https://github.com/taimac/tailormaciel.github.io/issues/84)** B34 — Developer Guide — Setup & Workflow `priority-medium, type-documentation, component-docs, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:43:30Z • comments: 0_

**Backlog ID**: B34

**Issue #34: Developer Guide — Setup & Workflow**

**Description**
Consolidate setup steps, scripts reference, debugging tips, and quality gates for onboarding.

**Learning Goals**
- Onboarding experience.  
- Troubleshooting checklists.

**Acceptance Criteria**
- [ ] End-to-end local setup with screenshots.  
- [ ] Known issues & fixes page.  
- [ ] Links to tests, scripts, and style guides.

**Subtasks**
- [ ] “First bug to fix” checklist for newcomers.

**Depends On**: #4, #28, #29

**Suggested Branch**: `docs/issue-34-developer-guide`

🚀 **[#83](https://github.com/taimac/tailormaciel.github.io/issues/83)** B33 — User Guide — Content & Metadata `priority-medium, type-documentation, component-docs, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:43:27Z • comments: 0_

**Backlog ID**: B33

**Issue #33: User Guide — Content & Metadata**

**Description**
Write a user-facing guide on adding files, writing metadata, and linking topics.

**Learning Goals**
- Clear instructional writing.  
- Examples-first documentation.

**Acceptance Criteria**
- [ ] Step-by-step guide with screenshots/GIFs.  
- [ ] FAQs and common errors section.  
- [ ] Cross-links to schema and tools.

**Subtasks**
- [ ] Short video/gif capture pipeline (optional).

**Depends On**: #2, #10

**Suggested Branch**: `docs/issue-33-user-guide`

🚀 **[#82](https://github.com/taimac/tailormaciel.github.io/issues/82)** B32 — Keep README & Architecture Docs Updated `priority-medium, type-documentation, component-docs, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:43:25Z • comments: 0_

**Backlog ID**: B32

**Issue #32: Keep README & Architecture Docs Updated**

**Description**
Continuously align README, architecture diagrams, and change log with the codebase.

**Learning Goals**
- Docs-as-code workflows.  
- Communicating design decisions.

**Acceptance Criteria**
- [ ] README quickstart verified quarterly or per milestone.  
- [ ] Diagrams updated for major structure changes.  
- [ ] `docs/CHANGELOG.md` entries per release.

**Subtasks**
- [ ] Doc CI check (links, anchors).

**Depends On**: Ongoing

**Suggested Branch**: `docs/issue-32-readme-arch`

🚀 **[#81](https://github.com/taimac/tailormaciel.github.io/issues/81)** B31 — Security Tests & Static Checks `priority-medium, type-feature, component-testing, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:43:22Z • comments: 0_

**Backlog ID**: B31

**Issue #31: Security Tests & Static Checks**

**Description**
Add static analysis (JS/CSS/Python), token tamper/replay tests, and basic dependency audit.

**Learning Goals**
- Shift-left security.  
- Threat modeling to test cases.

**Acceptance Criteria**
- [ ] ESLint/stylelint/flake8 configured in CI.  
- [ ] Token replay/tamper tests fail safely.  
- [ ] Dependency audit step (npm/pip) with report.

**Subtasks**
- [ ] Baseline vulnerabilities list in `docs/security.md`.

**Depends On**: #16, #18

**Suggested Branch**: `feature/issue-31-security-static`

🚀 **[#80](https://github.com/taimac/tailormaciel.github.io/issues/80)** B30 — Integration Tests (Dev Environment) `priority-high, type-feature, component-testing, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:43:15Z • comments: 0_

**Backlog ID**: B30

**Issue #30: Integration Tests (Dev Environment)**

**Description**
E2E flow: login → navigate to private → open file → logout; plus search and graph basic journeys.

**Learning Goals**
- Black‑box testing mindset.  
- Deterministic fixtures.

**Acceptance Criteria**
- [ ] Headless browser or script validating UI+API integration.  
- [ ] Stable sample content under `content/private/_samples`.  
- [ ] CI job runs E2E nightly and on PR label.

**Subtasks**
- [ ] Retry helpers and screenshots on failure (optional).

**Depends On**: #4, #7, #16, #17

**Suggested Branch**: `feature/issue-30-e2e`

🚀 **[#79](https://github.com/taimac/tailormaciel.github.io/issues/79)** B29 — Backend Tests (Flask) `priority-high, type-feature, component-testing, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:43:12Z • comments: 0_

**Backlog ID**: B29

**Issue #29: Backend Tests (Flask)**

**Description**
Unit/integration tests for auth endpoints and private file serving.

**Learning Goals**
- API testing with Flask client.  
- Fixtures and token helpers.

**Acceptance Criteria**
- [ ] Happy path login/validate; 401s for bad password/token.  
- [ ] Private file 401 without token; 200 with token; 404 for missing.  
- [ ] Rate-limit simulation test (basic).

**Subtasks**
- [ ] PyTest config & coverage report.

**Depends On**: #3, #16

**Suggested Branch**: `feature/issue-29-backend-tests`

🚀 **[#78](https://github.com/taimac/tailormaciel.github.io/issues/78)** B28 — Frontend Unit Tests (Vanilla JS) `priority-high, type-feature, component-testing, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:43:09Z • comments: 0_

**Backlog ID**: B28

**Issue #28: Frontend Unit Tests (Vanilla JS)**

**Description**
Test services and DOM-light components; set up coverage reporting and CI gate.

**Learning Goals**
- Testable architecture.  
- Deterministic unit tests.  
- Coverage instrumentation.

**Acceptance Criteria**
- [ ] Test runner configured (e.g., Vitest/Jest without bundling).  
- [ ] Coverage threshold ≥ 70% project-wide.  
- [ ] Mocks for services; snapshot tests for simple markup.

**Subtasks**
- [ ] CI workflow to run tests on PR.

**Depends On**: #5, #8, #12, #19

**Suggested Branch**: `feature/issue-28-frontend-tests`

🚀 **[#77](https://github.com/taimac/tailormaciel.github.io/issues/77)** B27 — deploy.py `priority-medium, type-feature, component-utilities, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:43:07Z • comments: 0_

**Backlog ID**: B27

**Issue #27: deploy.py**

**Description**
Automate build + publish to GitHub Pages/Netlify and ping backend health if used.

**Learning Goals**
- Deployment scripting and env injection.  
- Post‑deploy verification.

**Acceptance Criteria**
- [ ] Builds to `dist/`, publishes, verifies 200 on homepage.  
- [ ] Optional: backend healthcheck endpoint ping.  
- [ ] Rollback notes documented.

**Subtasks**
- [ ] Secrets/keys handled via env vars.

**Depends On**: #23, #39

**Suggested Branch**: `feature/issue-27-deploy`

🚀 **[#76](https://github.com/taimac/tailormaciel.github.io/issues/76)** B26 — validate_connections.py `priority-medium, type-feature, component-utilities, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:43:04Z • comments: 0_

**Backlog ID**: B26

**Issue #26: validate_connections.py**

**Description**
Validate that all `connections[].to` targets exist; report missing nodes, cycles (optional), and invalid strengths.

**Learning Goals**
- Data validation and reporting.  
- CI‑friendly exit codes.

**Acceptance Criteria**
- [ ] CLI outputs human‑readable summary + machine‑readable JSON.  
- [ ] Exit code 1 on invalid; 0 on success.  
- [ ] Integration note for CI job.

**Subtasks**
- [ ] Option to auto‑fix common mistakes (case, trailing slash).

**Depends On**: #10

**Suggested Branch**: `feature/issue-26-validate-connections`

🚀 **[#75](https://github.com/taimac/tailormaciel.github.io/issues/75)** B25 — generate_metadata.py `priority-medium, type-feature, component-utilities, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:43:01Z • comments: 0_

**Backlog ID**: B25

**Issue #25: generate_metadata.py**

**Description**
Scan content folders and produce baseline `.metadata.json` where missing; merge safely when present.

**Learning Goals**
- Filesystem traversal.  
- Idempotent scripts and dry‑run patterns.  
- Safe JSON writing/merging.

**Acceptance Criteria**
- [ ] Dry‑run prints intended changes; real run writes.  
- [ ] Never overwrites custom fields without explicit flag.  
- [ ] Unit tests on sample trees.

**Subtasks**
- [ ] Config for ignore/include patterns.

**Depends On**: #2

**Suggested Branch**: `feature/issue-25-generate-metadata`

🚀 **[#74](https://github.com/taimac/tailormaciel.github.io/issues/74)** B24 — Navigation Header & Footer Components `priority-medium, type-feature, component-ui, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:42:59Z • comments: 0_

**Backlog ID**: B24

**Issue #24: Navigation Header & Footer Components**

**Description**
Reusable header/footer with active route highlighting, auth indicator, and responsive menu.

**Learning Goals**
- Component reuse and state wiring.  
- Mobile nav patterns.  
- Semantic landmarks.

**Acceptance Criteria**
- [ ] Header with current route highlight; auth state icon/text.  
- [ ] Footer shows version/build date; links to docs.  
- [ ] Mobile menu expands/collapses via keyboard and touch.

**Subtasks**
- [ ] Add “skip to nav” link.

**Depends On**: #19, #20

**Suggested Branch**: `feature/issue-24-nav`

🚀 **[#73](https://github.com/taimac/tailormaciel.github.io/issues/73)** B23 — Frontend Build Lite (Optional Minifier Only) `priority-low, type-enhancement, component-ui, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:42:57Z • comments: 0_

**Backlog ID**: B23

**Issue #23: Frontend Build Lite (Optional Minifier Only)**

**Description**
Add a tiny build step (esbuild/terser or Python) for minifying JS/CSS and cache‑busting via hashed filenames.

**Learning Goals**
- Build pipelines and asset hashing.  
- Cache control strategies for static hosting.

**Acceptance Criteria**
- [ ] Minify JS/CSS; copy assets to `dist/`.  
- [ ] Filename hashing + manifest mapping.  
- [ ] Updated deployment docs to serve `dist/`.

**Subtasks**
- [ ] Simple Node or Python script; no bundling required.

**Depends On**: #19, #20

**Suggested Branch**: `feature/issue-23-build-lite`

🚀 **[#72](https://github.com/taimac/tailormaciel.github.io/issues/72)** B22 — Error States & Empty States UX `priority-medium, type-feature, component-ui, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:42:54Z • comments: 0_

**Backlog ID**: B22

**Issue #22: Error States & Empty States UX**

**Description**
Define consistent patterns for network errors, empty results, and unknown routes with helpful recovery actions.

**Learning Goals**
- UX writing for errors.  
- Diagnostics exposure without leaking internals.  
- Testing unhappy paths.

**Acceptance Criteria**
- [ ] Error boundary wrapper for views.  
- [ ] Inline error banners with retry and diagnostics toggle.  
- [ ] Empty state illustrations/text; tracking of frequency.  
- [ ] Unit tests simulate network failures.

**Subtasks**
- [ ] Centralized error catalog.

**Depends On**: #7, #12

**Suggested Branch**: `feature/issue-22-error-empty`

🚀 **[#71](https://github.com/taimac/tailormaciel.github.io/issues/71)** B21 — Accessibility & Keyboard Navigation `priority-high, type-feature, component-ui, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:42:52Z • comments: 0_

**Backlog ID**: B21

**Issue #21: Accessibility & Keyboard Navigation**

**Description**
Add global a11y enhancements: skip links, focus traps, keyboard shortcuts, ARIA roles, and semantic headings.

**Learning Goals**
- Practical WCAG practices.  
- Keyboard-first navigation.  
- Screen reader testing basics.

**Acceptance Criteria**
- [ ] Skip‑to‑content link works across views.  
- [ ] Keyboard map documented; modals trap focus.  
- [ ] Landmarks and roles assigned; headings logical.  
- [ ] A11y smoke test doc with findings.

**Subtasks**
- [ ] Live region for async results.  
- [ ] Reduced motion preference respected.

**Depends On**: #8

**Suggested Branch**: `feature/issue-21-a11y`

🚀 **[#70](https://github.com/taimac/tailormaciel.github.io/issues/70)** B20 — Global Styling System (BEM + CSS Utilities) `priority-high, type-feature, component-ui, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:42:49Z • comments: 0_

**Backlog ID**: B20

**Issue #20: Global Styling System (BEM + CSS Utilities)**

**Description**
Create CSS architecture: tokens (colors/spacing), resets, layout utilities, and responsive breakpoints using BEM.

**Learning Goals**
- Scalable CSS systems.  
- Dark/light readiness and theming.  
- Performance (avoid heavy selectors).

**Acceptance Criteria**
- [ ] `styles/main.css`, `styles/components.css`, `styles/responsive.css`.  
- [ ] CSS variables for color/spacing; optional dark tokens.  
- [ ] No inline styles; audit of naming consistency.  
- [ ] A11y: visible focus states and contrast checks.

**Subtasks**
- [ ] Print styles for PDFs/images.  
- [ ] Lint with stylelint (optional).

**Depends On**: #8

**Suggested Branch**: `feature/issue-20-styling`

🚀 **[#69](https://github.com/taimac/tailormaciel.github.io/issues/69)** B19 — App Shell & Routing (Vanilla JS) `priority-critical, type-feature, component-ui, learning-frontend, backlog-import-2025-08`
  _milestone: Milestone 4_

  _author: taimac • created: 2025-08-15T00:42:47Z • comments: 0_

**Backlog ID**: B19

**Issue #19: App Shell & Routing (Vanilla JS)**

**Description**
Implement hash‑based router (`#/home`, `#/search`, `#/graph`, `#/private`) with view registration and 404 fallback.

**Learning Goals**
- SPA routing fundamentals without frameworks.  
- Title/meta updates and scroll restoration.  
- Guarded routes for auth.

**Acceptance Criteria**
- [ ] Router module with `register(route, view)` and `navigate()` API.  
- [ ] 404 page and not‑found analytics counter.  
- [ ] Per‑route title/meta; focus management on navigation.  
- [ ] Simple smoke tests for route transitions.

**Subtasks**
- [ ] Route guards integrate with `AuthService`.  
- [ ] Back/forward browser support.

**Depends On**: #8, #12

**Suggested Branch**: `feature/issue-19-routing`

🚀 **[#68](https://github.com/taimac/tailormaciel.github.io/issues/68)** B18 — Secure Session Management (Vanilla JS) `priority-high, type-feature, learning-security, component-auth, backlog-import-2025-08`
  _milestone: Milestone 3_

  _author: taimac • created: 2025-08-15T00:42:44Z • comments: 0_

**Backlog ID**: B18

**Issue #18: Secure Session Management (Vanilla JS)**

**Description**
Client‑side session timer, idle timeout, clock drift checks, and token renewal UX (if implemented) with robust error handling.

**Learning Goals**
- Session hijacking/threat modeling basics.  
- Idle timeout and renewal patterns.  
- Defensive coding for network failures.

**Acceptance Criteria**
- [ ] Idle timer auto‑logout after N minutes (configurable).  
- [ ] Foreground renewal prompt when close to expiry.  
- [ ] All token errors produce safe, user‑friendly messages.  
- [ ] Unit tests for timers and edge cases.

**Subtasks**
- [ ] Optional: visibility‑based pause of idle timer.  
- [ ] Centralized error codes/messages.

**Depends On**: #16

**Suggested Branch**: `feature/issue-18-session-mgmt`

🚀 **[#67](https://github.com/taimac/tailormaciel.github.io/issues/67)** B17 — Private Content Access Control `priority-critical, type-feature, learning-security, component-files, backlog-import-2025-08`
  _milestone: Milestone 3_

  _author: taimac • created: 2025-08-15T00:42:41Z • comments: 0_

**Backlog ID**: B17

**Issue #17: Private Content Access Control**

**Description**
Guard private routes in UI and fetch flows; show authenticated-only sections and restrict navigation.

**Learning Goals**
- Conditional rendering and guards.  
- Security UX (clear states, no leaks).  
- File serving with token headers.

**Acceptance Criteria**
- [ ] `AuthService` stores token securely (localStorage + memory).  
- [ ] `FileSystemService` uses `Authorization: Bearer` for private paths.  
- [ ] UI reflects auth state (header, lock icons, blocked actions).  
- [ ] Tests: unauthorized fetch returns 401/redirect flow.

**Subtasks**
- [ ] “Remember me” token persistence toggle.  
- [ ] Logout clears all sensitive caches.

**Depends On**: #16

**Suggested Branch**: `feature/issue-17-access-control`

🚀 **[#66](https://github.com/taimac/tailormaciel.github.io/issues/66)** B16 — Minimal Backend Authentication System `priority-critical, type-feature, learning-security, component-auth, backlog-import-2025-08`
  _milestone: Milestone 3_

  _author: taimac • created: 2025-08-15T00:42:39Z • comments: 0_

**Backlog ID**: B16

**Issue #16: Minimal Backend Authentication System**

**Description**
Finalize JWT login, validate, and logout flows with password hashing and environment‑based secrets. No user DB; single admin secret for MVP.

**Learning Goals**
- Password hashing & verification.  
- Token TTL/refresh strategies.  
- Secure error messages and rate limiting (basic).

**Acceptance Criteria**
- [ ] `/api/auth/login`, `/api/auth/validate`, `/api/auth/logout` (if applicable).  
- [ ] Hashed password via env var (bcrypt/werkzeug).  
- [ ] JWT expiration (24h default) and clock skew handling.  
- [ ] Tests: invalid/expired tokens, brute‑force throttle (simple counter).

**Subtasks**
- [ ] Add security headers middleware.  
- [ ] Error audit: no sensitive info in responses.

**Depends On**: #3

**Suggested Branch**: `feature/issue-16-auth-system`

🚀 **[#65](https://github.com/taimac/tailormaciel.github.io/issues/65)** B15 — Graph‑Based Navigation & Discovery `priority-medium, type-feature, learning-frontend, component-graph, backlog-import-2025-08`
  _milestone: Milestone 2_

  _author: taimac • created: 2025-08-15T00:42:37Z • comments: 0_

**Backlog ID**: B15

**Issue #15: Graph‑Based Navigation & Discovery**

**Description**
Use the graph to surface related content, breadcrumb-like path trails, and suggested learning paths by difficulty.

**Learning Goals**
- Intro to recommendation heuristics.  
- Contextual navigation design.  
- Progressive disclosure UX.

**Acceptance Criteria**
- [ ] “Related content” sidebar with ranked items.  
- [ ] Path trail (topic → … → topic) from current node.  
- [ ] Basic learning path generator (beginner→advanced).  
- [ ] Tests validating suggestion rules.

**Subtasks**
- [ ] Toggle suggestions by tag/topic.  
- [ ] Cache last suggestions.

**Depends On**: #14

**Suggested Branch**: `feature/issue-15-graph-discovery`

🚀 **[#64](https://github.com/taimac/tailormaciel.github.io/issues/64)** B14 — Interactive Graph Visualization Component `priority-high, type-feature, learning-frontend, component-graph, backlog-import-2025-08`
  _milestone: Milestone 2_

  _author: taimac • created: 2025-08-15T00:42:35Z • comments: 0_

**Backlog ID**: B14

**Issue #14: Interactive Graph Visualization Component**

**Description**
Render graph with Canvas or SVG, supporting pan/zoom, node drag, highlighting neighbors, and responsive layouts.

**Learning Goals**
- Canvas/SVG rendering pipelines.  
- Event handling for complex interactions.  
- Layout algorithms (force-directed or simple radial).

**Acceptance Criteria**
- [ ] Smooth pan/zoom at ≥ 50 FPS on mid-tier laptop.  
- [ ] Hover/selection highlights neighbors and path to selection.  
- [ ] Mobile gestures for pan/zoom.  
- [ ] Resize observer for responsiveness.

**Subtasks**
- [ ] Option to throttle redraw with `requestAnimationFrame`.  
- [ ] Accessibility: text labels with `aria-hidden` mirroring list.

**Depends On**: #13

**Suggested Branch**: `feature/issue-14-graph-viz`

🚀 **[#63](https://github.com/taimac/tailormaciel.github.io/issues/63)** B13 — Graph Data Structure & Connection Management `priority-critical, type-feature, learning-frontend, component-graph, backlog-import-2025-08`
  _milestone: Milestone 2_

  _author: taimac • created: 2025-08-15T00:42:32Z • comments: 0_

**Backlog ID**: B13

**Issue #13: Graph Data Structure & Connection Management**

**Description**
Build graph nodes/edges from metadata connections with weights and utilities for traversal (BFS/DFS), shortest path, and clustering.

**Learning Goals**
- Graph data structures and traversal algorithms.  
- Weighting/normalization for recommendations.  
- Performance tuning for graph ops.

**Acceptance Criteria**
- [ ] `GraphService` exposes `neighbors()`, `shortestPath()`, `cluster()`.  
- [ ] Connection strength computed and capped 0..1.  
- [ ] Test suite with known graphs and expected paths/clusters.

**Subtasks**
- [ ] Defensive handling for missing nodes.  
- [ ] Serialization format documented.

**Depends On**: #10

**Suggested Branch**: `feature/issue-13-graph-data`

🚀 **[#62](https://github.com/taimac/tailormaciel.github.io/issues/62)** B12 — Frontend Services Layer (Vanilla JS) `priority-high, type-feature, component-ui, learning-frontend, backlog-import-2025-08`
  _milestone: Milestone 2_

  _author: taimac • created: 2025-08-15T00:42:24Z • comments: 0_

**Backlog ID**: B12

**Issue #12: Frontend Services Layer (Vanilla JS)**

**Description**
Implement stateless services: `FileSystemService`, `AuthService`, `SearchService`, `GraphService`, `MetadataService`. No DOM. Promise-based APIs with consistent error model.

**Learning Goals**
- Separation of concerns and testability.  
- Async/await API design.  
- Error normalization across services.

**Acceptance Criteria**
- [ ] Service contracts documented; mockable in tests.  
- [ ] All services return `{ok, data|error}` shapes.  
- [ ] Unit tests cover success/failure paths.  
- [ ] No direct DOM access from services.

**Subtasks**
- [ ] Common error types and mappers.  
- [ ] Minimal retry for transient fetch failures.

**Depends On**: #2

**Suggested Branch**: `feature/issue-12-services-layer`

🚀 **[#61](https://github.com/taimac/tailormaciel.github.io/issues/61)** B11 — Advanced Filtering & Tagging System `priority-medium, type-feature, learning-frontend, component-metadata, backlog-import-2025-08`
  _milestone: Milestone 2_

  _author: taimac • created: 2025-08-15T00:42:22Z • comments: 0_

**Backlog ID**: B11

**Issue #11: Advanced Filtering & Tagging System**

**Description**
Provide UI and logic for filtering by tags, type, difficulty, with AND/OR combinations and URL state persistence.

**Learning Goals**
- UI state modeling and observer pattern.  
- URL routing and deep-linking of filter state.  
- Composability of filters.

**Acceptance Criteria**
- [ ] Tag cloud generated from index with counts.  
- [ ] Multi-criteria filter with AND/OR, clear all, and chips UI.  
- [ ] URL `#search?tags=...&type=...` reflects state.  
- [ ] Tests for filter accuracy and edge cases.

**Subtasks**
- [ ] Debounced filter application.  
- [ ] Keyboard-accessible chips.

**Depends On**: #10

**Suggested Branch**: `feature/issue-11-filtering`

🚀 **[#60](https://github.com/taimac/tailormaciel.github.io/issues/60)** B10 — Metadata Aggregation & Indexing System `priority-high, type-feature, learning-frontend, component-metadata, backlog-import-2025-08`
  _milestone: Milestone 2_

  _author: taimac • created: 2025-08-15T00:42:20Z • comments: 0_

**Backlog ID**: B10

**Issue #10: Metadata Aggregation & Indexing System**

**Description**
Aggregate all `.metadata.json` across content folders; build an in-memory index suitable for search and graph building. Cache in `localStorage` with versioning.

**Learning Goals**
- Async file loading and error isolation.  
- Index data structures and normalization.  
- Client-side caching/version invalidation.

**Acceptance Criteria**
- [ ] `MetadataService` that loads, validates, and normalizes metadata.  
- [ ] Incremental update support (load-on-demand).  
- [ ] Cache with `indexVersion`; purge on schema change.  
- [ ] Tests for corrupted/missing metadata files.

**Subtasks**
- [ ] Add `scripts/generate_metadata.py` (#25) integration note.  
- [ ] Document index shape in `docs/metadata_schema.md`.

**Depends On**: #2

**Suggested Branch**: `feature/issue-10-indexer`

🚀 **[#59](https://github.com/taimac/tailormaciel.github.io/issues/59)** B09 — Search Engine with Strategy Pattern `priority-critical, type-feature, learning-patterns, component-metadata, backlog-import-2025-08`
  _milestone: Milestone 2_

  _author: taimac • created: 2025-08-15T00:42:17Z • comments: 0_

**Backlog ID**: B09

**Issue #9: Search Engine with Strategy Pattern**

**Description**
Implement `SearchEngine` with pluggable strategies: exact, fuzzy, and tag-based. Debounce user input; rank results.

**Learning Goals**
- Strategy pattern for algorithm swap.  
- Relevance scoring and ranking.  
- Performance considerations in the browser.

**Acceptance Criteria**
- [ ] `SearchEngine` interface + strategies (`ExactMatch`, `Fuzzy`, `TagFilter`).  
- [ ] Debounced search; cancellation of stale requests.  
- [ ] Deterministic ranking; tie-break by recency or path length.  
- [ ] Unit perf test: large index search < 100ms on mid-tier laptop.

**Subtasks**
- [ ] Add `SearchService` wrapper used by `SearchUI`.  
- [ ] Telemetry hooks (console or simple counter) for tuning.

**Depends On**: #10, #12

**Suggested Branch**: `feature/issue-9-search-engine`

🚀 **[#58](https://github.com/taimac/tailormaciel.github.io/issues/58)** B08 — Core Frontend Components (Vanilla JS) `priority-critical, type-feature, component-ui, learning-frontend, backlog-import-2025-08`
  _milestone: Milestone 1_

  _author: taimac • created: 2025-08-15T00:42:15Z • comments: 0_

**Backlog ID**: B08

**Issue #8: Core Frontend Components (Vanilla JS)**

**Description**
Implement shared UI building blocks: `Modal` (focus trap), `AuthComponent` (login/logout), `GraphUI` (placeholder), `SearchUI` (presentation), plus utilities.

**Learning Goals**
- Modular components with no business logic.  
- BEM CSS, responsive design.  
- Keyboard and screen-reader support.

**Acceptance Criteria**
- [ ] `Modal.js` with focus trap and ESC close.  
- [ ] `AuthComponent.js` basic login form (no token storage yet).  
- [ ] `SearchUI.js` input + results container (no engine).  
- [ ] CSS in `styles/components.css` follows BEM.

**Subtasks**
- [ ] Utility: `dom.js` for qs/qsa, event helpers.  
- [ ] `responsive.css` breakpoints.

**Depends On**: #5

**Suggested Branch**: `feature/issue-8-core-ui`

🚀 **[#57](https://github.com/taimac/tailormaciel.github.io/issues/57)** B07 — Polymorphic File Explorer Component `priority-high, type-feature, learning-oop, component-ui, backlog-import-2025-08`
  _milestone: Milestone 1_

  _author: taimac • created: 2025-08-15T00:42:13Z • comments: 0_

**Backlog ID**: B07

**Issue #7: Polymorphic File Explorer Component**

**Description**
Build the UI explorer that renders folders/files using the common content interface. Include grid/list views, breadcrumbs, and keyboard navigation.

**Learning Goals**
- Polymorphism in UI rendering and events.  
- Accessibility-first navigation.  
- Separation of presentation vs services.

**Acceptance Criteria**
- [ ] `FileExplorer.js` renders polymorphic cards/rows using `getPreviewInfo()`.  
- [ ] Breadcrumbs, back/forward keyboard shortcuts.  
- [ ] A11y: roles, labels, tab order, `aria-live` for updates.  
- [ ] Works for public and (later) private content toggle.

**Subtasks**
- [ ] Grid and list renderer strategies.  
- [ ] Empty/error states.

**Depends On**: #5, #6, #12

**Suggested Branch**: `feature/issue-7-file-explorer-ui`

🚀 **[#56](https://github.com/taimac/tailormaciel.github.io/issues/56)** B06 — Content Type Inheritance Hierarchy `priority-critical, type-feature, learning-oop, component-files, backlog-import-2025-08`
  _milestone: Milestone 1_

  _author: taimac • created: 2025-08-15T00:42:10Z • comments: 0_

**Backlog ID**: B06

**Issue #6: Content Type Inheritance Hierarchy**

**Description**
Create `ContentItem` abstract base and subclasses: `PDFDocument`, `ImageFile`, `TextDocument`, `NotebookFile` (placeholder) with type-specific preview/info behavior. Add `ContentFactory`.

**Learning Goals**
- IS-A vs HAS-A decisions (inheritance vs composition).  
- Overriding & template method pattern.  
- Factory pattern for extensibility.

**Acceptance Criteria**
- [ ] Base class with abstract `getPreviewInfo()` and shared fields.  
- [ ] Subclasses implement preview/metadata logic.  
- [ ] `ContentFactory.createContentItem()` chooses by extension.  
- [ ] Tests: polymorphic `getPreviewInfo()` and factory coverage ≥ 80%.

**Subtasks**
- [ ] UML sketch (doc) for hierarchy.  
- [ ] Edge-case handling for unknown extensions.

**Depends On**: #5

**Suggested Branch**: `feature/issue-6-content-types`

🚀 **[#55](https://github.com/taimac/tailormaciel.github.io/issues/55)** B05 — Base FileSystem Classes with Encapsulation `priority-critical, type-feature, learning-oop, component-files, backlog-import-2025-08`
  _milestone: Milestone 1_

  _author: taimac • created: 2025-08-15T00:42:08Z • comments: 0_

**Backlog ID**: B05

**Issue #5: Base FileSystem Classes with Encapsulation**

**Description**
Create `FileSystemNode`, `ContentFolder`, `ContentFile` classes with private fields, validated paths, and safe operations to list contents and read metadata.

**Learning Goals**
- Encapsulation & SRP in domain modeling.  
- Input/path validation and error handling.  
- Designing testable classes (no DOM access).

**Acceptance Criteria**
- [ ] ES6 modules under `frontend/js/models/`.  
- [ ] Private fields for internal state; getters for safe read.  
- [ ] Unit tests for invalid paths and metadata edge cases.  
- [ ] JSDoc docstrings for each class & method.

**Subtasks**
- [ ] Define interfaces and invariants.  
- [ ] Implement error classes (ValidationError, UnauthorizedError).

**Depends On**: #1, #2

**Suggested Branch**: `feature/issue-5-filesystem-classes`

🚀 **[#54](https://github.com/taimac/tailormaciel.github.io/issues/54)** B04 — Development Environment & Dual Server Setup `priority-high, type-feature, learning-architecture, backlog-import-2025-08`
  _milestone: Milestone 0_

  _author: taimac • created: 2025-08-15T00:42:05Z • comments: 0_

**Backlog ID**: B04

**Issue #4: Development Environment & Dual Server Setup**

**Description**
Provide a script to start both servers (frontend static + Flask backend). Ensure logs are readable and CORS works.

**Learning Goals**
- Manage multi-process dev workflows.  
- Understand cross-origin requests and proxy/CORS trade-offs.  
- Build a clean developer experience.

**Acceptance Criteria**
- [ ] `scripts/start_dev.py` (or shell) starts both servers with helpful output.  
- [ ] Confirmed endpoints reachable: `/` (frontend), `/api/auth/login` (backend).  
- [ ] Clear README section for starting/stopping and ports.  
- [ ] Hot-reload guidance (manual refresh acceptable; optional watchdog).

**Subtasks**
- [ ] Add logging prefixes per process.  
- [ ] Document port collisions and remedies.

**Depends On**: #1, #3

**Suggested Branch**: `feature/issue-4-dev-servers`

🚀 **[#53](https://github.com/taimac/tailormaciel.github.io/issues/53)** B03 — Minimal Flask Backend for Authentication `priority-critical, type-feature, learning-architecture, learning-security, component-auth, backlog-import-2025-08`
  _milestone: Milestone 0_

  _author: taimac • created: 2025-08-15T00:42:03Z • comments: 0_

**Backlog ID**: B03

**Issue #3: Minimal Flask Backend for Authentication**

**Description**
Create a tiny Flask app (3–4 endpoints) for login (JWT), token validate, and private file serving. Include minimal config and CORS. No DB.

**Learning Goals**
- Implement JWT securely (signing, expiration).  
- Learn secure file serving from private directory.  
- Configure CORS and environment variables.

**Acceptance Criteria**
- [ ] `/api/auth/login` issues a JWT upon valid password.  
- [ ] `/api/auth/validate` returns token validity.  
- [ ] `/private/<path>` serves only with valid `Authorization: Bearer` header.  
- [ ] Basic tests for auth success/failure cases.  
- [ ] `backend/requirements.txt` minimal (Flask, PyJWT, Werkzeug).  
- [ ] Security notes: secret management, token TTL, error messages.

**Subtasks**
- [ ] Wire CORS for localhost:3000 → 5000.  
- [ ] Add `.env.example` and config reader.  
- [ ] Unit tests with PyTest/Flask client.

**Depends On**: #1

**Suggested Branch**: `feature/issue-3-flask-auth`

🚀 **[#52](https://github.com/taimac/tailormaciel.github.io/issues/52)** B02 — Metadata System for Content Organization `priority-critical, type-feature, learning-architecture, component-metadata, backlog-import-2025-08`
  _milestone: Milestone 0_

  _author: taimac • created: 2025-08-15T00:42:00Z • comments: 0_

**Backlog ID**: B02

**Issue #2: Metadata System for Content Organization**

**Description**
Define and implement `.metadata.json` per folder to describe files, tags, relationships, and optional attributes (difficulty, created, etc.). Include a schema doc and examples.

**Learning Goals**
- Design JSON schemas for content description.  
- Understand metadata-driven rendering and search without a DB.  
- Practice validation and graceful error handling for malformed JSON.

**Acceptance Criteria**
- [ ] Documented schema with fields: title, description, tags, files[], connections[].  
- [ ] Sample metadata files in `content/public/...` and `content/private/...`.  
- [ ] A small validator (JS or Python) that reports errors with line/file.  
- [ ] Guidelines added to `docs/` on authoring metadata.

**Subtasks**
- [ ] Author `docs/metadata_schema.md` with examples.  
- [ ] Implement `scripts/validate_metadata.py` (or JS) with exit codes.  
- [ ] Run on repo to baseline-fix issues.

**Depends On**: #1

**Suggested Branch**: `feature/issue-2-metadata-schema`

🚀 **[#51](https://github.com/taimac/tailormaciel.github.io/issues/51)** B01 — Hybrid Project Structure & Setup `priority-critical, type-feature, learning-architecture, backlog-import-2025-08`
  _milestone: Milestone 0_

  _author: taimac • created: 2025-08-15T00:41:58Z • comments: 0 • assignees: taimac_

**Backlog ID**: B01

**Issue #1: Hybrid Project Structure & Setup**

**Description**
Create the hybrid skeleton: file-based content (public/private), static frontend, and a minimal backend folder for auth and private file serving. Establish `.gitignore`, base docs, and basic tooling.

**Learning Goals**
- Compare static vs hybrid vs full-backend delivery and their trade-offs.  
- Practice clean project layout aligned with Clean Architecture layers.  
- Understand how file-based content enables versioning and simplicity.

**Acceptance Criteria**
- [ ] Root folders exist: `content/public`, `content/private`, `frontend`, `backend`, `scripts`, `docs`.  
- [ ] Initial HTML (`frontend/index.html`), `frontend/styles/`, `frontend/js/` scaffolds.  
- [ ] `.gitignore`, `README.md`, and this backlog linked in `docs/`.  
- [ ] Local static server command documented (python http.server).  
- [ ] Dev instructions in `docs/SETUP.md` validated end-to-end.

**Subtasks**
- [ ] Create folder tree and placeholder files.  
- [ ] Add basic favicon/assets placeholders.  
- [ ] Verify static serving at `http://localhost:3000` (or chosen port).

**Depends On**: —

**Suggested Branch**: `feature/issue-1-hybrid-structure`

## Closed Pull Requests (5)

❌ **[#49](https://github.com/taimac/tailormaciel.github.io/pull/49)** Feature/issue 39 backend bootstrap
  _author: taimac • created: 2025-08-12T01:07:49Z • comments: 0_

## Issue
Closes #39

## Summary
Implements backend bootstrap (Flask app factory, secure config, dev script). Resolves AA conflicts with security-first architectural decisions.

## Architecture
- Application Factory (create_app) isolates construction.
- Config inheritance (BaseConfig → DevelopmentConfig / ProductionConfig).
- Runtime overlay (apply_runtime_env) separates static vs dynamic settings.
- Clean Architecture layering preserved (infra vs app vs domain vs presentation).

## Security
- secrets.token_urlsafe(32) for SECRET_KEY.
- Input validation via config class mapping.
- No hardcoded secrets.
- Dev script validates environment and key generation.

## OOP Principles
- Factory Pattern (get_config_class / create_app).
- Inheritance (configuration hierarchy).
- Encapsulation (configuration module boundaries).
- Single Responsibility (each function focused).

## Decisions
1. Mapping-based config selection over string formatting (validation & safety).
2. Runtime env application separate from config classes (testability).
3. Enhanced dev script for early failure and security validation.

## Testing / Validation
- Manual health endpoint test.
- Runtime key generation check.
- Import and factory instantiation verification.
(Add pytest refs when tests added.)

## Risks / Follow‑Ups
- Add automated tests (target ≥70%).
- Implement auth (JWT) before private areas.
- Add production security headers & TLS enforcement later.

## Checklist
- [x] Branch targets dev
- [x] Conflicts resolved
- [x] No hardcoded secrets
- [x] Docstrings added
- [x] Pre-commit hook passes
- [ ] Backlog updated (confirm)
- [ ] Create follow-up issues (tests, auth, knowledge base)

## Backlog / Next Issues
- Knowledge Base core domain entities
- Authentication & authorization layer
- Test suite build-out
- CI pipeline

❌ **[#48](https://github.com/taimac/tailormaciel.github.io/pull/48)** Feature/issue 39 backend bootstrap
  _author: taimac • created: 2025-08-10T23:58:28Z • comments: 0 • assignees: taimac_

## Feature: Backend Bootstrap, Configuration Refactor, and Automated Testing (Issue #39)

### What does this PR do?

- Refactors backend configuration to load environment variables at runtime, enabling secure, testable, and extensible settings management.
- Implements and documents the Flask application factory pattern, supporting modularity, testability, and Clean Architecture principles.
- Adds and documents automated tests for configuration and the `/health` endpoint, ensuring correctness, security, and maintainability.
- Integrates a shared test client fixture via `conftest.py` for DRY, scalable test setup.
- Updates documentation and code comments to explain architectural decisions, OOP principles, and security implications.

---

### Why is this important?

- **Teaches OOP Principles**: Demonstrates encapsulation (config logic), abstraction (factory pattern), and single responsibility (test separation).
- **Clean Architecture**: Separates infrastructure (config), application (factory), and presentation (endpoints), with clear dependency direction.
- **Security-First**: Ensures secrets are never hardcoded, endpoints do not leak sensitive data, and tests validate safe behavior.
- **Testability**: All changes are covered by automated tests, supporting TDD and CI/CD readiness.

---

### Architectural Decisions

- **Runtime config overlay**: Defers environment variable loading to runtime for testability and security.
- **Application factory**: Enables modular app creation and supports dependency injection.
- **Shared fixtures**: Centralizes test setup for maintainability and DRY code.

---

### Security Considerations

- No secrets or credentials are committed.
- All configuration is loaded securely from environment variables.
- `/health` endpoint is safe for public monitoring.

---

### Testing Strategy

- Automated tests for configuration and `/health` endpoint.
- Manual and automated validation after every reviewer suggestion.
- All tests pass with `PYTHONPATH=$(pwd) pytest backend/tests`.

---

### Reviewer Checklist

- [ ] OOP and Clean Architecture principles are clearly demonstrated and explained.
- [ ] Security implications are documented and addressed.
- [ ] Automated tests cover all new/changed logic.
- [ ] Code is self-documenting and follows clean code standards.
- [ ] Documentation and backlog are updated.

---

### Linked Issue

Closes #39

---

**Learning Validation Questions:**
- Why is runtime config loading important for testability and security?
- How does the application factory pattern support modularity and maintainability?
- What would break if config was loaded at import time instead of runtime?

---

*This PR is designed to teach and demonstrate professional backend setup, Clean Architecture, OOP, and security-first development. Please review with a focus on learning outcomes and architectural clarity.*

❌ **[#47](https://github.com/taimac/tailormaciel.github.io/pull/47)** docs: close Issue #39 and document backend bootstrap completion
  _author: taimac • created: 2025-08-09T23:23:53Z • comments: 0 • assignees: taimac_

## Feature: Backend Dependencies & Flask Application Bootstrap (Issue #39)

### What does this PR do?

- Sets up the backend Python environment using a virtual environment and pinned `requirements.txt` for reproducibility and security.
- Implements the Flask application using the **application factory pattern** to teach encapsulation, dependency injection, and Clean Architecture.
- Adds configuration management (`config.py`) for clear separation of dev/prod environments and secure handling of secrets.
- Introduces a `/health` endpoint for safe, observable service monitoring, following security-first development.
- Provides a development server startup script (`run_dev.sh`) to automate environment activation and ensure consistent onboarding.
- Updates `docs/SETUP.md` with step-by-step, educational instructions and rationale for every setup decision.

### Why is this important?

- **Teaches Clean Architecture**: Demonstrates separation of concerns, modularity, and dependency direction.
- **OOP Principles**: Applies encapsulation, abstraction, and dependency injection in backend setup.
- **Security-First**: Enforces environment isolation, secure config management, and safe monitoring endpoints.
- **Professional Workflow**: Automates setup and documents every step for new contributors.

### Architectural Decisions

- Adopted the application factory pattern for modular, testable app creation.
- Used environment variables and `.env` files for secure, flexible configuration.
- Isolated backend dependencies and environment from frontend for maintainability and security.

### Security Considerations

- No secrets or credentials are committed.
- `.venv/` and `.env` are included in `.gitignore`.
- Health check endpoint does not expose sensitive information.

### Reviewer Checklist

- [ ] All setup steps are clear and justified in `docs/SETUP.md`
- [ ] Application factory pattern is correctly implemented
- [ ] Configuration management supports both dev and prod
- [ ] Health check endpoint is present and secure
- [ ] Development server script works as documented
- [ ] No secrets or environment folders are tracked in git

### Linked Issue

Closes #39

---

**Questions for Reviewers:**
- Are the setup instructions clear for someone new to Clean Architecture?
- Is the separation between backend and frontend environments well explained?
- Do you see any security or maintainability concerns?

---

*This PR is designed to teach and demonstrate professional backend setup, Clean Architecture, and security-first development. Please provide feedback or questions for further learning!*

❌ **[#46](https://github.com/taimac/tailormaciel.github.io/pull/46)** feat: implement project structure and documentation for Issue #38
  _author: taimac • created: 2025-08-09T15:01:57Z • comments: 0_

## Feature: Project Structure Creation (Issue #38)

### What does this PR do?

- Implements the complete project folder structure following Clean Architecture principles.
- Adds README.md files to all frontend and backend folders, explaining their purpose and architectural mapping.
- Updates `.gitignore` to cover Python, Node.js, frontend assets, secrets, and editor/OS files.
- Ensures backend tests are organized under `backend/tests/` with documentation.
- Updates documentation to reflect new structure.

### Why is this important?

- **Teaches Clean Architecture**: Demonstrates separation of concerns and dependency direction.
- **Supports OOP Principles**: Each folder and README explains encapsulation, abstraction, and reusability.
- **Security-First**: `.gitignore` and folder structure prevent accidental leaks and enforce best practices.
- **Professional Workflow**: Follows feature branch strategy and documentation-driven development.

### Architectural Decisions

- Adopted Clean Architecture folder mapping for both frontend and backend.
- README files in each folder clarify intent and usage for new contributors.
- `.gitignore` prevents sensitive and unnecessary files from being tracked.

### Security Considerations

- No secrets or credentials are committed.
- All user input and output handling is documented for security.
- Folder permissions and structure follow the principle of least privilege.

### Reviewer Checklist

- [ ] Folder structure matches technical requirements in backlog
- [ ] All README.md files are present and clear
- [ ] `.gitignore` is comprehensive and effective
- [ ] No secrets or sensitive files are present
- [ ] Documentation is up to date

### Linked Issue

Closes #38

---

**Questions for Reviewers:**
- Do you see any areas where the folder structure could be improved for clarity or security?
- Are the README explanations clear for someone new to Clean Architecture?
- Is there anything missing from the `.gitignore`?

---

*This PR is designed to teach and demonstrate professional project setup, Clean Architecture, and security-first development. Please provide feedback or questions for further learning!*

❌ **[#45](https://github.com/taimac/tailormaciel.github.io/pull/45)** docs: close Issue #37 - environment setup complete
  _author: taimac • created: 2025-08-08T01:20:50Z • comments: 0_

## Summary

**Feature:** Development Environment Setup & Validation (Issue #37)

This PR establishes a secure, repeatable, and professional development environment for the project.  
It includes:
- Python virtual environment setup
- Dependency management via `requirements.txt`
- Git and VSCode configuration
- Automated environment validation script

---

## Architectural Decisions

- **Why:** Consistent environments prevent "works on my machine" bugs and support onboarding, security, and maintainability.
- **How:** All dependencies are tracked in `requirements.txt` and validated with a script, following Clean Architecture’s principle of clear boundaries and repeatability.
- **OOP Principle:** Encapsulation — the environment is isolated from the system, ensuring predictable behavior.
- **Security:** .gitignore prevents secrets from being committed; validation script ensures only approved tools/versions are used.

---

## Implementation Details

- Created and activated Python virtual environment (`.venv`)
- Added and documented all dependencies in `requirements.txt`
- Configured `.gitignore` for Python, VSCode, and OS artifacts
- Wrote `scripts/validate_environment.py` to check Python, Git, VSCode, and pip versions
- Documented setup steps and learning in `docs/backlog.md`

---

## Testing & Validation

- Ran the validation script to confirm all tools are installed and configured correctly
- Verified `.venv` isolation and dependency installation
- Confirmed `.gitignore` prevents local artifacts from being committed

---

## Security Considerations

- No secrets or credentials are committed
- All dependencies are pinned and auditable
- Defensive scripting prevents misconfiguration

---

## Linked Issues

Closes #37

---

## Learning Notes

- Learned the importance of environment consistency, dependency management, and defensive programming
- Practiced Clean Architecture and OOP encapsulation at the environment level

---

## Closed Issues (18)

✅ **[#50](https://github.com/taimac/tailormaciel.github.io/issues/50)** TEMP: Backlog probe `backlog-import-2025-08`
  _author: taimac • created: 2025-08-15T00:22:28Z • comments: 1_

created via gh to verify perms

**Comments**

- _taimac • 2025-08-15T00:47:54Z_

  Closing probe issue


✅ **[#44](https://github.com/taimac/tailormaciel.github.io/issues/44)** Documentation System Setup `priority-medium, type-documentation, learning-architecture, superseded-by-2025-08`
  _milestone: Milestone 0: Development Environment Ready_

  _author: taimac • created: 2025-08-07T01:57:09Z • comments: 1 • assignees: taimac_

Create comprehensive documentation system with learning progress tracking and architectural decision records.

**Learning Goals**:
- Understand documentation-driven development
- Learn technical writing best practices
- Master architectural decision recording
- Understand the importance of learning documentation

**Acceptance Criteria**:
- [ ] Create comprehensive README.md
- [ ] Set up architectural decision records (ADRs)
- [ ] Create learning progress tracking system
- [ ] Add code documentation standards
- [ ] Create API documentation structure
- [ ] Set up changelog and release notes system

**Technical Requirements**:
```markdown
# docs/adr/001-project-structure.md
# ADR 001: Project Structure Organization

## Status
Accepted

## Context
Need to organize project structure to support Clean Architecture principles and educational objectives.

## Decision
Adopt folder structure that maps directly to Clean Architecture layers.

## Consequences
- Clear separation of concerns
- Easy to understand code organization
- Supports learning objectives
- May seem over-engineered for simple features initially
```

**Sub-tasks**:
- [ ] Create comprehensive README
- [ ] Set up ADR documentation system
- [ ] Create learning progress templates
- [ ] Add code documentation standards
- [ ] Create API documentation structure
- [ ] Set up automated documentation generation

**Comments**

- _taimac • 2025-08-15T01:12:52Z_

  This legacy issue is superseded by the Aug 2025 Backlog items: B32 B33 B34 (Backlog IDs). Closing to reduce noise while preserving history.


✅ **[#43](https://github.com/taimac/tailormaciel.github.io/issues/43)** CI/CD Setup & GitHub Integration `priority-medium, type-feature, learning-architecture, superseded-by-2025-08`
  _milestone: Milestone 0: Development Environment Ready_

  _author: taimac • created: 2025-08-07T01:52:31Z • comments: 1 • assignees: taimac_

Set up basic CI/CD pipeline with GitHub Actions for automated testing and code quality checks.

**Learning Goals**:
- Understand continuous integration benefits
- Learn GitHub Actions configuration
- Master automated testing workflows
- Understand deployment pipeline concepts

**Acceptance Criteria**:
- [ ] Create GitHub Actions workflow for testing
- [ ] Add code quality checks to CI pipeline
- [ ] Set up branch protection rules
- [ ] Create pull request template
- [ ] Add issue templates for different types
- [ ] Configure automated project management

**Technical Requirements**:
```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, dev ]
  pull_request:
    branches: [ main, dev ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.8'
    
    - name: Install dependencies
      run: |
        cd backend
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        cd backend
        python -m pytest tests/ -v --cov=backend
    
    - name: Run linting
      run: |
        cd backend
        python -m flake8 . --count --max-line-length=88
```

**Sub-tasks**:
- [ ] Create GitHub Actions workflow
- [ ] Set up automated testing
- [ ] Add code quality checks
- [ ] Configure branch protection
- [ ] Create PR and issue templates
- [ ] Test CI/CD pipeline works

**Comments**

- _taimac • 2025-08-15T01:12:45Z_

  This legacy issue is superseded by the Aug 2025 Backlog items: B27 B28 B29 B31 B39 (Backlog IDs). Closing to reduce noise while preserving history.


✅ **[#42](https://github.com/taimac/tailormaciel.github.io/issues/42)** Development Tools & Scripts Setup `priority-high, type-feature, learning-architecture, superseded-by-2025-08`
  _milestone: Milestone 0: Development Environment Ready_

  _author: taimac • created: 2025-08-07T01:48:58Z • comments: 1 • assignees: taimac_

Create development utility scripts for common tasks like running tests, code formatting, and project management.

**Learning Goals**:
- Understand development automation benefits
- Learn script organization and documentation
- Master code quality tools configuration
- Understand professional development workflows

**Acceptance Criteria**:
- [ ] Create test runner script with coverage reporting
- [ ] Add code formatting and linting scripts
- [ ] Create database management scripts
- [ ] Add development server startup scripts
- [ ] Include project validation and health check scripts
- [ ] Create comprehensive development documentation

**Technical Requirements**:
```python
# scripts/run_tests.py
import subprocess
import sys

def run_backend_tests():
    """Run backend tests with coverage reporting"""
    print("Running backend tests...")
    result = subprocess.run([
        'python', '-m', 'pytest', 
        'backend/tests/', 
        '-v', 
        '--cov=backend',
        '--cov-report=term-missing'
    ], cwd='backend')
    return result.returncode == 0

def run_frontend_tests():
    """Run frontend tests"""
    print("Running frontend tests...")
    # Implementation for frontend testing
    return True

if __name__ == '__main__':
    backend_passed = run_backend_tests()
    frontend_passed = run_frontend_tests()
    
    if backend_passed and frontend_passed:
        print("✅ All tests passed!")
        sys.exit(0)
    else:
        print("❌ Some tests failed!")
        sys.exit(1)
```

**Sub-tasks**:
- [ ] Create test runner script
- [ ] Add code quality check script
- [ ] Create database utility scripts
- [ ] Add development server scripts
- [ ] Create project health check script
- [ ] Document all scripts and their usage

**Comments**

- _taimac • 2025-08-15T01:12:49Z_

  This legacy issue is superseded by the Aug 2025 Backlog items: B25 B26 B27 B28 B29 B30 B31 (Backlog IDs). Closing to reduce noise while preserving history.


✅ **[#41](https://github.com/taimac/tailormaciel.github.io/issues/41)** Frontend Basic Structure & Build Setup `priority-critical, type-feature, learning-architecture, layer-presentation, superseded-by-2025-08`
  _milestone: Milestone 0: Development Environment Ready_

  _author: taimac • created: 2025-08-07T01:42:53Z • comments: 1 • assignees: taimac_

Create basic HTML structure and set up simple build/serve process for frontend development.

**Learning Goals**:
- Understand semantic HTML structure
- Learn CSS organization and methodology
- Master basic build processes without complex tooling
- Understand the progression from simple to complex build tools

**Acceptance Criteria**:
- [ ] Create semantic HTML5 structure
- [ ] Set up CSS organization with BEM methodology
- [ ] Create basic JavaScript module structure
- [ ] Add simple development server setup
- [ ] Include basic responsive design foundation
- [ ] Create frontend development documentation

**Technical Requirements**:
```html
<!-- index.html structure -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Website & Knowledge Base</title>
    <link rel="stylesheet" href="styles/main.css">
</head>
<body>
    <nav class="navigation">
        <!-- Navigation component will be rendered here -->
    </nav>
    
    <main class="main-content">
        <section class="hero">
            <!-- Hero section -->
        </section>
        
        <section class="content-grid">
            <!-- Dynamic content will be rendered here -->
        </section>
    </main>
    
    <script type="module" src="js/main.js"></script>
</body>
</html>
```

**Sub-tasks**:
- [ ] Create semantic HTML5 structure
- [ ] Set up CSS file organization
- [ ] Create basic CSS reset and variables
- [ ] Add responsive design foundation
- [ ] Set up JavaScript module structure
- [ ] Create development server options
- [ ] Test frontend serves correctly

**Comments**

- _taimac • 2025-08-15T01:12:41Z_

  This legacy issue is superseded by the Aug 2025 Backlog items: B19 B20 B21 B22 B23 B24 (Backlog IDs). Closing to reduce noise while preserving history.


✅ **[#40](https://github.com/taimac/tailormaciel.github.io/issues/40)** Database Setup & Initial Schema `priority-critical, type-feature, learning-architecture, layer-infrastructure, superseded-by-2025-08`
  _milestone: Milestone 0: Development Environment Ready_

  _author: taimac • created: 2025-08-07T01:39:58Z • comments: 2 • assignees: taimac_

Set up SQLite database with initial schema and database management utilities.

**Learning Goals**:
- Understand database schema design principles
- Learn database initialization and migration concepts
- Master SQLite setup for development
- Understand the progression path to PostgreSQL

**Acceptance Criteria**:
- [ ] Create database initialization script
- [ ] Design initial schema for users and content
- [ ] Create database connection management
- [ ] Add sample data seeding script
- [ ] Implement basic database utilities
- [ ] Create database reset/rebuild script

**Technical Requirements**:
```python
# init_database.py
import sqlite3
from datetime import datetime

def init_database():
    conn = sqlite3.connect('development.db')
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Content items table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS content_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(200) NOT NULL,
            content TEXT,
            type VARCHAR(50) NOT NULL,
            user_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    conn.commit()
    conn.close()
```

**Sub-tasks**:
- [ ] Design entity-relationship diagram
- [ ] Create database initialization script
- [ ] Add database connection utilities  
- [ ] Create sample data generation
- [ ] Add database reset functionality
- [ ] Test database operations work correctly

**Comments**

- _taimac • 2025-08-12T23:48:38Z_

  Close as superseded: Database deferred by new hosting/data strategy.

Decision:
- Adopt hybrid approach: GitHub Pages (UI, thumbnails, static JSON graph) + object storage (R2/B2/S3) for originals.
- Use a file-based knowledge graph (nodes/edges JSON). No database initially.

Why:
- Pages 1 GB limit; media library will exceed several GBs.
- Object storage is cheaper/scalable for PDFs/images.
- Private docs can use presigned URLs after auth.
- Clean migration path to DB later (editing, multi-user, rich search).

Replacements (tracked in docs/project_backlog.md):
- Public graph generator + sidecar metadata
- Thumbnails/WebP pipeline
- Storage integration (public base URL)
- Private presigned download flow + minimal auth
- Unified /api/graph (public+private) and simple graph viewer

Migration plan (later):
- Map Node/Edge JSON to relational schema; add migrations (Alembic).
"

# Close and label (optional)
gh issue edit 40 --state closed --add-label "deferred"

- _taimac • 2025-08-15T01:12:57Z_

  We pivoted to a file-based metadata approach (no DB) for MVP. Superseded by Backlog IDs B02 and B10.


✅ **[#39](https://github.com/taimac/tailormaciel.github.io/issues/39)** Backend Dependencies & Flask Application Bootstrap `priority-critical, type-feature, learning-architecture, layer-infrastructure, backlog-import-2025-08`
  _milestone: Milestone 0: Development Environment Ready_

  _author: taimac • created: 2025-08-07T01:35:58Z • comments: 3 • assignees: taimac_

Install backend dependencies and create minimal Flask application with proper application factory pattern.

**Learning Goals**:
- Understand dependency management with requirements.txt
- Learn Flask application factory pattern
- Master configuration management concepts
- Understand the difference between development and production setups

**Acceptance Criteria**:
- [ ] Create requirements.txt with all necessary dependencies
- [ ] Install dependencies in virtual environment
- [ ] Create Flask application using factory pattern
- [ ] Set up configuration management (dev/prod)
- [ ] Create basic health check endpoint
- [ ] Add development server startup script

**Technical Requirements**:
```python
# requirements.txt content
Flask==2.3.3
SQLAlchemy==2.0.21
PyJWT==2.8.0
Werkzeug==2.3.7
pytest==7.4.2
black==23.7.0
flake8==6.0.0
python-dotenv==1.0.0

# Basic app.py structure
from flask import Flask

def create_app(config_name='development'):
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(f'config.{config_name.title()}Config')
    
    # Register blueprints
    from controllers import auth_bp, content_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(content_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
```

**Sub-tasks**:
- [x] Research and document dependency choices
- [x] Create requirements.txt with pinned versions
- [x] Install dependencies with pip
- [x] Create config.py with development/production configs
- [x] Implement application factory pattern
- [x] Add basic route for health check
- [x] Create development startup script
- [x] Test application starts without errors

**Comments**

- _taimac • 2025-08-09T23:17:52Z_

  Issue #39: Backend Dependencies & Flask Application Bootstrap — Completed

All acceptance criteria have been met:

✅ requirements.txt created and pinned for reproducibility and security
✅ Virtual environment setup and documented for environment isolation
✅ Flask application implemented using the application factory pattern (teaches encapsulation, dependency injection, and Clean Architecture)
✅ Configuration management (config.py) supports dev/prod separation and secure environment variables
✅ Health check endpoint (/health) added for safe monitoring and infrastructure integration
✅ Development server startup script (run_dev.sh) automates safe, repeatable onboarding
✅ All steps and architectural decisions documented in [SETUP.md](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) with educational explanations
Teaching Notes:
This issue demonstrates how to bootstrap a secure, maintainable backend using Clean Architecture and OOP p...

- _taimac • 2025-08-10T23:52:39Z_

  Issue #39: Backend Dependencies & Flask Application Bootstrap — Complete

Solution & Implementation:

Pulled and integrated Copilot’s review suggestions into your feature branch.
Refactored configuration management for testability and security (runtime env overlay, OOP encapsulation).
Ensured application factory pattern is used for modular, testable app creation.
Added and passed automated tests:
test_config.py: Validates dev/prod config, environment variable handling, and security.
test_health.py: Verifies /health endpoint is safe, correct, and does not leak sensitive info.
Used fixtures and conftest.py for DRY, scalable test setup.
Ran all tests with explicit PYTHONPATH to confirm import correctness and maintainability.
Documented and explained every architectural and security decision in code and workflow.

All reviewer suggestions integrated and tested.
Configuration, application factory, and health endpoint are secure, modular, and fully covered by automated tests.
All code and te...

- _taimac • 2025-08-12T01:32:20Z_

  Backend Bootstrap Complete – Merge & Conflict Resolution Summary

The backend bootstrap for the project is now complete and merged into dev.

Key highlights and decisions from this work:

Application Factory Pattern: Implemented a secure, extensible Flask app factory with clear separation of concerns.
Configuration Management: Used OOP inheritance for config classes and a factory method for safe environment selection.
Security-First Approach: All secrets are loaded from environment variables or generated securely (secrets.token_urlsafe(32)), eliminating hardcoded keys.
AA Merge Conflict Resolution: Both branches had independently added backend files. Resolved by selecting the implementation with stronger security and architectural patterns, then enhanced with additional documentation and error handling.
Pre-commit Quality Pipeline: Established automated checks for whitespace, formatting, and linting to maintain code quality.
Comprehensive Documentation: All major classes and functions ...


✅ **[#38](https://github.com/taimac/tailormaciel.github.io/issues/38)** Project Structure Creation `priority-critical, type-feature, learning-architecture`
  _milestone: Milestone 0: Development Environment Ready_

  _author: taimac • created: 2025-08-07T01:27:05Z • comments: 1 • assignees: taimac_

Create complete project folder structure following Clean Architecture principles and professional organization.

**Learning Goals**:
- Understand project organization best practices
- Learn Clean Architecture folder mapping
- Master separation of concerns through structure
- Understand the relationship between folder structure and code architecture

**Acceptance Criteria**:
- [ ] Create complete folder structure as per architecture guide
- [ ] Add README.md files explaining each folder's purpose
- [ ] Create __init__.py files for Python packages
- [ ] Add placeholder files to maintain folder structure in Git
- [ ] Include proper .gitignore for Python and frontend assets
- [ ] Validate structure with automated script

**Technical Requirements**:
```
personal-website/
├── docs/                    # Documentation
├── frontend/               # Client-side code
│   ├── js/
│   │   ├── components/     # UI Components
│   │   ├── services/       # Business logic
│   │   └── utils/          # Utilities
│   ├── styles/             # CSS files
│   └── assets/             # Static resources
├── backend/                # Server-side code
│   ├── models/             # Domain layer
│   ├── services/           # Application layer
│   ├── controllers/        # Presentation layer
│   ├── repositories/       # Infrastructure layer
│   ├── middleware/         # Cross-cutting concerns
│   └── tests/              # Test files
└── scripts/                # Development utilities
```

**Sub-tasks**:
- [ ] Create main project folders
- [ ] Add layer-specific subfolders for backend
- [ ] Create frontend component organization
- [ ] Add documentation folder structure
- [ ] Create test folder hierarchy
- [ ] Add README.md files explaining each folder
- [ ] Create .gitignore with appropriate patterns

**Comments**

- _taimac • 2025-08-09T15:14:40Z_

  **Issue #38: Project Structure Creation — Completed**

All acceptance criteria have been met:

- ✅ Complete folder structure implemented following Clean Architecture principles
- ✅ README.md files added to each major folder, explaining architectural purpose and OOP/security considerations
- ✅ Python package `__init__.py` and placeholder files included where needed
- ✅ Comprehensive .gitignore covers backend, frontend, secrets, and build artifacts
- ✅ Automated validation and documentation updated

**Teaching Notes:**  
This issue demonstrates how Clean Architecture enforces separation of concerns, supports maintainability, and improves onboarding for new contributors. Each folder’s README clarifies its role in the architecture, and the .gitignore ensures security and professionalism by preventing accidental commits of sensitive or unnecessary files.

**Next Steps:**  
- Continue applying these architectural and documentation standards to all new features.
- Use this structure as a refe...


✅ **[#37](https://github.com/taimac/tailormaciel.github.io/issues/37)** Development Environment Setup & Validation `priority-critical, type-feature, learning-architecture`
  _milestone: Milestone 0: Development Environment Ready_

  _author: taimac • created: 2025-08-07T01:14:08Z • comments: 1 • assignees: taimac_

Set up complete development environment with proper Python virtual environment, Git configuration, and editor setup.

**Learning Goals**:
- Understand virtual environment isolation and dependency management
- Learn professional Git workflow setup
- Master development tool configuration
- Understand the importance of environment consistency

**Acceptance Criteria**:
- [x] Python 3.8+ installed and verified
- [x] Git installed with proper user configuration
- [x] VSCode installed with required extensions
- [x] Virtual environment created and activated
- [x] Git repository initialized with proper .gitignore
- [x] Environment validation script runs successfully

**Technical Requirements**:
```bash
# Environment validation checklist
python --version  # Must be 3.8+
git --version
code --version  # VSCode
which pip  # Should point to venv pip after activation
```

**Sub-tasks**:
- [x] Install Python 3.8+ from python.org
- [x] Install Git and configure user.name/user.email
- [x] Install VSCode with Python and GitHub Copilot extensions
- [x] Create and test virtual environment
- [x] Initialize Git repository with initial commit
- [x] Create environment validation script

**Definition of Done**:
- All software installed and verified
- Virtual environment working correctly
- Git repository initialized
- Validation script passes all checks
- Documentation updated with setup instructions

**Comments**

- _taimac • 2025-08-08T02:14:38Z_

  Summary:

All acceptance criteria for environment setup and validation have been met.

Python, Git, and VSCode are installed and validated.
Virtual environment and [.gitignore](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) are configured.
All dependencies are managed in [requirements.txt](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html).
An automated environment validation script ensures consistency and security.
Documentation and learning notes have been updated in [backlog.md](vscode-file://vscode-app/usr/share/code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html).
Learning Outcomes:

Understood the importance of repeatable, secure environment setup for professional projects.
Practiced defensive programming and dependency management.
Reinforced Clean Architecture and OOP encapsulation at the environment level.


✅ **[#36](https://github.com/taimac/tailormaciel.github.io/issues/36)** EPIC 8: Performance & Production Readiness `priority-low, type-epic, superseded-by-2025-08`
  _milestone: Milestone 4: Advanced Features & Production Ready_

  _author: taimac • created: 2025-08-06T16:37:40Z • comments: 1 • assignees: taimac_

Optimize performance and prepare for production deployment.

Learning Goals: 

Understand production considerations and optimization techniques

**Comments**

- _taimac • 2025-08-15T01:12:07Z_

  This legacy issue is superseded by the Aug 2025 Backlog items: B35 B36 B37 B38 B39 (Backlog IDs). Closing to reduce noise while preserving history.


✅ **[#35](https://github.com/taimac/tailormaciel.github.io/issues/35)** EPIC 7: Knowledge Base Features `priority-medium, type-epic, component-knowledge, superseded-by-2025-08`
  _milestone: Milestone 4: Advanced Features & Production Ready_

  _author: taimac • created: 2025-08-06T16:36:06Z • comments: 1 • assignees: taimac_

Build intelligent knowledge base with graph connections and search.

Learning Goals: 

Apply all learned concepts to complex feature implementation

**Comments**

- _taimac • 2025-08-15T01:12:03Z_

  This legacy issue is superseded by the Aug 2025 Backlog items: B10 B11 B13 B14 B15 (Backlog IDs). Closing to reduce noise while preserving history.


✅ **[#34](https://github.com/taimac/tailormaciel.github.io/issues/34)** EPIC 6: Testing & Quality Assurance `priority-high, type-epic, learning-testing, superseded-by-2025-08`
  _milestone: Milestone 4: Advanced Features & Production Ready_

  _author: taimac • created: 2025-08-06T16:34:09Z • comments: 3 • assignees: taimac_

Implement comprehensive testing strategy with TDD approach.

Learning Goals: 
Master testing principles and achieve 70%+ coverage

**Comments**

- _taimac • 2025-08-15T01:07:21Z_

  This legacy issue is superseded by the Aug 2025 Backlog items: B28 B29 B30 B31 (Backlog IDs). Closing to reduce noise while preserving history.

- _taimac • 2025-08-15T01:08:52Z_

  This legacy issue is superseded by the Aug 2025 Backlog items: B28 B29 B30 B31 (Backlog IDs). Closing to reduce noise while preserving history.

- _taimac • 2025-08-15T01:11:59Z_

  This legacy issue is superseded by the Aug 2025 Backlog items: B28 B29 B30 B31 (Backlog IDs). Closing to reduce noise while preserving history.


✅ **[#33](https://github.com/taimac/tailormaciel.github.io/issues/33)** EPIC 5: Design Patterns Implementation `priority-medium, type-epic, learning-patterns, superseded-by-2025-08`
  _milestone: Milestone 4: Advanced Features & Production Ready_

  _author: taimac • created: 2025-08-06T16:32:27Z • comments: 1 • assignees: taimac_

Apply classic design patterns to solve common software problems.

Learning Goals: 
Master pattern recognition and appropriate pattern application

**Comments**

- _taimac • 2025-08-15T01:12:28Z_

  This legacy issue is superseded by the Aug 2025 Backlog items: B06 B09 B12 B15 (Backlog IDs). Closing to reduce noise while preserving history.


✅ **[#32](https://github.com/taimac/tailormaciel.github.io/issues/32)** EPIC 4: Frontend OOP & Component Architecture `priority-high, type-epic, learning-oop, component-ui, superseded-by-2025-08`
  _milestone: Milestone 2: Knowledge Graph & Search System_

  _author: taimac • created: 2025-08-06T16:29:32Z • comments: 1 • assignees: taimac_

Apply OOP principles to frontend JavaScript with component-based architecture.

Learning Goals: 
Master JavaScript classes and modular component design

**Comments**

- _taimac • 2025-08-15T01:12:24Z_

  This legacy issue is superseded by the Aug 2025 Backlog items: B07 B08 B19 B20 B21 B22 B23 B24 (Backlog IDs). Closing to reduce noise while preserving history.


✅ **[#31](https://github.com/taimac/tailormaciel.github.io/issues/31)** EPIC 3: Security-First Development `priority-high, type-epic, learning-security, superseded-by-2025-08`
  _milestone: Milestone 3: Authentication & Private Content_

  _author: taimac • created: 2025-08-06T16:27:03Z • comments: 1 • assignees: taimac_

Implement comprehensive security measures throughout all layers.

**Learning Goals**: 

Master security principles and common vulnerability prevention

**Comments**

- _taimac • 2025-08-15T01:12:20Z_

  This legacy issue is superseded by the Aug 2025 Backlog items: B16 B17 B18 B31 (Backlog IDs). Closing to reduce noise while preserving history.


✅ **[#30](https://github.com/taimac/tailormaciel.github.io/issues/30)** EPIC 2: Clean Architecture Foundation `priority-critical, type-epic, learning-architecture, superseded-by-2025-08`
  _milestone: Milestone 2: Knowledge Graph & Search System_

  _author: taimac • created: 2025-08-06T16:23:19Z • comments: 1 • assignees: taimac_

Implement proper layer separation with clear boundaries and dependency rules.

**Learning Goals**: 
Master Clean Architecture principles with hands-on layer implementation

**Comments**

- _taimac • 2025-08-15T01:12:11Z_

  This legacy issue is superseded by the Aug 2025 Backlog items: B12 B32 B33 B34 (Backlog IDs). Closing to reduce noise while preserving history.


✅ **[#29](https://github.com/taimac/tailormaciel.github.io/issues/29)** EPIC 1: OOP Fundamentals Implementation `priority-critical, type-epic, learning-oop, superseded-by-2025-08`
  _milestone: Milestone 1: File-Based Foundation & OOP Fundamentals_

  _author: taimac • created: 2025-08-06T16:21:11Z • comments: 1 • assignees: taimac_

Establish solid OOP foundation with practical examples demonstrating all four core principles.

**Learning Goals**: 
Master encapsulation, inheritance, polymorphism, and abstraction through hands-on coding

**Comments**

- _taimac • 2025-08-15T01:12:32Z_

  This legacy issue is superseded by the Aug 2025 Backlog items: B05 B06 B07 B08 (Backlog IDs). Closing to reduce noise while preserving history.


✅ **[#28](https://github.com/taimac/tailormaciel.github.io/issues/28)** EPIC 0: Hybrid Project Foundation (File-Based + Minimal Backend) `priority-critical, type-epic, learning-architecture, superseded-by-2025-08`
  _milestone: Milestone 0: Development Environment Ready_

  _author: taimac • created: 2025-08-06T16:16:50Z • comments: 1 • assignees: taimac_

Set up file-based knowledge system with minimal backend for authentication and private file serving Learning Goals: Understand hybrid architecture, static site principles, and when to use minimal backend vs full application

**Comments**

- _taimac • 2025-08-15T01:12:36Z_

  This legacy issue is superseded by the Aug 2025 Backlog items: B01 B02 B03 B04 (Backlog IDs). Closing to reduce noise while preserving history.


