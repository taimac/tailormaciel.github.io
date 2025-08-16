# 📋 Development Backlog

**Repository**: [taimac/tailormaciel.github.io](https://github.com/taimac/tailormaciel.github.io)
**Last Updated**: 2025-08-14 23:18:59
**Total Issues**: 57 | **Open**: 39 | **Closed**: 18

---

## 🚀 Open Issues (To Do)

### 🟢 Issue #51: B01 — Hybrid Project Structure & Setup

**Status**: OPEN | `priority-critical` `type-feature` `learning-architecture` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/51](https://github.com/taimac/tailormaciel.github.io/issues/51)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #52: B02 — Metadata System for Content Organization

**Status**: OPEN | `priority-critical` `type-feature` `learning-architecture` `component-metadata` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/52](https://github.com/taimac/tailormaciel.github.io/issues/52)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #53: B03 — Minimal Flask Backend for Authentication

**Status**: OPEN | `priority-critical` `type-feature` `learning-architecture` `learning-security` `component-auth` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/53](https://github.com/taimac/tailormaciel.github.io/issues/53)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #54: B04 — Development Environment & Dual Server Setup

**Status**: OPEN | `priority-high` `type-feature` `learning-architecture` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/54](https://github.com/taimac/tailormaciel.github.io/issues/54)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #55: B05 — Base FileSystem Classes with Encapsulation

**Status**: OPEN | `priority-critical` `type-feature` `learning-oop` `component-files` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/55](https://github.com/taimac/tailormaciel.github.io/issues/55)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #56: B06 — Content Type Inheritance Hierarchy

**Status**: OPEN | `priority-critical` `type-feature` `learning-oop` `component-files` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/56](https://github.com/taimac/tailormaciel.github.io/issues/56)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #57: B07 — Polymorphic File Explorer Component

**Status**: OPEN | `priority-high` `type-feature` `learning-oop` `component-ui` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/57](https://github.com/taimac/tailormaciel.github.io/issues/57)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #58: B08 — Core Frontend Components (Vanilla JS)

**Status**: OPEN | `priority-critical` `type-feature` `component-ui` `learning-frontend` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/58](https://github.com/taimac/tailormaciel.github.io/issues/58)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #59: B09 — Search Engine with Strategy Pattern

**Status**: OPEN | `priority-critical` `type-feature` `learning-patterns` `component-metadata` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/59](https://github.com/taimac/tailormaciel.github.io/issues/59)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #60: B10 — Metadata Aggregation & Indexing System

**Status**: OPEN | `priority-high` `type-feature` `learning-frontend` `component-metadata` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/60](https://github.com/taimac/tailormaciel.github.io/issues/60)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #61: B11 — Advanced Filtering & Tagging System

**Status**: OPEN | `priority-medium` `type-feature` `learning-frontend` `component-metadata` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/61](https://github.com/taimac/tailormaciel.github.io/issues/61)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #62: B12 — Frontend Services Layer (Vanilla JS)

**Status**: OPEN | `priority-high` `type-feature` `component-ui` `learning-frontend` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/62](https://github.com/taimac/tailormaciel.github.io/issues/62)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #63: B13 — Graph Data Structure & Connection Management

**Status**: OPEN | `priority-critical` `type-feature` `learning-frontend` `component-graph` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/63](https://github.com/taimac/tailormaciel.github.io/issues/63)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #64: B14 — Interactive Graph Visualization Component

**Status**: OPEN | `priority-high` `type-feature` `learning-frontend` `component-graph` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/64](https://github.com/taimac/tailormaciel.github.io/issues/64)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #65: B15 — Graph‑Based Navigation & Discovery

**Status**: OPEN | `priority-medium` `type-feature` `learning-frontend` `component-graph` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/65](https://github.com/taimac/tailormaciel.github.io/issues/65)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #66: B16 — Minimal Backend Authentication System

**Status**: OPEN | `priority-critical` `type-feature` `learning-security` `component-auth` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/66](https://github.com/taimac/tailormaciel.github.io/issues/66)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #67: B17 — Private Content Access Control

**Status**: OPEN | `priority-critical` `type-feature` `learning-security` `component-files` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/67](https://github.com/taimac/tailormaciel.github.io/issues/67)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #68: B18 — Secure Session Management (Vanilla JS)

**Status**: OPEN | `priority-high` `type-feature` `learning-security` `component-auth` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/68](https://github.com/taimac/tailormaciel.github.io/issues/68)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #69: B19 — App Shell & Routing (Vanilla JS)

**Status**: OPEN | `priority-critical` `type-feature` `component-ui` `learning-frontend` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/69](https://github.com/taimac/tailormaciel.github.io/issues/69)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #70: B20 — Global Styling System (BEM + CSS Utilities)

**Status**: OPEN | `priority-high` `type-feature` `component-ui` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/70](https://github.com/taimac/tailormaciel.github.io/issues/70)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #71: B21 — Accessibility & Keyboard Navigation

**Status**: OPEN | `priority-high` `type-feature` `component-ui` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/71](https://github.com/taimac/tailormaciel.github.io/issues/71)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #72: B22 — Error States & Empty States UX

**Status**: OPEN | `priority-medium` `type-feature` `component-ui` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/72](https://github.com/taimac/tailormaciel.github.io/issues/72)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #73: B23 — Frontend Build Lite (Optional Minifier Only)

**Status**: OPEN | `priority-low` `type-enhancement` `component-ui` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/73](https://github.com/taimac/tailormaciel.github.io/issues/73)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #74: B24 — Navigation Header & Footer Components

**Status**: OPEN | `priority-medium` `type-feature` `component-ui` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/74](https://github.com/taimac/tailormaciel.github.io/issues/74)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #75: B25 — generate_metadata.py

**Status**: OPEN | `priority-medium` `type-feature` `component-utilities` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/75](https://github.com/taimac/tailormaciel.github.io/issues/75)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #76: B26 — validate_connections.py

**Status**: OPEN | `priority-medium` `type-feature` `component-utilities` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/76](https://github.com/taimac/tailormaciel.github.io/issues/76)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #77: B27 — deploy.py

**Status**: OPEN | `priority-medium` `type-feature` `component-utilities` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/77](https://github.com/taimac/tailormaciel.github.io/issues/77)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #78: B28 — Frontend Unit Tests (Vanilla JS)

**Status**: OPEN | `priority-high` `type-feature` `component-testing` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/78](https://github.com/taimac/tailormaciel.github.io/issues/78)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #79: B29 — Backend Tests (Flask)

**Status**: OPEN | `priority-high` `type-feature` `component-testing` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/79](https://github.com/taimac/tailormaciel.github.io/issues/79)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #80: B30 — Integration Tests (Dev Environment)

**Status**: OPEN | `priority-high` `type-feature` `component-testing` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/80](https://github.com/taimac/tailormaciel.github.io/issues/80)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #81: B31 — Security Tests & Static Checks

**Status**: OPEN | `priority-medium` `type-feature` `component-testing` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/81](https://github.com/taimac/tailormaciel.github.io/issues/81)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #82: B32 — Keep README & Architecture Docs Updated

**Status**: OPEN | `priority-medium` `type-documentation` `component-docs` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/82](https://github.com/taimac/tailormaciel.github.io/issues/82)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #83: B33 — User Guide — Content & Metadata

**Status**: OPEN | `priority-medium` `type-documentation` `component-docs` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/83](https://github.com/taimac/tailormaciel.github.io/issues/83)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #84: B34 — Developer Guide — Setup & Workflow

**Status**: OPEN | `priority-medium` `type-documentation` `component-docs` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/84](https://github.com/taimac/tailormaciel.github.io/issues/84)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #85: B35 — Client‑Side Caching & Prefetching

**Status**: OPEN | `priority-medium` `type-feature` `component-performance` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/85](https://github.com/taimac/tailormaciel.github.io/issues/85)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #86: B36 — Search Index Compression

**Status**: OPEN | `priority-medium` `type-feature` `component-performance` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/86](https://github.com/taimac/tailormaciel.github.io/issues/86)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #87: B37 — Graph Rendering Optimization

**Status**: OPEN | `priority-medium` `type-feature` `component-performance` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/87](https://github.com/taimac/tailormaciel.github.io/issues/87)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #88: B38 — Asset Optimization & Lazy Loading

**Status**: OPEN | `priority-medium` `type-feature` `component-performance` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/88](https://github.com/taimac/tailormaciel.github.io/issues/88)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### 🟢 Issue #89: B39 — Static Site Deployment & Hosting Configuration

**Status**: OPEN | `priority-high` `type-feature` `component-performance` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/89](https://github.com/taimac/tailormaciel.github.io/issues/89)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

## ✅ Completed Issues

### ✅ Issue #50: TEMP: Backlog probe

**Status**: CLOSED | `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/50](https://github.com/taimac/tailormaciel.github.io/issues/50)

**Description**:
created via gh to verify perms

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #44: Documentation System Setup

**Status**: CLOSED | `priority-medium` `type-documentation` `learning-architecture` `superseded-by-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/44](https://github.com/taimac/tailormaciel.github.io/issues/44)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #43: CI/CD Setup & GitHub Integration

**Status**: CLOSED | `priority-medium` `type-feature` `learning-architecture` `superseded-by-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/43](https://github.com/taimac/tailormaciel.github.io/issues/43)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #42: Development Tools & Scripts Setup

**Status**: CLOSED | `priority-high` `type-feature` `learning-architecture` `superseded-by-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/42](https://github.com/taimac/tailormaciel.github.io/issues/42)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #41: Frontend Basic Structure & Build Setup

**Status**: CLOSED | `priority-critical` `type-feature` `learning-architecture` `layer-presentation` `superseded-by-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/41](https://github.com/taimac/tailormaciel.github.io/issues/41)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #40: Database Setup & Initial Schema

**Status**: CLOSED | `priority-critical` `type-feature` `learning-architecture` `layer-infrastructure` `superseded-by-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/40](https://github.com/taimac/tailormaciel.github.io/issues/40)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #39: Backend Dependencies & Flask Application Bootstrap

**Status**: CLOSED | `priority-critical` `type-feature` `learning-architecture` `layer-infrastructure` `backlog-import-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/39](https://github.com/taimac/tailormaciel.github.io/issues/39)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #38: Project Structure Creation

**Status**: CLOSED | `priority-critical` `type-feature` `learning-architecture`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/38](https://github.com/taimac/tailormaciel.github.io/issues/38)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #37: Development Environment Setup & Validation

**Status**: CLOSED | `priority-critical` `type-feature` `learning-architecture`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/37](https://github.com/taimac/tailormaciel.github.io/issues/37)

**Description**:
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

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #36: EPIC 8: Performance & Production Readiness

**Status**: CLOSED | `priority-low` `type-epic` `superseded-by-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/36](https://github.com/taimac/tailormaciel.github.io/issues/36)

**Description**:
Optimize performance and prepare for production deployment.

Learning Goals: 

Understand production considerations and optimization techniques

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #35: EPIC 7: Knowledge Base Features

**Status**: CLOSED | `priority-medium` `type-epic` `component-knowledge` `superseded-by-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/35](https://github.com/taimac/tailormaciel.github.io/issues/35)

**Description**:
Build intelligent knowledge base with graph connections and search.

Learning Goals: 

Apply all learned concepts to complex feature implementation

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #34: EPIC 6: Testing & Quality Assurance

**Status**: CLOSED | `priority-high` `type-epic` `learning-testing` `superseded-by-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/34](https://github.com/taimac/tailormaciel.github.io/issues/34)

**Description**:
Implement comprehensive testing strategy with TDD approach.

Learning Goals: 
Master testing principles and achieve 70%+ coverage

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #33: EPIC 5: Design Patterns Implementation

**Status**: CLOSED | `priority-medium` `type-epic` `learning-patterns` `superseded-by-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/33](https://github.com/taimac/tailormaciel.github.io/issues/33)

**Description**:
Apply classic design patterns to solve common software problems.

Learning Goals: 
Master pattern recognition and appropriate pattern application

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #32: EPIC 4: Frontend OOP & Component Architecture

**Status**: CLOSED | `priority-high` `type-epic` `learning-oop` `component-ui` `superseded-by-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/32](https://github.com/taimac/tailormaciel.github.io/issues/32)

**Description**:
Apply OOP principles to frontend JavaScript with component-based architecture.

Learning Goals: 
Master JavaScript classes and modular component design

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #31: EPIC 3: Security-First Development

**Status**: CLOSED | `priority-high` `type-epic` `learning-security` `superseded-by-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/31](https://github.com/taimac/tailormaciel.github.io/issues/31)

**Description**:
Implement comprehensive security measures throughout all layers.

**Learning Goals**: 

Master security principles and common vulnerability prevention

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #30: EPIC 2: Clean Architecture Foundation

**Status**: CLOSED | `priority-critical` `type-epic` `learning-architecture` `superseded-by-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/30](https://github.com/taimac/tailormaciel.github.io/issues/30)

**Description**:
Implement proper layer separation with clear boundaries and dependency rules.

**Learning Goals**: 
Master Clean Architecture principles with hands-on layer implementation

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #29: EPIC 1: OOP Fundamentals Implementation

**Status**: CLOSED | `priority-critical` `type-epic` `learning-oop` `superseded-by-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/29](https://github.com/taimac/tailormaciel.github.io/issues/29)

**Description**:
Establish solid OOP foundation with practical examples demonstrating all four core principles.

**Learning Goals**: 
Master encapsulation, inheritance, polymorphism, and abstraction through hands-on coding


**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

### ✅ Issue #28: EPIC 0: Hybrid Project Foundation (File-Based + Minimal Backend)

**Status**: CLOSED | `priority-critical` `type-epic` `learning-architecture` `superseded-by-2025-08`
**GitHub**: [https://github.com/taimac/tailormaciel.github.io/issues/28](https://github.com/taimac/tailormaciel.github.io/issues/28)

**Description**:
Set up file-based knowledge system with minimal backend for authentication and private file serving Learning Goals: Understand hybrid architecture, static site principles, and when to use minimal backend vs full application

**My Development Notes**:
*Add your progress, learning notes, and implementation details here*

---

