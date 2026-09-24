# Coverage and refresh record

Date: September 21, 2026 America/Los_Angeles (September 22 UTC).
No site was built, modified, deployed, or published.

## Evidence and limits

| Source | Coverage | Limits |
|---|---|---|
| Chiron main | Complete recursive tree; configuration, workflow, README, license heading; empty requirements verified from tree | Other branches and deployed page rendering not inspected |
| MyST | Official syntax, TOC, themes/options, theme architecture, navigation, inclusion/embedding, exercises, tabs/cards, notebook build/runtime execution, Pages deployment | No local MyST build; no exhaustive schema or implementation audit |
| FRCSoftware | All 65 MDX files cached and structurally indexed; complete sidebar; home/course/educator structure; representative Stage 0 and 1B lesson bodies; resources; contribution guidance; configuration, example embedding and CI | Not every lesson body read line-by-line; Java examples not compiled; external repositories/media not audited |
| FRCDesign | All 170 MDX files cached and structurally indexed; complete course navigation; course/educator progression; representative exercise/review/summary pages; handbook/resources; contributor docs and CI | Not every lesson body read line-by-line; CAD documents, videos, component-generated catalogs not exhaustively reviewed |
| Browser | Both sites' home/course navigation; screenshots of Software home and Design course; live Software rewrite lesson and its controls | No accessibility audit, device matrix, search-quality evaluation, or live hardware testing |

“Complete inventory” means all MDX source files in each pinned repository tree,
not all reachable internet resources, and not a claim that every indexed file
is in public navigation. Source snapshots and the deployed sites can differ.

Detailed source reads included:

- Software: configuration, sidebar/topic/outline settings, region plugin,
  package scripts, build/compile/preview workflows, Copybara config, educator
  introduction/preparation/stages/1A/1B, resource overviews/hardware/examples,
  style guide, conditionals, kitbot rewrite part 1, stage wrap-ups, 1C/2 overviews.
- Design: configuration, sidebar, outline settings, package/CI, course overview,
  educator stage map and Stage 1 guides, improvement guide, 1C exercise 8,
  2D summary, Next Steps, handbook/resources/best-practice introductions,
  feature and contributor guides.

The local cache contains more source than was deeply reviewed. Retrieval,
automatic indexing, reading, and execution verification are different levels
of evidence; future tasks should not collapse them into “fully verified.”

## Revisions

| Repository | Revision |
|---|---|
| Spartronics4915/Chiron | `8114652213e4facc99f827d29a1c1db4eb825b4c` |
| frcsoftware/frcsoftware.org | `a5cea0436c10b6da9017b3464ac4c265771afcf3` |
| frcdesign/FRCDesign.org | `bf97fe228fef7d01330de1d6f56cfab79e9ed057` |

MyST notes cite live official documentation, accessed on the date above. They
are not pinned to a release. Chiron's workflow did not pin MyST, so no precise
deployed CLI version is claimed.

## Local lookup

Read the small note first. Then search the appropriate JSON inventory by
title/path/heading to identify one source file. Read its cached file if present,
or use the immutable GitHub link. Avoid loading entire inventories by default.

The ignored caches are sparse public Git checkouts:

- `.research-cache/frcsoftware/`
- `.research-cache/frcdesign/`

They include MDX text and selected configuration, not complete downloadable
courses or all images, examples, videos, dependencies, and generated outputs.
Git may need network access for blobs outside the sparse checkout. Do not run
upstream scripts merely to read these caches.

## Refresh procedure

1. Inspect local work and choose the topic that actually needs updating.
2. Compare the upstream main revision with the recorded revision.
3. Fetch/read only changed relevant files. Read updated course ordering and WIP
   markers if the curriculum changed.
4. Before implementing a MyST feature, verify its current docs against the version
   selected for Chiron and exercise it in a small real build.
5. Update the relevant note and its date/revision. Mark inference versus observed
   behavior. Do not silently rewrite historical claims.
6. If refreshing all source inventories, update the sparse caches deliberately,
   then run `research/tools/index-sources.ps1` from this workspace. Review the diff.

The indexer extracts filenames, title lines, Markdown headings, and textual
WIP/TODO markers. It is not an MDX parser, cannot see all component-generated
headings, and may find markers in explanatory text. Live URL candidates are
inferred; immutable source URLs are the reliable lookup key.

## Remaining targeted work

When course design begins, review the specific upstream lesson being adapted
in full and validate its Python equivalent. When frontend work begins, verify
the relevant MyST element and responsive behavior. Assess learner effectiveness
through actual Team 4915 use; neither reference site's age nor this inspection
substitutes for that.

