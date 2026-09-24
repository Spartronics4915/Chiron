# Chiron: baseline and application

## Verified baseline

Public repository: [Spartronics4915/Chiron](https://github.com/Spartronics4915/Chiron).
Inspected main revision: `8114652213e4facc99f827d29a1c1db4eb825b4c`.
Repository metadata gives [GitHub Pages](https://spartronics4915.github.io/Chiron/)
as its homepage; the user confirms it is hosted there. Live rendering was not
verified because the web reader could not retrieve it.

The complete tracked-file list is only seven files: `.gitignore`,
`.github/workflows/deploy.yml`, `LICENSE.md`, `README.md`,
`images/site_logo.png`, `myst.yml`, and an empty `requirements.txt`.
There are no course pages or notebooks in this main-branch snapshot.
The local workspace initially had only `.git` and no remote.

[MyST configuration](https://github.com/Spartronics4915/Chiron/blob/8114652213e4facc99f827d29a1c1db4eb825b4c/myst.yml):
`book-theme`, title `Documentation`, a logo, no explicit TOC, empty description,
and `project.github` pointing to `SPUD42AG/Resources`. That old value should be
corrected when implementation begins: repository links and some execution
defaults depend on it.

[Deployment](https://github.com/Spartronics4915/Chiron/blob/8114652213e4facc99f827d29a1c1db4eb825b4c/.github/workflows/deploy.yml):
pushes to main build with Node 18.x and an unpinned global `mystmd` installation,
then upload `_build/html`. `BASE_URL` comes from the repository name. It does
not install Python dependencies or execute notebooks. A requirements file alone
would not change that. The README is a placeholder.
[License file](https://github.com/Spartronics4915/Chiron/blob/8114652213e4facc99f827d29a1c1db4eb825b4c/LICENSE.md)
is headed CC BY 4.0.

## Proposed directions, not implemented or approved architecture

1. Keep one MyST project initially. Use top-level landing pages for Course,
   Hardware, API Reference, and optionally Educators/Contributing.
2. Use explicit `project.toc` ordering for the course. Allow patterns only where
   automatic ordering is intentional. Reuse TOC-derived child lists instead of
   maintaining another lesson list in prose.
3. Keep section folders and choose URL policy before publishing many pages.
   `site.options.folders: true` is a candidate; confirm it against the pinned
   MyST version and test the GitHub Pages base path.
4. Prefer Markdown for explanations and notebooks for executable work. Every
   notebook should have a meaningful static reading experience.
5. Separate introductory Python execution from robot simulation/deployment.
   Browser Python support does not establish RobotPy/vendor-library compatibility.
6. Link authoritative API documentation with a tested version and short team
   context. A complete copied vendor API reference would create unnecessary drift.
   Decide separately whether team-owned APIs warrant generated reference pages.
7. Pin the build toolchain, validate internal links/labels and TOC targets, execute
   representative notebooks in a clean environment, and preview changes before
   deployment. Keep deployment configuration separate from lesson content.

Possible layout to discuss later:

```text
myst.yml
index.md
course/
  index.md
  setup/
  python-foundations/
  robot-basics/
  commands/
  controls/
hardware/
  index.md
api/
  index.md
educators/
contributing/
assets/
examples/
```

This is a grouping sketch, not a syllabus. The team's RobotPy/WPILib season,
robot controller, vendors, student starting level, meeting cadence, and expected
completion outcomes remain undecided. Resolve these when the related work begins,
not by inheriting FRCSoftware's Java choices.

## Suggested lesson contract

Objective and prerequisites → brief explanation → worked example → student task
→ optional staged hints → observable success checks → reflection/review → next
lesson. Reference pages instead answer a specific lookup question quickly.
An educator note should identify misconceptions, checkpoints, and extension work.

## Portability

MyST's static HTML output makes a future host move plausible without rewriting
lessons. Rebuild for the destination base path, test assets/deep links/downloads,
preserve or redirect public URLs, and separately account for any notebook
execution service. Static hosting does not itself supply a Python kernel.

