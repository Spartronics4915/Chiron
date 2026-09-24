---
title: Checking your understanding
---

You can use these questions while working through the course or when revisiting
something you've already learned. Try an explanation from memory first, then
check the relevant lesson. Run a small example if you're unsure of the answer.

After comparing your code with a solution, close it and try a slightly different
input. If you can explain the result, the comparison gave you something you can
use. If you can't yet, trace the example one line at a time and try again.

| Topic | What to try | Question to explain |
|---|---|---|
| Setup | Open correct folder, run own file, show a commit on their fork | What happens if you save but don't push? |
| Early Python | Trace assignments and a conditional; read an error | Does changing a variable update an earlier calculated result? |
| Functions and collections | Return a decision, check boundaries, trace a loop | Is printing the same as returning? Is a detected sample a unique piece? |
| Objects and Stage 0 project | Independent instances; multi-file intake model | Do two names necessarily mean two objects? Which data survives a call? |
| Stage 1A | Teleop, timed auto, disable, observed request/output/sensor | Does a timeout prove success? Why not wait in periodic? |
| Stage 1B | Requirements, cleanup, defaults, triggers, final independent change | What owns the intake after a conflicting command schedules? |
| Control concepts | Trace request, applied effort, and measurement; calculate a proportional correction | Does half output guarantee half speed? Can a possession detector measure speed? |
| Program structure | Draw shared objects and assign a new requirement to its owner | Does moving competing motor writes into separate files fix ownership? |

Use the [control overview](../course/robot/control-and-feedback.md),
[program structure](../course/subsystems/robot-code-structure.md), and
[feedback lesson](../course/subsystems/feedback-control.md) for explanation before
implementation. Redraw a diagram from memory and label what each arrow carries,
then compare it with the page. The arm examples are a way to practice reasoning
about feedback before implementing another mechanism.

For the final project, run the tests against your own assignment. Before changing
the collection speed or timeout, write down which class needs to change and what
the new result should be. Then check that the other behavior still works.

When you return to the course, pick a question from an earlier topic before
opening your notes. You might explain `self`, trace a boolean condition, or
describe where a commit is stored before a push. Check the answer, then use the
idea in that day's work.

Common trouble spots include wrong interpreter, unsaved files, misplaced indentation,
local versus instance state, creating a new subsystem per command, forgetting
`super().__init__()`, passing a supplier's result instead of the callable, and
writing outputs outside the declared subsystem. When working with another student,
trace one of these problems together before suggesting a larger rewrite.
