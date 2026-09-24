# MyST working reference

Scope: the JavaScript `mystmd` toolchain used by Chiron, not Sphinx's Python
`myst-parser`. Verified against official documentation on September 21, 2026.
Examples below are reference sketches, not a tested Chiron build.

## Content and rendering

MyST extends CommonMark with block directives and inline roles. A directive
contains a name, optional argument, options, and body; a role is inline.
Use colon fences for Markdown bodies and backtick fences for code-like bodies.
Nested containers need longer outer fences. Page metadata is YAML frontmatter.
[Syntax](https://mystmd.org/guide/syntax-overview)

The engine parses Markdown/notebooks into a structured document representation.
The web theme renders the resolved content. During development, `myst start`
builds `_build/site`, exposes content JSON and assets, and starts the theme.
A custom theme is a separate web application with a `template.yml` contract;
it is a substantially larger maintenance commitment than styling the standard
theme. [Architecture](https://mystmd.org/guide/theme-developer)

## Theme and navigation

`book-theme` suits a multi-page course/reference; `article-theme` centers on an
article with supporting documents. Set `site.template`. Theme-wide settings live
under `site.options`; per-page overrides live directly under frontmatter
`site`, without an `options` wrapper. Relevant settings include `logo`,
`logo_dark`, `favicon`, `style`, `hide_toc`, `hide_outline`,
`hide_footer_links`, and `outline_maxdepth`.

URLs flatten folders by default. `site.options.folders: true` preserves folder
paths and supports folder `index.md` landing pages. Avoid both `course.md` and
`course/index.md`, which collide. [Theme options](https://mystmd.org/guide/website-templates)

`site.nav` supplies global links/dropdowns; `project.toc` drives the primary
sidebar; headings drive the secondary outline. These are distinct navigation
surfaces. `site.parts` can supply banners/footers. `project.github` enables
repository editing links; `edit_url` overrides them.
[Navigation](https://mystmd.org/guide/website-navigation)

## Table of contents

An explicit TOC is a tree of `file`, `title`, `children`, `url`, and `pattern`
entries. Patterns preserve folder structure, respect exclusions, and skip files
already listed explicitly. `hidden: true` builds a page without showing it in
navigation; it is not access control.

Without `project.toc`, MyST discovers Markdown/notebooks from the filesystem and
orders filenames, including natural numeric sorting. `myst init --write-toc`
creates a starting TOC. `project.exclude` keeps non-content out of discovery.
A TOC entry title overrides the navigation label; page `short_title` also helps.

`{toc}` supports project, page, section, or children contexts and depth controls.
Useful for section landing pages. Default flat slugs derive from filenames, strip
leading numbering, and deduplicate collisions. Public URL stability therefore
needs an intentional policy. [TOC details](https://mystmd.org/guide/table-of-contents)

Illustrative configuration; paths must exist before use:

```yaml
version: 1
project:
  title: Chiron
  github: https://github.com/Spartronics4915/Chiron
  toc:
    - file: index.md
    - file: course/index.md
      children:
        - file: course/python-foundations/variables.ipynb
    - file: hardware/index.md
    - file: api/index.md
site:
  template: book-theme
  options:
    folders: true
```

## Teaching elements

| Need | Native MyST approach | Source |
|---|---|---|
| Tips, cautions, optional hints | Admonitions; dropdown class | [Callouts](https://mystmd.org/guide/admonitions) |
| Exercise with linked answer | `exercise` label, `solution` referring to label | [Exercises](https://mystmd.org/guide/exercises) |
| Vendor alternatives | `tab-set` / `tab-item`; `sync` for related tabs | [Tabs/cards](https://mystmd.org/guide/dropdowns-cards-and-tabs) |
| Section entry points | Grids/cards and TOC child lists | [Tabs/cards](https://mystmd.org/guide/dropdowns-cards-and-tabs) |
| Reusable explanation | `include` for source text, `embed` for resolved labeled content | [Reuse](https://mystmd.org/guide/embed) |
| Tested source snippets | `literalinclude` instead of copied code blocks | [Reuse](https://mystmd.org/guide/embed) |

An ordinary Python code fence displays code; it does not make it executable.
Use notebook cells or `code-cell`. Executable cells must remain at document root:
use `exercise-start` / `exercise-end` and analogous solution gates when wrapping
them, rather than nesting cells inside directive bodies. A dropdown solution is
a teaching affordance, not protected assessment content.
[Exercise execution](https://mystmd.org/guide/exercises)

## Three separate execution experiences

| Experience | How it works | Chiron implication |
|---|---|---|
| Saved outputs | Render existing notebook results | Reading works without a live kernel |
| Build-time execution | `myst build --execute --html`; Jupyter Server plus kernel required | CI must install the Python environment |
| Reader execution | Thebe connection to Binder, JupyterLite/WASM, or Jupyter server | Separate capability and infrastructure decision |

Build execution follows cell order and caches outputs. Changes to computational
content invalidate the cache; `myst clean --execute` clears it.
`skip-execution` and `raises-exception` tags support special teaching cases.
[Build execution](https://mystmd.org/guide/execute-notebooks)

`project.jupyter: true` enables in-page execution and defaults to Binder.
`project.github` can determine the Binder repository. The feature is documented
as beta; a configured backend is required. Do not treat an uploaded notebook as
automatically interactive, or assume browser kernels support hardware packages.
[Reader execution](https://mystmd.org/guide/in-page-execution)

## Build and host

`myst start` previews; `myst build --html` produces static `_build/html`.
`myst init --gh-pages` scaffolds deployment. GitHub repository sites need the
appropriate build-time `BASE_URL`, such as `/Chiron`; a domain-root deployment
uses an empty base path. Test a future host with deep links and assets, not just
its homepage. [GitHub Pages](https://mystmd.org/guide/deployment-github-pages)

Future implementation should pin and test the chosen CLI/theme versions. Current
documentation describes capabilities, not a guarantee that every historical
release supports them.

