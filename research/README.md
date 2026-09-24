# Chiron reference pack

Researched September 21, 2026 (America/Los_Angeles; September 22 UTC).
Start here in future tasks; read one topic note, not the whole pack.

| Need | Read |
|---|---|
| MyST syntax, theme, TOC, notebooks, hosting | [MyST](myst.md) |
| Current teaching evidence, user voice, and temp-branch direction | [Teaching](teaching.md) |
| Programming-course structure and maintenance patterns | [FRCSoftware](frcsoftware.md) |
| CAD-course pedagogy, design, and mature reference organization | [FRCDesign](frcdesign.md) |
| Existing Chiron state and suggested application | [Chiron](chiron.md) |
| Exactly what was verified; how to refresh | [Coverage](coverage.md) |
| Find a specific upstream page | [Software index](inventories/frcsoftware.md), [Design index](inventories/frcdesign.md) |

## Durable findings

- Keep the guided course distinct from lookup/reference material. Both reference
  sites also give educators their own guidance.
- Teach through meaningful robot projects, progressively reduce hints, and build
  review and debugging into the learning loop.
- Both reference sites currently use Astro/Starlight + MDX. Chiron uses MyST:
  transfer the learning experience and information architecture, not their syntax.
- MyST already provides most needed elements: book navigation, notebooks,
  exercises/solutions, callouts, tabs, cards, cross-references, and static export.
  Start with configuration and content before considering a custom theme.
- Course order needs editorial control. A filesystem directory, a navigation
  tree, and a public URL are separate decisions in MyST.
- Current FRCSoftware content includes unfinished stages and 2027-oriented Java
  APIs. Its source is valuable, but is not a ready-to-copy Python curriculum.
- Longer history is not proof of every design choice being validated. FRCDesign
  has visible maintenance drift too.

## Scope

This is a reusable architectural and curriculum reference, with **all 65
FRCSoftware and 170 FRCDesign MDX source pages indexed** at pinned revisions.
Those counts include component demonstration pages. Detailed review focused on
site structure, pedagogy, representative lessons, authoring, and build systems.
It is **not a claim of literal 100% understanding or technical validation of
every lesson, video, linked codebase, or CAD document**. See the coverage record.

Sources are linked in the topic notes; inventories contain per-file immutable
GitHub links, headings, hashes, and WIP/TODO markers in JSON. Optional local text
snapshots are in `.research-cache/`, excluded from Git. The notes and inventories
work without those caches. No website implementation or deployment was performed
during that research phase. Implementation now follows the separately approved
[design](../design/course-plan.md) and [decision log](../design/decisions.md).
