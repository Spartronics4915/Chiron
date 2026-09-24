---
title: Contributing to Chiron
---

The active scope is the beginner course through a mechanism subsystem. Hardware
guides will cover physical setup, flashing, settings, and troubleshooting. API
reference will give concise, task-oriented guidance for team libraries. Those two
sections are deliberately deferred; the existing `temp` branch supplies examples
of the intended approach, not material to overwrite with generic reference pages.

Students need only the documented Python environment. Site contributors additionally
need Node from `.node-version` and uv 0.11.28. From the repository root:

```sh
uv sync --frozen --group docs
npm ci
uv run python tools/validate.py
npm start
```

The validation command checks the course structure, code, notebooks, and both
root/subpath HTML builds. The final static artifact is in `_build/html`, built for
`/Chiron`. Preview that artifact using
`uv run python tools/preview.py --base /Chiron`.

Keep `student-work` out of team PRs. Describe the student problem, resulting change,
and verification. Review the corresponding exercise and teaching notes whenever a
lesson changes. See [authoring](authoring.md) for content conventions.

The repository's existing license applies to its material. FRCSoftware and FRCDesign
inspire progression and teaching patterns; these Python lessons are newly written,
not copied Java lessons. Adapted external material needs source attribution and
license review. Research notes preserve provenance outside the published site.
