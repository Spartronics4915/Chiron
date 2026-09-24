# FRCSoftware reference

Primary inspiration: [frcsoftware.org](https://frcsoftware.org/).
Source snapshot: [a5cea043](https://github.com/frcsoftware/frcsoftware.org/tree/a5cea0436c10b6da9017b3464ac4c265771afcf3).
All 65 MDX files are indexed in [Markdown](inventories/frcsoftware.md) and
[JSON](inventories/frcsoftware.json). The JSON includes headings and status markers.

## Purpose and teaching choices

A self-paced path from Java basics to useful in-season robot programming.
Simulation makes practice possible without exclusive robot access. Educators
spend meeting time diagnosing individual problems and reviewing work while the
site provides explanations and exercises. Guidance decreases as capability grows.
The authors deliberately prioritize broadly useful fundamentals over specialist
topics; their stated course goal does not require every student to learn swerve,
vision, or pose estimation.

Java is the authors' choice for ecosystem reach and existing student familiarity,
not evidence that Chiron should change languages. The educator guide explicitly
notes that language/library differences limit transfer.
[Educator introduction](https://frcsoftware.org/educators-guide/introduction/),
[preparation](https://frcsoftware.org/educators-guide/introduction/preparation/)

## Actual navigation and curriculum

| Area | Ordered content / learner outcome | Current state |
|---|---|---|
| Setup | Feature guide; WPILib tools, Driver Station, Git/GitHub; VS Code; fork/clone templates | Written |
| Stage 0 | Java fundamentals → debugging → operators → conditionals → loops → classes/objects → methods/mutable state → arrays/for-each → interfaces/generics/lists → resources → wrap-up | Written |
| Stage 1A | Template structure → drivetrain/motor configuration → simulation → timed autonomous → intake/launcher and feeder → wrap-up | Written, with simulation-only hardware caveat |
| Stage 1B | Command model → coroutine body → mechanisms/commands → triggers/scheduling → defaults/delays/parallelism → error exercises → kitbot rewrite → suppliers → drivetrain/autonomous rewrite → error exercises → wrap-up | Written, uses Commands v3 |
| Stage 1C | PID positioning and telemetry; intended turn-to-angle and drive-distance work | Overview only; WIP |
| Stage 2 | MIDTIDE: elevator → arm → claw → basic teleops → intake/indexer and self-written simulation → state machine teleop → collision avoidance | Planned sequence; WIP |
| Educators | Preparation, stage objectives, misconceptions, extra practice | Uneven: Stage 1 overview and 1C are placeholders; Stage 2 is WIP |
| Resources | Examples, external documentation, hardware introduction, glossary | Reference, not a full API manual |
| Best practices | Git, GitHub issues/PRs/projects, formatting, CI | Separate from course |
| Contribution | Workflow, style guide, contributors, roadmap | Roadmap points to GitHub project |

The exact sidebar sequence is in
[sidebarConfig.ts](https://github.com/frcsoftware/frcsoftware.org/blob/a5cea0436c10b6da9017b3464ac4c265771afcf3/src/config/sidebarConfig.ts).
[Course overview](https://frcsoftware.org/learning-course/) and
[stage guide](https://frcsoftware.org/educators-guide/introduction/the-stages/)
explain the progression.

Stage 1 reuses one 2026 kitbot: first get it working, then restructure the same
behavior into commands. This isolates the new architecture from a new physical
problem. The current site warns that Stage 1 targets **Systemcore**, was tested
in simulation, and was not tested on a real kitbot. Stage 1B identifies the
**2027 framework / Commands v3**. Historical example links still include
Commands v2. Keep those contexts separate when adapting content.

## Lesson mechanics

A simple lesson such as
[Conditionals](https://frcsoftware.org/learning-course/stage0/conditionals/)
moves from everyday analogy to syntax, traced examples, then a template-file
exercise. Debugging appears early and recurs in dedicated error-finding exercises.

[Kitbot Rewrite, Part 1](https://frcsoftware.org/learning-course/stage1/stage1b/command-based-kitbot/)
states the deliverable, links prerequisites/templates, divides work into tasks,
and offers progressively specific collapsed hints. CTRE/REV tabs synchronize
vendor choices. The live page rendered code into source fences that are empty
in MDX because a build plugin inserts the corresponding Java regions. These
empty source fences are not unfinished examples.

The learner works in a local IDE and simulation; the site's buttons, tabs,
glossary, and hints are browser interactions. This is different from Chiron's
planned executable notebook experience.

## Visual and navigation system

Observed: a strong purple identity, large homepage logo, prominent Start Learning
button, cards for secondary destinations, persistent development notice,
search/theme controls, nested course navigation, previous/next links, code-copy
controls, and collapsed hints. A sidebar topic selector changes the section.
The active course branch expands, reducing the amount of unrelated content shown.

Source CSS uses Noto Sans, a nominal 0.875rem body size, 1.7 line height, purple
`#924dc3` accent and lighter dark-mode link color. These are observed source
choices, not recommended accessibility targets. No contrast audit was performed.

## Maintainability mechanisms

| Mechanism | Why it matters | Source |
|---|---|---|
| Section folders plus explicit sidebar | Course order is editorial; folder location alone is insufficient | `src/content/docs/`, `src/config/sidebarConfig.ts` |
| Topic configuration derives from sidebar data | Reuses content structure for navigation | `src/config/sidebarTopics.ts` |
| Shared Astro components and Markdown plugins | Consistent callouts, media, glossary, layout | `src/components/`, `src/plugins/` |
| Region-based example embedding | Docs display source code from the examples tree | `remark-code-region.ts`, `codeRegionSources` frontmatter |
| Example build workflow | Compiles example projects; does not establish real-hardware behavior | `.github/workflows/compile.yml` |
| Copybara configuration | Publishes template/solution subtrees to learner-facing repositories | `copy.bara.sky` |
| Formatting, linting, region checks, type checks, prose checks | Reduces review effort and mechanical drift | `package.json`, contribution style guide |
| Site build + link validator + PR previews | Finds broken content and exposes reviewable rendering | `astro.config.mjs`, `.github/workflows/` |

[Configuration](https://github.com/frcsoftware/frcsoftware.org/blob/a5cea0436c10b6da9017b3464ac4c265771afcf3/astro.config.mjs),
[package scripts](https://github.com/frcsoftware/frcsoftware.org/blob/a5cea0436c10b6da9017b3464ac4c265771afcf3/package.json),
[style guide](https://frcsoftware.org/contribution/styleguide/)

The source uses Astro/Starlight + MDX with custom overrides, not MyST.
An in-page-outline override is selective; its directory configuration still
contains a design-handbook entry inherited from the other site. Its README
describes a GitHub Pages deployment workflow absent from this snapshot, whereas
the current preview workflow uses Cloudflare Wrangler. Therefore the README
alone does not establish the current production hosting path.

The repository README identifies content as CC BY-NC-SA 4.0 and examples as
BSD 3-Clause. Preserve provenance when considering actual reuse; the present
notes summarize design patterns, not copied curriculum.

## Transfer to Chiron

Adopt the progression, repeated robot problem, staged hints, educator checkpoints,
source-backed code snippets, and build checks. Use native MyST equivalents first.
Do not transplant Java-specific classes, MDX components, the full custom frontend,
or unfinished syllabus promises. Keep a small native authoring vocabulary so
students can contribute without learning a web framework.

