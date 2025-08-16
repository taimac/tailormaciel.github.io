# GitHub Project Backlog — Personal Website & File‑Based Knowledge Base (Full, Expanded)

---

## 🔗 Reference

* **Architecture & Patterns**: `docs/OOP_Architectur_Guide.md`
* **Setup Guide**: `docs/SETUP.md`
* **Daily Workflow**: `docs/Daily_Development_Routine.md`
* **Knowledge Base Structure**: `docs/Simplified_Knowledge_Base_Architecture.md`

---

## 🏷️ Labels System (use in GitHub)

**Priority**: `priority-critical`, `priority-high`, `priority-medium`, `priority-low`
**Type**: `type-epic`, `type-feature`, `type-bug`, `type-enhancement`, `type-refactor`, `type-documentation`
**Learning Focus**: `learning-oop`, `learning-architecture`, `learning-security`, `learning-patterns`, `learning-frontend`
**Component**: `component-files`, `component-metadata`, `component-graph`, `component-auth`, `component-ui`, `component-utilities`, `component-testing`, `component-docs`, `component-performance`

---

## 🔧 Conventions & Definition of Done (DoD)

**Branch Strategy**: `feature/issue-<N>-short-slug` → PR into `dev` (never `main`).

**DoD for every issue**

* [ ] 70%+ test coverage for changed area (unit or integration as appropriate)
* [ ] A11y pass for UI work (keyboard, labels, focus order)
* [ ] Security notes added if input/auth/tokens involved
* [ ] Docstrings/comments explain business purpose and design decisions
* [ ] `docs/CHANGELOG.md` entry & any affected docs updated
* [ ] All linters/formatters/CI checks pass; pre-commit hook clean

---

## 🎯 Milestones & Success Criteria

### Milestone 0: Development Environment Ready (Week 1)

* **Success**: Environment set up, static file serving, docs in place.

### Milestone 1: File‑Based Foundation & OOP Fundamentals (Week 3)

* **Success**: File explorer, metadata system, basic viewing.

### Milestone 2: Knowledge Graph & Search System (Week 5)

* **Success**: Knowledge graph, search, tagging/filtering.

### Milestone 3: Authentication & Private Content (Week 7)

* **Success**: Auth, public/private separation, session management.

### Milestone 4: Advanced Features & Production Ready (Week 8)

* **Success**: Mobile design, performance optimization, full docs.

---

## 📚 Epics & Issues (expanded for GitHub Project use)

> Each issue below is formatted for copy/paste into a GitHub Issue. Include labels, milestone, and link dependencies in the issue description.

---

# EPIC 0: Hybrid Project Foundation — **Milestone 0**

**Labels**: `type-epic`, `learning-architecture`, `priority-critical`

### Issue #1: Hybrid Project Structure & Setup

**Labels**: `type-feature`, `learning-architecture`, `priority-critical`
**Milestone**: 0
**Depends On**: —
**Suggested Branch**: `feature/issue-1-hybrid-structure`

**Description**
Create the hybrid skeleton: file-based content (public/private), static frontend, and a minimal backend folder for auth and private file serving. Establish `.gitignore`, base docs, and basic tooling.

**Learning Goals**

* Compare static vs hybrid vs full-backend delivery and their trade-offs.
* Practice clean project layout aligned with Clean Architecture layers.
* Understand how file-based content enables versioning and simplicity.

**Acceptance Criteria**

* [ ] Root folders exist: `content/public`, `content/private`, `frontend`, `backend`, `scripts`, `docs`.
* [ ] Initial HTML (`frontend/index.html`), `frontend/styles/`, `frontend/js/` scaffolds.
* [ ] `.gitignore`, `README.md`, and this backlog linked in `docs/`.
* [ ] Local static server command documented (python http.server).
* [ ] Dev instructions in `docs/SETUP.md` validated end-to-end.

**Subtasks**

* [ ] Create folder tree and placeholder files.
* [ ] Add basic favicon/assets placeholders.
* [ ] Verify static serving at `http://localhost:3000` (or chosen port).

---

### Issue #2: Metadata System for Content Organization

**Labels**: `type-feature`, `learning-architecture`, `component-metadata`, `priority-critical`
**Milestone**: 0
**Depends On**: #1
**Suggested Branch**: `feature/issue-2-metadata-schema`

**Description**
Define and implement `.metadata.json` per folder to describe files, tags, relationships, and optional attributes (difficulty, created, etc.). Include a schema doc and examples.

**Learning Goals**

* Design JSON schemas for content description.
* Understand metadata-driven rendering and search without a DB.
* Practice validation and graceful error handling for malformed JSON.

**Acceptance Criteria**

* [ ] Documented schema with fields: title, description, tags, files\[], connections\[].
* [ ] Sample metadata files in `content/public/...` and `content/private/...`.
* [ ] A small validator (JS or Python) that reports errors with line/file.
* [ ] Guidelines added to `docs/` on authoring metadata.

**Subtasks**

* [ ] Author `docs/metadata_schema.md` with examples.
* [ ] Implement `scripts/validate_metadata.py` (or JS) with exit codes.
* [ ] Run on repo to baseline-fix issues.

---

### Issue #3: Minimal Flask Backend for Authentication

**Labels**: `type-feature`, `learning-architecture`, `learning-security`, `component-auth`, `priority-critical`
**Milestone**: 0
**Depends On**: #1
**Suggested Branch**: `feature/issue-3-flask-auth`

**Description**
Create a tiny Flask app (3–4 endpoints) for login (JWT), token validate, and private file serving. Include minimal config and CORS. No DB.

**Learning Goals**

* Implement JWT securely (signing, expiration).
* Learn secure file serving from private directory.
* Configure CORS and environment variables.

**Acceptance Criteria**

* [ ] `/api/auth/login` issues a JWT upon valid password.
* [ ] `/api/auth/validate` returns token validity.
* [ ] `/private/<path>` serves only with valid `Authorization: Bearer` header.
* [ ] Basic tests for auth success/failure cases.
* [ ] `backend/requirements.txt` minimal (Flask, PyJWT, Werkzeug).
* [ ] Security notes: secret management, token TTL, error messages.

**Subtasks**

* [ ] Wire CORS for localhost:3000 → 5000.
* [ ] Add `.env.example` and config reader.
* [ ] Unit tests with PyTest/Flask client.

---

### Issue #4: Development Environment & Dual Server Setup

**Labels**: `type-feature`, `learning-architecture`, `priority-high`
**Milestone**: 0
**Depends On**: #1, #3
**Suggested Branch**: `feature/issue-4-dev-servers`

**Description**
Provide a script to start both servers (frontend static + Flask backend). Ensure logs are readable and CORS works.

**Learning Goals**

* Manage multi-process dev workflows.
* Understand cross-origin requests and proxy/CORS trade-offs.
* Build a clean developer experience.

**Acceptance Criteria**

* [ ] `scripts/start_dev.py` (or shell) starts both servers with helpful output.
* [ ] Confirmed endpoints reachable: `/` (frontend), `/api/auth/login` (backend).
* [ ] Clear README section for starting/stopping and ports.
* [ ] Hot-reload guidance (manual refresh acceptable; optional watchdog).

**Subtasks**

* [ ] Add logging prefixes per process.
* [ ] Document port collisions and remedies.

---

# EPIC 1: OOP File Explorer & Content Management — **Milestone 1**

**Labels**: `type-epic`, `learning-oop`, `priority-critical`

### Issue #5: Base FileSystem Classes with Encapsulation

**Labels**: `type-feature`, `learning-oop`, `component-files`, `priority-critical`
**Milestone**: 1
**Depends On**: #1, #2
**Suggested Branch**: `feature/issue-5-filesystem-classes`

**Description**
Create `FileSystemNode`, `ContentFolder`, `ContentFile` classes with private fields, validated paths, and safe operations to list contents and read metadata.

**Learning Goals**

* Encapsulation & SRP in domain modeling.
* Input/path validation and error handling.
* Designing testable classes (no DOM access).

**Acceptance Criteria**

* [ ] ES6 modules under `frontend/js/models/`.
* [ ] Private fields for internal state; getters for safe read.
* [ ] Unit tests for invalid paths and metadata edge cases.
* [ ] JSDoc docstrings for each class & method.

**Subtasks**

* [ ] Define interfaces and invariants.
* [ ] Implement error classes (ValidationError, UnauthorizedError).

---

### Issue #6: Content Type Inheritance Hierarchy

**Labels**: `type-feature`, `learning-oop`, `component-files`, `priority-critical`
**Milestone**: 1
**Depends On**: #5
**Suggested Branch**: `feature/issue-6-content-types`

**Description**
Create `ContentItem` abstract base and subclasses: `PDFDocument`, `ImageFile`, `TextDocument`, `NotebookFile` (placeholder) with type-specific preview/info behavior. Add `ContentFactory`.

**Learning Goals**

* IS-A vs HAS-A decisions (inheritance vs composition).
* Overriding & template method pattern.
* Factory pattern for extensibility.

**Acceptance Criteria**

* [ ] Base class with abstract `getPreviewInfo()` and shared fields.
* [ ] Subclasses implement preview/metadata logic.
* [ ] `ContentFactory.createContentItem()` chooses by extension.
* [ ] Tests: polymorphic `getPreviewInfo()` and factory coverage ≥ 80%.

**Subtasks**

* [ ] UML sketch (doc) for hierarchy.
* [ ] Edge-case handling for unknown extensions.

---

### Issue #7: Polymorphic File Explorer Component

**Labels**: `type-feature`, `learning-oop`, `component-ui`, `priority-high`
**Milestone**: 1
**Depends On**: #5, #6, #12
**Suggested Branch**: `feature/issue-7-file-explorer-ui`

**Description**
Build the UI explorer that renders folders/files using the common content interface. Include grid/list views, breadcrumbs, and keyboard navigation.

**Learning Goals**

* Polymorphism in UI rendering and events.
* Accessibility-first navigation.
* Separation of presentation vs services.

**Acceptance Criteria**

* [ ] `FileExplorer.js` renders polymorphic cards/rows using `getPreviewInfo()`.
* [ ] Breadcrumbs, back/forward keyboard shortcuts.
* [ ] A11y: roles, labels, tab order, `aria-live` for updates.
* [ ] Works for public and (later) private content toggle.

**Subtasks**

* [ ] Grid and list renderer strategies.
* [ ] Empty/error states.

---

### Issue #8: Core Frontend Components (Vanilla JS)

**Labels**: `type-feature`, `learning-frontend`, `component-ui`, `priority-critical`
**Milestone**: 1
**Depends On**: #5
**Suggested Branch**: `feature/issue-8-core-ui`

**Description**
Implement shared UI building blocks: `Modal` (focus trap), `AuthComponent` (login/logout), `GraphUI` (placeholder), `SearchUI` (presentation), plus utilities.

**Learning Goals**

* Modular components with no business logic.
* BEM CSS, responsive design.
* Keyboard and screen-reader support.

**Acceptance Criteria**

* [ ] `Modal.js` with focus trap and ESC close.
* [ ] `AuthComponent.js` basic login form (no token storage yet).
* [ ] `SearchUI.js` input + results container (no engine).
* [ ] CSS in `styles/components.css` follows BEM.

**Subtasks**

* [ ] Utility: `dom.js` for qs/qsa, event helpers.
* [ ] `responsive.css` breakpoints.

---

# EPIC 2: Client‑Side Search & Metadata Processing — **Milestone 2**

**Labels**: `type-epic`, `learning-frontend`, `priority-high`

### Issue #9: Search Engine with Strategy Pattern

**Labels**: `type-feature`, `learning-patterns`, `component-metadata`, `priority-critical`
**Milestone**: 2
**Depends On**: #10, #12
**Suggested Branch**: `feature/issue-9-search-engine`

**Description**
Implement `SearchEngine` with pluggable strategies: exact, fuzzy, and tag-based. Debounce user input; rank results.

**Learning Goals**

* Strategy pattern for algorithm swap.
* Relevance scoring and ranking.
* Performance considerations in the browser.

**Acceptance Criteria**

* [ ] `SearchEngine` interface + strategies (`ExactMatch`, `Fuzzy`, `TagFilter`).
* [ ] Debounced search; cancellation of stale requests.
* [ ] Deterministic ranking; tie-break by recency or path length.
* [ ] Unit perf test: large index search < 100ms on mid-tier laptop.

**Subtasks**

* [ ] Add `SearchService` wrapper used by `SearchUI`.
* [ ] Telemetry hooks (console or simple counter) for tuning.

---

### Issue #10: Metadata Aggregation & Indexing System

**Labels**: `type-feature`, `learning-frontend`, `component-metadata`, `priority-high`
**Milestone**: 2
**Depends On**: #2
**Suggested Branch**: `feature/issue-10-indexer`

**Description**
Aggregate all `.metadata.json` across content folders; build an in-memory index suitable for search and graph building. Cache in `localStorage` with versioning.

**Learning Goals**

* Async file loading and error isolation.
* Index data structures and normalization.
* Client-side caching/version invalidation.

**Acceptance Criteria**

* [ ] `MetadataService` that loads, validates, and normalizes metadata.
* [ ] Incremental update support (load-on-demand).
* [ ] Cache with `indexVersion`; purge on schema change.
* [ ] Tests for corrupted/missing metadata files.

**Subtasks**

* [ ] Add `scripts/generate_metadata.py` (#25) integration note.
* [ ] Document index shape in `docs/metadata_schema.md`.

---

### Issue #11: Advanced Filtering & Tagging System

**Labels**: `type-feature`, `learning-frontend`, `component-metadata`, `priority-medium`
**Milestone**: 2
**Depends On**: #10
**Suggested Branch**: `feature/issue-11-filtering`

**Description**
Provide UI and logic for filtering by tags, type, difficulty, with AND/OR combinations and URL state persistence.

**Learning Goals**

* UI state modeling and observer pattern.
* URL routing and deep-linking of filter state.
* Composability of filters.

**Acceptance Criteria**

* [ ] Tag cloud generated from index with counts.
* [ ] Multi-criteria filter with AND/OR, clear all, and chips UI.
* [ ] URL `#search?tags=...&type=...` reflects state.
* [ ] Tests for filter accuracy and edge cases.

**Subtasks**

* [ ] Debounced filter application.
* [ ] Keyboard-accessible chips.

---

### Issue #12: Frontend Services Layer (Vanilla JS)

**Labels**: `type-feature`, `component-ui`, `learning-frontend`, `priority-high`
**Milestone**: 2
**Depends On**: #2
**Suggested Branch**: `feature/issue-12-services-layer`

**Description**
Implement stateless services: `FileSystemService`, `AuthService`, `SearchService`, `GraphService`, `MetadataService`. No DOM. Promise-based APIs with consistent error model.

**Learning Goals**

* Separation of concerns and testability.
* Async/await API design.
* Error normalization across services.

**Acceptance Criteria**

* [ ] Service contracts documented; mockable in tests.
* [ ] All services return `{ok, data|error}` shapes.
* [ ] Unit tests cover success/failure paths.
* [ ] No direct DOM access from services.

**Subtasks**

* [ ] Common error types and mappers.
* [ ] Minimal retry for transient fetch failures.

---

# EPIC 3: Knowledge Graph Visualization — **Milestone 2**

**Labels**: `type-epic`, `learning-frontend`, `priority-high`

### Issue #13: Graph Data Structure & Connection Management

**Labels**: `type-feature`, `learning-frontend`, `component-graph`, `priority-critical`
**Milestone**: 2
**Depends On**: #10
**Suggested Branch**: `feature/issue-13-graph-data`

**Description**
Build graph nodes/edges from metadata connections with weights and utilities for traversal (BFS/DFS), shortest path, and clustering.

**Learning Goals**

* Graph data structures and traversal algorithms.
* Weighting/normalization for recommendations.
* Performance tuning for graph ops.

**Acceptance Criteria**

* [ ] `GraphService` exposes `neighbors()`, `shortestPath()`, `cluster()`.
* [ ] Connection strength computed and capped 0..1.
* [ ] Test suite with known graphs and expected paths/clusters.

**Subtasks**

* [ ] Defensive handling for missing nodes.
* [ ] Serialization format documented.

---

### Issue #14: Interactive Graph Visualization Component

**Labels**: `type-feature`, `learning-frontend`, `component-graph`, `priority-high`
**Milestone**: 2
**Depends On**: #13
**Suggested Branch**: `feature/issue-14-graph-viz`

**Description**
Render graph with Canvas or SVG, supporting pan/zoom, node drag, highlighting neighbors, and responsive layouts.

**Learning Goals**

* Canvas/SVG rendering pipelines.
* Event handling for complex interactions.
* Layout algorithms (force-directed or simple radial).

**Acceptance Criteria**

* [ ] Smooth pan/zoom at ≥ 50 FPS on mid-tier laptop.
* [ ] Hover/selection highlights neighbors and path to selection.
* [ ] Mobile gestures for pan/zoom.
* [ ] Resize observer for responsiveness.

**Subtasks**

* [ ] Option to throttle redraw with `requestAnimationFrame`.
* [ ] Accessibility: text labels with `aria-hidden` mirroring list.

---

### Issue #15: Graph‑Based Navigation & Discovery

**Labels**: `type-feature`, `learning-frontend`, `component-graph`, `priority-medium`
**Milestone**: 2
**Depends On**: #14
**Suggested Branch**: `feature/issue-15-graph-discovery`

**Description**
Use the graph to surface related content, breadcrumb-like path trails, and suggested learning paths by difficulty.

**Learning Goals**

* Intro to recommendation heuristics.
* Contextual navigation design.
* Progressive disclosure UX.

**Acceptance Criteria**

* [ ] “Related content” sidebar with ranked items.
* [ ] Path trail (topic → … → topic) from current node.
* [ ] Basic learning path generator (beginner→advanced).
* [ ] Tests validating suggestion rules.

**Subtasks**

* [ ] Toggle suggestions by tag/topic.
* [ ] Cache last suggestions.

---

# EPIC 4: Authentication & Private Content Security — **Milestone 3**

**Labels**: `type-epic`, `learning-security`, `priority-high`

### Issue #16: Minimal Backend Authentication System

**Labels**: `type-feature`, `learning-security`, `component-auth`, `priority-critical`
**Milestone**: 3
**Depends On**: #3
**Suggested Branch**: `feature/issue-16-auth-system`

**Description**
Finalize JWT login, validate, and logout flows with password hashing and environment‑based secrets. No user DB; single admin secret for MVP.

**Learning Goals**

* Password hashing & verification.
* Token TTL/refresh strategies.
* Secure error messages and rate limiting (basic).

**Acceptance Criteria**

* [ ] `/api/auth/login`, `/api/auth/validate`, `/api/auth/logout` (if applicable).
* [ ] Hashed password via env var (bcrypt/werkzeug).
* [ ] JWT expiration (24h default) and clock skew handling.
* [ ] Tests: invalid/expired tokens, brute‑force throttle (simple counter).

**Subtasks**

* [ ] Add security headers middleware.
* [ ] Error audit: no sensitive info in responses.

---

### Issue #17: Private Content Access Control

**Labels**: `type-feature`, `learning-security`, `component-files`, `priority-critical`
**Milestone**: 3
**Depends On**: #16
**Suggested Branch**: `feature/issue-17-access-control`

**Description**
Guard private routes in UI and fetch flows; show authenticated-only sections and restrict navigation.

**Learning Goals**

* Conditional rendering and guards.
* Security UX (clear states, no leaks).
* File serving with token headers.

**Acceptance Criteria**

* [ ] `AuthService` stores token securely (localStorage + memory).
* [ ] `FileSystemService` uses `Authorization: Bearer` for private paths.
* [ ] UI reflects auth state (header, lock icons, blocked actions).
* [ ] Tests: unauthorized fetch returns 401/redirect flow.

**Subtasks**

* [ ] “Remember me” token persistence toggle.
* [ ] Logout clears all sensitive caches.

---

### Issue #18: Secure Session Management (Vanilla JS)

**Labels**: `type-feature`, `learning-security`, `component-auth`, `priority-high`
**Milestone**: 3
**Depends On**: #16
**Suggested Branch**: `feature/issue-18-session-mgmt`

**Description**
Client‑side session timer, idle timeout, clock drift checks, and token renewal UX (if implemented) with robust error handling.

**Learning Goals**

* Session hijacking/threat modeling basics.
* Idle timeout and renewal patterns.
* Defensive coding for network failures.

**Acceptance Criteria**

* [ ] Idle timer auto‑logout after N minutes (configurable).
* [ ] Foreground renewal prompt when close to expiry.
* [ ] All token errors produce safe, user‑friendly messages.
* [ ] Unit tests for timers and edge cases.

**Subtasks**

* [ ] Optional: visibility‑based pause of idle timer.
* [ ] Centralized error codes/messages.

---

# EPIC 5: Frontend Foundation & UX — **Milestone 4**

**Labels**: `type-epic`, `learning-frontend`, `priority-critical`

### Issue #19: App Shell & Routing (Vanilla JS)

**Labels**: `type-feature`, `learning-frontend`, `component-ui`, `priority-critical`
**Milestone**: 4
**Depends On**: #8, #12
**Suggested Branch**: `feature/issue-19-routing`

**Description**
Implement hash‑based router (`#/home`, `#/search`, `#/graph`, `#/private`) with view registration and 404 fallback.

**Learning Goals**

* SPA routing fundamentals without frameworks.
* Title/meta updates and scroll restoration.
* Guarded routes for auth.

**Acceptance Criteria**

* [ ] Router module with `register(route, view)` and `navigate()` API.
* [ ] 404 page and not‑found analytics counter.
* [ ] Per‑route title/meta; focus management on navigation.
* [ ] Simple smoke tests for route transitions.

**Subtasks**

* [ ] Route guards integrate with `AuthService`.
* [ ] Back/forward browser support.

---

### Issue #20: Global Styling System (BEM + CSS Utilities)

**Labels**: `type-feature`, `component-ui`, `priority-high`
**Milestone**: 4
**Depends On**: #8
**Suggested Branch**: `feature/issue-20-styling`

**Description**
Create CSS architecture: tokens (colors/spacing), resets, layout utilities, and responsive breakpoints using BEM.

**Learning Goals**

* Scalable CSS systems.
* Dark/light readiness and theming.
* Performance (avoid heavy selectors).

**Acceptance Criteria**

* [ ] `styles/main.css`, `styles/components.css`, `styles/responsive.css`.
* [ ] CSS variables for color/spacing; optional dark tokens.
* [ ] No inline styles; audit of naming consistency.
* [ ] A11y: visible focus states and contrast checks.

**Subtasks**

* [ ] Print styles for PDFs/images.
* [ ] Lint with stylelint (optional).

---

### Issue #21: Accessibility & Keyboard Navigation

**Labels**: `type-feature`, `component-ui`, `priority-high`
**Milestone**: 4
**Depends On**: #8
**Suggested Branch**: `feature/issue-21-a11y`

**Description**
Add global a11y enhancements: skip links, focus traps, keyboard shortcuts, ARIA roles, and semantic headings.

**Learning Goals**

* Practical WCAG practices.
* Keyboard-first navigation.
* Screen reader testing basics.

**Acceptance Criteria**

* [ ] Skip‑to‑content link works across views.
* [ ] Keyboard map documented; modals trap focus.
* [ ] Landmarks and roles assigned; headings logical.
* [ ] A11y smoke test doc with findings.

**Subtasks**

* [ ] Live region for async results.
* [ ] Reduced motion preference respected.

---

### Issue #22: Error States & Empty States UX

**Labels**: `type-feature`, `component-ui`, `priority-medium`
**Milestone**: 4
**Depends On**: #7, #12
**Suggested Branch**: `feature/issue-22-error-empty`

**Description**
Define consistent patterns for network errors, empty results, and unknown routes with helpful recovery actions.

**Learning Goals**

* UX writing for errors.
* Diagnostics exposure without leaking internals.
* Testing unhappy paths.

**Acceptance Criteria**

* [ ] Error boundary wrapper for views.
* [ ] Inline error banners with retry and diagnostics toggle.
* [ ] Empty state illustrations/text; tracking of frequency.
* [ ] Unit tests simulate network failures.

**Subtasks**

* [ ] Centralized error catalog.

---

### Issue #23: Frontend Build Lite (Optional Minifier Only)

**Labels**: `type-enhancement`, `component-ui`, `priority-low`
**Milestone**: 4
**Depends On**: #19, #20
**Suggested Branch**: `feature/issue-23-build-lite`

**Description**
Add a tiny build step (esbuild/terser or Python) for minifying JS/CSS and cache‑busting via hashed filenames.

**Learning Goals**

* Build pipelines and asset hashing.
* Cache control strategies for static hosting.

**Acceptance Criteria**

* [ ] Minify JS/CSS; copy assets to `dist/`.
* [ ] Filename hashing + manifest mapping.
* [ ] Updated deployment docs to serve `dist/`.

**Subtasks**

* [ ] Simple Node or Python script; no bundling required.

---

### Issue #24: Navigation Header & Footer Components

**Labels**: `type-feature`, `component-ui`, `priority-medium`
**Milestone**: 4
**Depends On**: #19, #20
**Suggested Branch**: `feature/issue-24-nav`

**Description**
Reusable header/footer with active route highlighting, auth indicator, and responsive menu.

**Learning Goals**

* Component reuse and state wiring.
* Mobile nav patterns.
* Semantic landmarks.

**Acceptance Criteria**

* [ ] Header with current route highlight; auth state icon/text.
* [ ] Footer shows version/build date; links to docs.
* [ ] Mobile menu expands/collapses via keyboard and touch.

**Subtasks**

* [ ] Add “skip to nav” link.

---

# EPIC 6: Development Utilities & Automation — **Milestone 4**

**Labels**: `type-epic`, `component-utilities`, `priority-medium`

### Issue #25: generate\_metadata.py

**Labels**: `type-feature`, `component-utilities`, `priority-medium`
**Milestone**: 4
**Depends On**: #2
**Suggested Branch**: `feature/issue-25-generate-metadata`

**Description**
Scan content folders and produce baseline `.metadata.json` where missing; merge safely when present.

**Learning Goals**

* Filesystem traversal.
* Idempotent scripts and dry‑run patterns.
* Safe JSON writing/merging.

**Acceptance Criteria**

* [ ] Dry‑run prints intended changes; real run writes.
* [ ] Never overwrites custom fields without explicit flag.
* [ ] Unit tests on sample trees.

**Subtasks**

* [ ] Config for ignore/include patterns.

---

### Issue #26: validate\_connections.py

**Labels**: `type-feature`, `component-utilities`, `priority-medium`
**Milestone**: 4
**Depends On**: #10
**Suggested Branch**: `feature/issue-26-validate-connections`

**Description**
Validate that all `connections[].to` targets exist; report missing nodes, cycles (optional), and invalid strengths.

**Learning Goals**

* Data validation and reporting.
* CI‑friendly exit codes.

**Acceptance Criteria**

* [ ] CLI outputs human‑readable summary + machine‑readable JSON.
* [ ] Exit code 1 on invalid; 0 on success.
* [ ] Integration note for CI job.

**Subtasks**

* [ ] Option to auto‑fix common mistakes (case, trailing slash).

---

### Issue #27: deploy.py

**Labels**: `type-feature`, `component-utilities`, `priority-medium`
**Milestone**: 4
**Depends On**: #23, #39
**Suggested Branch**: `feature/issue-27-deploy`

**Description**
Automate build + publish to GitHub Pages/Netlify and ping backend health if used.

**Learning Goals**

* Deployment scripting and env injection.
* Post‑deploy verification.

**Acceptance Criteria**

* [ ] Builds to `dist/`, publishes, verifies 200 on homepage.
* [ ] Optional: backend healthcheck endpoint ping.
* [ ] Rollback notes documented.

**Subtasks**

* [ ] Secrets/keys handled via env vars.

---

# EPIC 7: Testing & QA — **Milestone 4**

**Labels**: `type-epic`, `component-testing`, `priority-high`

### Issue #28: Frontend Unit Tests (Vanilla JS)

**Labels**: `type-feature`, `component-testing`, `priority-high`
**Milestone**: 4
**Depends On**: #5, #8, #12, #19
**Suggested Branch**: `feature/issue-28-frontend-tests`

**Description**
Test services and DOM-light components; set up coverage reporting and CI gate.

**Learning Goals**

* Testable architecture.
* Deterministic unit tests.
* Coverage instrumentation.

**Acceptance Criteria**

* [ ] Test runner configured (e.g., Vitest/Jest without bundling).
* [ ] Coverage threshold ≥ 70% project-wide.
* [ ] Mocks for services; snapshot tests for simple markup.

**Subtasks**

* [ ] CI workflow to run tests on PR.

---

### Issue #29: Backend Tests (Flask)

**Labels**: `type-feature`, `component-testing`, `priority-high`
**Milestone**: 4
**Depends On**: #3, #16
**Suggested Branch**: `feature/issue-29-backend-tests`

**Description**
Unit/integration tests for auth endpoints and private file serving.

**Learning Goals**

* API testing with Flask client.
* Fixtures and token helpers.

**Acceptance Criteria**

* [ ] Happy path login/validate; 401s for bad password/token.
* [ ] Private file 401 without token; 200 with token; 404 for missing.
* [ ] Rate-limit simulation test (basic).

**Subtasks**

* [ ] PyTest config & coverage report.

---

### Issue #30: Integration Tests (Dev Environment)

**Labels**: `type-feature`, `component-testing`, `priority-high`
**Milestone**: 4
**Depends On**: #4, #7, #16, #17
**Suggested Branch**: `feature/issue-30-e2e`

**Description**
E2E flow: login → navigate to private → open file → logout; plus search and graph basic journeys.

**Learning Goals**

* Black‑box testing mindset.
* Deterministic fixtures.

**Acceptance Criteria**

* [ ] Headless browser or script validating UI+API integration.
* [ ] Stable sample content under `content/private/_samples`.
* [ ] CI job runs E2E nightly and on PR label.

**Subtasks**

* [ ] Retry helpers and screenshots on failure (optional).

---

### Issue #31: Security Tests & Static Checks

**Labels**: `type-feature`, `component-testing`, `priority-medium`
**Milestone**: 4
**Depends On**: #16, #18
**Suggested Branch**: `feature/issue-31-security-static`

**Description**
Add static analysis (JS/CSS/Python), token tamper/replay tests, and basic dependency audit.

**Learning Goals**

* Shift-left security.
* Threat modeling to test cases.

**Acceptance Criteria**

* [ ] ESLint/stylelint/flake8 configured in CI.
* [ ] Token replay/tamper tests fail safely.
* [ ] Dependency audit step (npm/pip) with report.

**Subtasks**

* [ ] Baseline vulnerabilities list in `docs/security.md`.

---

# EPIC 8: Documentation — **Milestone 4**

**Labels**: `type-epic`, `component-docs`, `priority-medium`

### Issue #32: Keep README & Architecture Docs Updated

**Labels**: `type-documentation`, `component-docs`, `priority-medium`
**Milestone**: 4
**Depends On**: Ongoing
**Suggested Branch**: `docs/issue-32-readme-arch`

**Description**
Continuously align README, architecture diagrams, and change log with the codebase.

**Learning Goals**

* Docs-as-code workflows.
* Communicating design decisions.

**Acceptance Criteria**

* [ ] README quickstart verified quarterly or per milestone.
* [ ] Diagrams updated for major structure changes.
* [ ] `docs/CHANGELOG.md` entries per release.

**Subtasks**

* [ ] Doc CI check (links, anchors).

---

### Issue #33: User Guide — Content & Metadata

**Labels**: `type-documentation`, `component-docs`, `priority-medium`
**Milestone**: 4
**Depends On**: #2, #10
**Suggested Branch**: `docs/issue-33-user-guide`

**Description**
Write a user-facing guide on adding files, writing metadata, and linking topics.

**Learning Goals**

* Clear instructional writing.
* Examples-first documentation.

**Acceptance Criteria**

* [ ] Step-by-step guide with screenshots/GIFs.
* [ ] FAQs and common errors section.
* [ ] Cross-links to schema and tools.

**Subtasks**

* [ ] Short video/gif capture pipeline (optional).

---

### Issue #34: Developer Guide — Setup & Workflow

**Labels**: `type-documentation`, `component-docs`, `priority-medium`
**Milestone**: 4
**Depends On**: #4, #28, #29
**Suggested Branch**: `docs/issue-34-developer-guide`

**Description**
Consolidate setup steps, scripts reference, debugging tips, and quality gates for onboarding.

**Learning Goals**

* Onboarding experience.
* Troubleshooting checklists.

**Acceptance Criteria**

* [ ] End-to-end local setup with screenshots.
* [ ] Known issues & fixes page.
* [ ] Links to tests, scripts, and style guides.

**Subtasks**

* [ ] “First bug to fix” checklist for newcomers.

---

# EPIC 9: Performance & Production Optimization — **Milestone 4**

**Labels**: `type-epic`, `component-performance`, `priority-medium`

### Issue #35: Client‑Side Caching & Prefetching

**Labels**: `type-feature`, `component-performance`, `priority-medium`
**Milestone**: 4
**Depends On**: #10, #19
**Suggested Branch**: `feature/issue-35-caching`

**Description**
Cache indexes and metadata with versioning; prefetch likely-next content on hover/idle.

**Learning Goals**

* Cache invalidation strategies.
* UX vs bandwidth trade-offs.

**Acceptance Criteria**

* [ ] Versioned cache with purge controls.
* [ ] Prefetch heuristics (hover, idle).
* [ ] Metrics: cache hit rate logged.

**Subtasks**

* [ ] Toggle prefetch via settings.

---

### Issue #36: Search Index Compression

**Labels**: `type-feature`, `component-performance`, `priority-medium`
**Milestone**: 4
**Depends On**: #10, #9
**Suggested Branch**: `feature/issue-36-index-compress`

**Description**
Compact index data structures; optionally gzip/brotli via hosting.

**Learning Goals**

* Data compaction techniques.
* Measuring size vs accuracy.

**Acceptance Criteria**

* [ ] Memory footprint reduced by ≥ 30% without accuracy loss.
* [ ] Load time improvement reported.
* [ ] Configurable compression toggle.

**Subtasks**

* [ ] Benchmark script.

---

### Issue #37: Graph Rendering Optimization

**Labels**: `type-feature`, `component-performance`, `priority-medium`
**Milestone**: 4
**Depends On**: #14
**Suggested Branch**: `feature/issue-37-graph-perf`

**Description**
Optimize the graph visualization for large node counts with batching and level-of-detail.

**Learning Goals**

* Rendering pipelines and throttling.
* LOD techniques.

**Acceptance Criteria**

* [ ] Stable ≥ 50 FPS for 1k nodes on mid-tier laptop.
* [ ] LOD reduces labels/edges when zoomed out.
* [ ] Perf diagnostics overlay.

**Subtasks**

* [ ] Frame scheduler utility.

---

### Issue #38: Asset Optimization & Lazy Loading

**Labels**: `type-feature`, `component-performance`, `priority-medium`
**Milestone**: 4
**Depends On**: #20, #23
**Suggested Branch**: `feature/issue-38-asset-opt`

**Description**
Implement lazy loading for images/PDFs, compress assets, and defer non-critical JS.

**Learning Goals**

* Modern image formats, responsive images.
* Defer/async scripts best practices.

**Acceptance Criteria**

* [ ] Lazy load non-critical assets with placeholders.
* [ ] Lighthouse performance ≥ 90 on homepage.
* [ ] Compression pipeline documented.

**Subtasks**

* [ ] Generate thumbnails for large images.

---

### Issue #39: Static Site Deployment & Hosting Configuration

**Labels**: `type-feature`, `component-performance`, `priority-high`
**Milestone**: 4
**Depends On**: #23, #27
**Suggested Branch**: `feature/issue-39-deploy-config`

**Description**
Harden production deploy: static CDN hosting for frontend, optional backend host, security headers, HTTPS, and monitoring/analytics.

**Learning Goals**

* Static hosting configs and headers.
* Basic monitoring/analytics wiring.

**Acceptance Criteria**

* [ ] GitHub Pages/Netlify config committed; custom domain optional.
* [ ] Security headers and HTTPS enforced.
* [ ] Monitoring enabled; baseline error budget defined.
* [ ] Deployment guide finalized in `docs/`.

**Subtasks**

* [ ] Healthcheck route + uptime check.

---

## 🚀 Quick Start Execution Plan (for Project Board)

**Phase 1 (Week 1–2)**: #1, #2, #3, #4, #5, #6, #8
**Phase 2 (Week 3–4)**: #7, #10, #12, #9, #11, #13, #14, #15
**Phase 3 (Week 5–6)**: #16, #17, #18, #28, #29, #30
**Phase 4 (Week 7–8)**: #19–#27, #31–#39

---

> Tip: When opening each GitHub issue, paste the corresponding section, set the **Milestone** and **Labels**, and add a **Project** card. Use the suggested branch name to keep history clean and traceable.
