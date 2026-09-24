---
title: Writing lessons that beginners can follow
---

Introduce what a tool or concept does, why a student needs it, and the next concrete
action. Use connected, conversational explanations. Explain a new name or symbol
before using it in an exercise. A concise reference entry and a beginner lesson
serve different jobs; do not compress the latter into an API summary.

Write as one student explaining something to another. Start with the problem
that makes the idea useful, then work through it in ordinary language. Keep the
user's conversational phrasing where it helps; correct ambiguity when it could
teach the wrong thing. Avoid grand claims, stock encouragement, and a repeated
summary of why every small step matters. Use a heading or table when it helps
someone find or compare information, rather than giving every paragraph one.

Every required exercise must work independently. Give students the inputs to try,
the expected results, and enough explanation to diagnose a mismatch. Don't require
another person to choose a bug, approve progress, or explain a missing setup step.
Discussion can add to the course, but completing a lesson cannot depend on it.

Start with a complete small example. Ask students to predict, run, trace, modify,
then solve a related task. Include expected results and two increasingly specific
hints where useful. Make a solution available after an attempt. Revisit earlier
concepts and ask for explanations, not only matching output. The teaching notes
links the research behind these choices.

`myst.yml` owns course order. Use descriptive lowercase filenames with hyphens;
keep Stage 0/1A/1B labels in navigation so URLs survive later rearrangement. Landing
pages use `{toc}` instead of a duplicate hand-maintained lesson list. Explicit
exercise labels must be unique. Include canonical tested source via `literalinclude`.

Use native MyST features when they help: OS tabs avoid irrelevant instructions,
dropdowns stage hints, diagrams explain flow, and the object-state notebook exposes
execution order. Do not add a widget or notebook simply to demonstrate a feature.
Essential instructions stay visible. Notebooks need saved output, download/local
instructions, and clean-kernel checks; RobotPy remains local. Do not pair notebook
and Markdown copies of the same lesson.

Published content is limited to the explicit TOC. Research, design, tools, tests,
examples, student work, and caches stay outside public page discovery. Python and
Node dependencies are locked. Regenerate student dependencies after an intentional
change with `uv export --no-dev --no-hashes --format requirements-txt --output-file requirements.txt`.

Before a cohort release, verify a fresh student clone, supported operating systems,
browser interactions, notebook fallback/download, and real learner progress. Record
a fixed reviewed baseline and environment; do not invent a release tag in setup.
Use compatible fixes during a cohort and document migrations for breaking changes.
