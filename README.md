# tailormaciel.com

Personal website of Tailor Maciel — B2B commercial operator and systems builder.

Live at **[tailormaciel.com](https://tailormaciel.com)**

## Stack

Static HTML · CSS · Vanilla JS · GitHub Pages

## Structure

```
index.html          Home
about.html          About
experience.html     Experience & projects
education.html      Education & certifications
contact.html        Contact
styles/             Component-based CSS architecture
scripts/            Site controller (navbar, mobile menu, language switcher, animations)
translations/       PT/EN string dictionary
images/             Photos, logos, certificates
```

## Languages

Portuguese (primary) · English toggle available on every page.

## Local Preview

Use the no-cache preview server while editing:

```bash
python3 dev_server.py
```

Open `http://127.0.0.1:8002/`. Local preview keeps Portuguese as the default source and polls HTML, CSS, JS, and translation files for changes.

## Licence

© 2026 Tailor Maciel. All rights reserved.

## Artigos (Portuguese)

`artigos/index.html` lists approved articles. Prepare a public article Markdown
with `status: draft` or `approved`, `approved: true`, `brand: personal`,
`format: article`, `slug`, `title` and `description`; then run:

```sh
node scripts/renderArticle.js article.md
node --test scripts/renderArticle.test.js
```

The input is publishable prose, not an entire private Editorial note. Existing
slugs are refused. A new article and the regenerated index enter a reviewed PR
to publishing `main`; repository-default `dev` is not the Pages source. Nothing
in the renderer commits, pushes, merges or publishes. Articles are Portuguese;
no automatic translation is performed.

### Visual preview of Artigos

```sh
node scripts/previewArticles.js 8787
```

Open `http://127.0.0.1:8787/` and follow Home → Artigos → demonstration →
Todos os artigos → TM. The real empty state is available at
`http://127.0.0.1:8787/_states/empty/artigos/`.

The helper copies only public assets into an isolated temporary directory and
adds one clearly identified synthetic article there. It binds to loopback,
disables indexing and caching, and never writes an article into the source
`artigos/` directory. Stop it with Ctrl+C and restart after source changes.
The production index remains empty until an approved article enters its own PR.

Navigation and footer are extracted from `about.html` by the renderer; shared
site styles/controllers remain the reference. Interface controls support PT/EN;
article prose stays Portuguese. [Visual evidence and engineering record](docs/artigos-identity-review.md).
