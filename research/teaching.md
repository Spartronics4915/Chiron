# Teaching and writing direction

Reviewed 2026-09-22. This note records evidence and its application; it does not
claim that Chiron itself has been evaluated in a classroom.

## Current delivery and writing direction

User clarification, September 23: independent study, with students teaching students.
Help should remain implicit in the student path. Required checks must give enough
information to complete them without a reviewer, partner, or approval. This
supersedes older mentions of mentor checkpoints in supporting notes.

Reread the user's private email samples for voice only: connected conversational
paragraphs, concrete reasons for suggestions, contractions, and direct requests.
Do not copy personal details or imitate typos. Preserve precision in definitions
and commands even when a more casual phrase would sound closer to an email.

The user supplied [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
as an editorial reference. Reviewed September 23: apply its observations about
repeated formulas, empty emphasis, vague significance, and excessive formatting.
It is descriptive guidance, not a detector or a reason to remove useful tables,
technical comparisons, or beginner explanations. Move repeated solution-use
instructions to the course introduction and make exercise headings describe the task.

The former Linux installation handoff now points to
[uv installation](https://docs.astral.sh/uv/getting-started/installation/) and uses
the documented [version-specific Python install](https://docs.astral.sh/uv/guides/install-python/).
These sources were checked September 23; Linux execution still needs a platform pilot.

## September 23 concept-teaching revision

User feedback requested more explanation of control and robot structure, diagrams,
and smoother onboarding. Added original goal/feedback, action-state, ownership,
and position-feedback diagrams with adjacent prose. Ask students to predict,
explain the arrows, and apply the model to a new requirement. This applies the
existing explanation/retrieval guidance below; no separate claim about the
effectiveness of these particular diagrams is made.

Technical sources refreshed September 23:

- [WPILib control basics](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/introduction/control-system-basics.html): control terminology.
- [PID](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/introduction/introduction-to-pid.html)
  and [feedforward](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/introduction/introduction-to-feedforward.html): qualitative controller behavior and model-based effort.
- [Subsystems](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html)
  and [project structure](https://docs.wpilib.org/en/stable/docs/software/commandbased/structuring-command-based-project.html): encapsulation and ownership. Current course files remain the source for our actual layout.
- [Python environments](https://docs.python.org/3.14/tutorial/venv.html),
  [VS Code environments](https://code.visualstudio.com/docs/python/environments),
  and [Python 3.14.7](https://www.python.org/downloads/release/python-3147/): isolation, interpreter selection, and release-specific installer choices.
- [RobotPy installation](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/python-setup.html): supported platforms and Windows runtime requirement.

Numerical arm examples and response traces are original illustrative arithmetic,
not measured robot data or suggested tuning values. Arm implementation remains
outside the current intake assessment. New source content does not establish
fresh-clone or cross-platform installation success; record those checks separately.

## Primary studies and professional guidance

- Sentance, Waite & Kallia (2019), *Teaching computer programming with PRIMM:
  a sociocultural perspective*, DOI
  [10.1080/08993408.2019.1608781](https://doi.org/10.1080/08993408.2019.1608781).
  [Author manuscript](https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/57800/Waite%20Teaching%20computer%20programming%202019%20Accepted.pdf?isAllowed=y&sequence=2).
  The study involved 493 pupils aged 11–14 across 13 schools over 8–12 weeks;
  the PRIMM group performed better on the post-test than the comparison group.
  This supports reading, predicting, discussing, modifying, then creating code.
  It does not establish an FRC training duration or guarantee independent mastery.
- Margulieux, Morrison & Decker (2020), *Reducing withdrawal and failure rates in
  introductory programming with subgoal labeled worked examples*,
  [International Journal of STEM Education](https://link.springer.com/article/10.1186/s40594-020-00222-7).
  The semester study included 265 introductory students. Subgoal instruction
  improved early quizzes and reduced failure/withdrawal; mean exam performance
  did not significantly improve. Apply meaningful labels to reasoning steps,
  such as “read the input” and “choose the output”; do not promise universal gains.
- Pashler et al. (2007), [IES practice guide: Organizing Instruction and Study
  to Improve Student Learning](https://ies.ed.gov/ncee/wwc/PracticeGuide/1).
  Recommendations include spacing, alternating examples with problems, retrieval,
  and explanatory questions. Its evidence ratings vary: retrieval re-exposure
  and explanatory questions have stronger backing than pre-questions. Use short
  delayed reviews and ask why a result occurs, without presenting every choice
  as equally proven. This is cross-subject guidance, not an FRC-specific study.
- [Raspberry Pi Foundation computing pedagogy](https://www.raspberrypi.org/teach/pedagogy):
  professional guidance emphasizing code reading before writing, structured
  progression, familiar contexts, and dialogue. Use partner explanation and
  teacher feedback, while retaining a usable self-paced route.

## Concrete Chiron choices

Define files, programs, editors, terminals, and repositories before asking students
to use them. Separate installation, version control, and Python syntax into readable
pages. Begin with complete tiny programs, trace values, change one aspect, then
solve a related task. Explain every new symbol. Revisit earlier ideas in later
exercises; keep solutions available but ask for an attempt first. Teach error
messages before complicated projects. Assess transfer using a new requirement,
not only the ability to replay a demonstrated solution.

These are our design applications, not tested effect sizes. Pilot with new students
and record where they need unstated help, not just whether a page was completed.

## User-authored references and voice

Read branch `temp` at
[`3adac498b85dda45da8561a016c42e3b19532e79`](https://github.com/Spartronics4915/Chiron/tree/3adac498b85dda45da8561a016c42e3b19532e79):
`docs/course/setup/required_tools.md`, `vs_code_overview.md`,
`docs/course/stage_0/overview.md`, `docs/hardware/cameras/limelight.md`, and
`docs/reference/photon/{photon_lib,getting_target_data}.md`.
The course has setup before Stage 0. Several opening pages are placeholders.
Limelight is a physical setup/configuration guide; Photon is task-oriented library
usage with short snippets. Neither is intended as a generic model-contract section.

The user's private email samples were read solely for voice; do not copy the
emails or their personal details into the repository. Write directly to the
student, introduce what a tool does and why it helps, use connected explanations
and concrete instructions, and explain unfamiliar terms conversationally. Preserve
that warmth without reproducing typos or unsupported technical claims.

FRCSoftware remains the structural reference: setup, fundamentals, working robot,
then command-based rewrite of familiar behavior. Use original Python examples;
do not copy its Java-specific ordering or licensed prose. This is a pedagogical
adaptation, not a translation of its lessons.
