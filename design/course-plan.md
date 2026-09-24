# Chiron: course structure and development direction

Approved user design, September 2026. This document preserves the project direction;
implementation scope and later decisions belong in [decisions.md](decisions.md).
Supporting evidence is in the [research pack](../research/README.md), especially
[MyST](../research/myst.md), [FRCSoftware](../research/frcsoftware.md), and
[FRCDesign](../research/frcdesign.md). Research observations do not override this plan.

## Purpose and principles

Take a student with no programming experience to the point where they can build,
simulate, debug, and explain a basic full robot program, then use documentation
to tackle more complex mechanisms independently. Use a self-paced course with
mentor checkpoints, local tools installed before starting, simulation before
hardware, and one student fork/clone. Notebooks supplement normal IDE work.

Transfer FRCSoftware's progressive robot projects, staged hints, reusable examples,
and separate educator guidance; FRCDesign's repeated practice, reduced scaffolding,
self-review, and distinction between lessons and references.

## Learning progression

Use one simple practice robot: differential drivetrain, intake with piece detection,
and pivoting scoring arm. Supply simulation infrastructure initially.

| Stage | Content, in order | Completion evidence |
|---|---|---|
| 0 Setup | Website features; Python/venv; VS Code/notebooks; Git/GitHub; fork/clone; dependencies; files/tests/simulation | Run a file, edit a notebook, launch simulation, commit |
| 1 Python | Values/variables; expressions/booleans; conditionals; loops; functions; lists/dictionaries; modules; classes/composition | Multi-file mechanism model; explain state/behavior |
| 2 Working robot | Lifecycle/periodic; IO; motor commands/configuration; controller input; drivetrain/intake; telemetry; timed auto | Operate simulated robot and diagnose an injected fault |
| 3 Commands | Subsystems; commands; scheduler/requirements; defaults; triggers; sequences/parallel actions; interruption/cleanup | Refactor the same robot without behavior loss |
| 4 Control | Sensors; units/signs; position/velocity; calibration/homing; limits; feedback; PID intuition/tuning; feedforward; diagnosis | Target arm position, explain response plot, handle limits/invalid conditions |
| 5 Integration | Combine mechanisms; operator coordination; possession/state; autonomous composition; timeouts/recovery; configuration/troubleshooting | Full teleop and acquire–position–score auto |
| 6 Independent extension | Unfamiliar APIs; adapting mechanisms; team code; advanced resources | Implement a modest written requirement and defend choices |

Debugging starts with the first traceback: inspect values, predict execution, and
write small assertions before larger tests. Git progresses from saving/committing
to branches, meaningful diffs, and pull requests. Core ends at basic integration;
swerve, advanced paths, vision, pose estimation, and advanced control are extensions.

Each lesson follows outcome/prerequisites → predict/explain → worked example and
mistakes → modified/independent practice → staged hints/solution → observable checks
and reflection → next lesson/reference. Reduce instructions as capability grows;
reuse familiar mechanisms while introducing new concepts. Follow interactive
exploration with normal Python files so cell state does not replace execution literacy.

Use stage demonstrations rather than accounts or mandatory tracking: demonstrate,
explain, diagnose, and make an unannounced small modification. Educator companions
contain prerequisites, misconceptions, questions, outcomes, and extensions, linking
the student sequence rather than duplicating it. Final assessment includes full
robot behavior, reproducible startup, useful telemetry, and code review. Physical
deployment is a separate supervised checkout.

## MyST experience and references

Use `book-theme`, limited shared CSS, explicit course TOC, and folder-based URLs.
Six destinations: Learning Course, Hardware Guides, API Reference, Examples and
Extensions, Educator Guide, Contributing. Global navigation selects destinations,
sidebar shows structure, outline supports scanning. Keep authoritative hardware/API
explanations in references; curate official APIs instead of copying vendors' docs.

Use notebooks for Python state, sensor readings, units, motion, and response
experiments; in-page execution for changed parameters; widgets for setpoints/gain/
noise/load; labeled exercises/solutions; dropdown hints/mistakes; synchronized
OS/vendor tabs; glossary/xrefs; figures/equations/diagrams; included tested source
and embedded outputs; cards/search/TOC-derived lists. Keep essential instructions
visible. Use Markdown for ordinary explanations, notebooks for executable work;
do not maintain paired copies.

Browser execution uses MyST JupyterLite/WASM, independent of RobotPy and vendor
packages; full robot simulation remains local. Validate a representative notebook
with plot, widget, reset/rerun, and download before scaling. Every interactive page
has useful static results and a downloadable notebook, with explicit persistence
instructions. Unsupported widgets must leave editable cells/local execution usable.
Execute demonstration/solution notebooks from clean kernels in CI; explicitly
exclude unfinished exercise cells and test completed solutions separately. Generate
outputs rather than copying them into prose. Execution features require testing
against the pinned toolchain, not merely configuration.

## Repository and maintenance

Keep published content, canonical starters/solutions/shared simulation, checks,
and authoring infrastructure in one repository with clear responsibilities.
Students copy starters into committable `student-work`, excluded from publication
and canonical checks. Research/design are outside published navigation. Only site
contributors require Node/MyST; students need the Python environment.

Students fork once, clone their fork, and create a learning branch from a published
cohort baseline. `origin` is their fork and `upstream` the team repository.
Document commit/push/recovery/restart, compatible upstream updates without losing
assignments, mentor reviews within the fork, and separate site-contribution branches.
Keep a cohort on one compatible baseline; apply compatible fixes during the cohort
and reserve breaking changes for new releases. Display the environment in setup.

Make explicit MyST TOC the source of course order and derive lists from it.
Use stable descriptive filenames/labels, with numbering in navigation. Keep assets
near owners and genuinely shared assets separate. Include tested snippets, document
small shared helpers, use lesson templates, and review educator notes/examples with
lesson changes. Pin Python/RobotPy/notebook/Node/MyST compatibility; use released APIs.
Preserve adaptation licenses and provenance. Publish complete slices incrementally
and distinguish roadmap from usable lessons. URLs, labels, downloads, and exercise
entry points are public interfaces requiring link updates and migration notes.

## Validation and delivery

PRs validate content/TOC/labels, MyST-compatible authoring, Python examples, clean
notebooks, HTML, and rendered internal links/assets. Upload review artifacts and
failure reports without publishing. Main runs identical checks and deploys only the
validated artifact from the official repository. Cache dependencies and cancel
superseded validation. Student forks must not deploy the team site.

Scheduled maintenance checks external links and dependency updates separately,
reporting actionable failures. Transient external outages do not block ordinary
PRs; internal links/assets do. Releases tag a compatible curriculum/example baseline
and record environment and significant changes.

Foundation acceptance: documented fresh-clone setup; no website build needed by
students; upstream fix preserves assignments; clean local/browser notebooks and
understandable static fallbacks; deterministic simulation checks for interruption,
timeouts, limits, and disable; narrow/wide and keyboard usability of navigation,
search, code, diagrams, tabs, hints; root and `/Chiron/` builds; no research,
submissions, caches, or development files published as course pages.

Implementation sequence: foundation and representative notebook → complete setup/
initial Python slice → remaining Python/basic robot → commands/control/integration
and needed references → real-student pilot and refinement before advanced expansion.
The immediate priority is a small complete maintainable learning experience.
