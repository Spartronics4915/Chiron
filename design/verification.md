# Verification record

This file records checks actually run. It is not a claim that learners have completed
the course or that the site has been published.

## Course rewrite, September 22–23, 2026

- Clean-kernel notebook execution completed locally. The browser JupyterLite kernel
  also ran the object-state notebook: the first run displayed length 4, rerunning
  the second cell displayed 5, and resetting restored the saved initial results.
- The notebook download menu exposed an `.ipynb` file in the static artifact.
- Browser checks confirmed course search results and hint disclosure, including
  keyboard activation. Full accessibility and supported-OS audits remain outstanding.
- Root and `/Chiron` HTML exports passed rendered internal link/asset checks.
- Deterministic mechanism tests exercised acquisition, timeout without success,
  release, requirement conflicts, cancellation, disable, rescheduling, and defaults.
- RobotPy's actual basic and command-based programs each passed its four built-in
  lifecycle checks. These are simulation results, not hardware validation.
- Starter-copy tests verified overwrite refusal. A disposable Git repository
  demonstrated that merging an upstream lesson fix preserves committed assignments.

## September 23 feedback revision

Validation completed with Python 3.14.7 and Node 24.21.0:

- Content checks passed for 41 published pages and 13 explicit labels; Ruff passed.
- All 61 example and student-workflow tests passed, including the canonical first
  pytest example included in the subsystem lesson.
- Both RobotPy programs passed their four built-in lifecycle checks (eight total).
- The demonstration notebook executed successfully from a clean kernel.
- Root and `/Chiron/` HTML exports passed rendered internal link and asset checks.
  Content validation and both exports were repeated successfully after the final
  prose and shared terminal-reminder changes.
- The documented Windows Command Prompt activation selected the workspace's
  `.venv/Scripts/python.exe`, verified by printing `sys.executable`.
- `git diff --check` reported no whitespace errors.

Logs are generated under `_build/reports/` and are not source files. The earlier
browser checks above were not repeated for this prose revision.

## September 23 concept and onboarding revision

- Full validation passed: 43 published pages, 15 explicit labels, Ruff, all 61
  example/workflow tests, clean notebook execution, and eight RobotPy lifecycle
  checks. Python 3.14.7 and Node 24.21.0 were used.
- Root and `/Chiron/` builds and rendered link/asset checks passed, including
  another content/site check after final heading and narrow-layout edits.
- Windows Command Prompt activation selected this project's environment and the
  documented `wpilib`/`commands2` import check printed `RobotPy is ready`.
- Headless Edge rendered all four new Mermaid diagrams without syntax errors.
  The three new concept pages and the existing VS Code screenshot page were
  checked at 1280px and 390px widths. After shortening headings whose link markers
  overflowed, none of those four pages had horizontal document overflow at 390px.
  Screenshots are local generated review artifacts under `_build/reports/`.
- The removed updates/reviews page was not restored. Its orphan TOC entry and
  links were replaced with a brief review section in the existing Git lesson.
- `git diff --check` passed. No dependency or robot behavior change was required.

These checks use the existing Windows development environment. They do not verify
fresh Python/runtime installation, Linux installation, every viewport, or a full
accessibility audit. No additional notebook browser-execution claim is made here.

## Still required before a supported cohort release

Publish reviewed source and a real cohort baseline; test installation from a fresh
clone on the supported operating systems; observe new students using the lessons;
review their independent mechanism changes. GitHub Actions definitions have been
prepared locally but no hosted run or deployment is claimed here. No physical
device configuration or vendor-library reference content was added in this scope.
