# Decisions and implementation status

## 2026-09-23: paths for restored hardware and reference pages

The user restored hardware and library reference files and requested path fixes.
Publish those existing files under `/hardware/` and `/reference/`, with explicit
TOC paths; omit the empty WPILib section until it has pages. Restore the Limelight
images from `origin/temp` to the shared `images/` directory. Teaching and
contributing pages remain reachable through links but hidden from the sidebar.
This updates publication scope without expanding or reviewing the hardware/API
content. Source validation now covers both restored sections and figure paths.

## 2026-09-23: independent study and student authorship

The user clarified that students teach students and the course must be completable
independently. Help is available in practice but should not be advertised as a
required step. Replace mentor-directed reviews, partner tasks, and surprise changes
with written self-checks, specified fault exercises, and concrete expected results.
Teaching notes serve student authors and optional collaboration; they do not gate
progress. This supersedes the approval/checkpoint language in the original plan
and previous decisions, which remain historical records outside publication.

Retain the user's edited titles and content. Use the private writing sample only
for voice. Remove repeated solution preambles and generic closing instructions;
keep definitions, tracing, technical contrasts, and structured comparisons where
they teach something. Record the editorial reference in research/teaching.md.

Published pages no longer use mentor wording. The setup fragment `mentor-review`
becomes `code-review`; all local callers are updated. Existing page paths stay
unchanged, including `/educators/`, now labeled Teaching Notes in navigation.
Linux setup gains a documented uv-based Python installation path instead of an
unstated human dependency. The RobotPy/Python baseline and robot code stay unchanged.

## 2026-09-23: concept teaching and setup clarity

Preserve the user's edited titles, prose, and screenshots. Add conceptual lessons
on high-level goals versus low-level effort, robot program responsibilities, and
feedback/PID intuition. Use original Mermaid diagrams, numerical examples, and
prediction/explanation exercises before implementation. Link the existing teaching
evidence and official WPILib references; don't imply that diagrams alone establish
learning. Keep the independent intake subsystem as the assessed endpoint. Arm
control is a conceptual transfer exercise, not a new hardware or tuning project.

Retain the project virtual environment for dependency isolation. Explain its
purpose and separate one-time creation/install from per-terminal activation.
Give exact Python release navigation, expected outputs, troubleshooting, and a
returning-session checklist. Use Command Prompt consistently for the Windows
route. Linux installation remains distribution-specific and mentor-assisted;
cross-platform installation has not been newly certified by editing these pages.
Correct the user's screenshot paths and numbered explanations without replacing
the images. No dependency or executable robot behavior changes in this revision.

## 2026-09-23: beginner onboarding and editorial feedback

Remove the required unknown baseline placeholder from individual setup. Students
branch from their cloned version and record its identifier; mentors have an explicit
publish/validate/select-version checklist for a fixed cohort. This does not claim
the local source or a release has already been published.

Make short `python` commands reliable by teaching environment activation (Command
Prompt on Windows, avoiding PowerShell policy changes), verifying the interpreter,
and including one shared reminder near runnable work. Give an editable greeting
on the first setup page. Simplify Stage 0 explanations and move advanced assertion
qualifications into optional detail. Add attempt/reflection prompts around solutions
and short intermediate explanation checks, without accounts or forced attempt gates.

Move the first subsystem test into canonical included source and the actual pytest
collection. Record verification separately, including limits of local testing.

## 2026-09-22: user-directed course rewrite (current)

The user rejected the compressed first draft and clarified the intended sections
using `temp` at `3adac498b85dda45da8561a016c42e3b19532e79`. Hardware guides concern
physical device work (flashing, configuration, troubleshooting); API reference is
quick guidance for team libraries. Defer both. Earlier generic pages are removed
from publication and preserved only in an ignored local archive.

The user explicitly lifted the month limit: continue through confidently writing
a mechanism subsystem. Use setup before Stage 0, then working mechanism and
command-based refactoring as in FRCSoftware. Expand beginner explanations of files,
editor, terminal, Git, syntax, tracing, state, and framework ownership. Use the
conversational, explanatory voice of the user's examples, without copying private
emails. Research backing and boundaries are in `research/teaching.md`.

The intake is the consistent teaching example. Larger robot integration and control
theory remain future work. A notebook is used only to expose object aliasing and
execution state. No claim of student proficiency is made merely because pages or
canonical tests are complete; the final independent change and mentor review matter.

The remaining entries below record previous decisions, superseded where noted.

## 2026-09-22: first-month boundary

User requested stopping after enough material for roughly one month. Publish stages
0–2 only: setup, Python foundations, and periodic drivetrain/intake simulation.
Plan approximately twelve 60–90 minute sessions; this estimate needs a real pilot.
Later stages remain roadmap items. Existing command/arm code is reference
infrastructure, not a claim that those lessons are complete.

## Environment and model

Python 3.14.7, RobotPy/commands2 2026.2.2, Node 24.21.0, MyST 1.11.0.
Lock Python/Node dependencies; export a student pip requirements file. Browser
notebooks contain no RobotPy or vendor code. Dashboard inputs substitute for
physical controller/device adapters. The deterministic model has simplified
drive/intake dynamics and idealized disabled braking; never use it for hardware
calibration. The simulation programs reject real hardware.

## Follow-up before a supported cohort release

- Have a new student complete setup and the month, recording friction and timing.
- Validate supported operating systems beyond this Windows development host.
- Have mentors approve the electrical/hardware checkout guidance for the team.
- Publish an actual baseline tag and release notes; no tag is invented in setup.
- Expand stages 3–6 only after this initial slice is reviewed.

See [verification.md](verification.md) for actual checks and remaining technical
limits. Record future changes here rather than rewriting approved design history.
