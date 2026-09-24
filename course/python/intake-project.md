---
title: Stage 0 Project - Model an intake
---

You've worked with decisions, loops, functions, collections, and objects.
Now use those ideas together with fewer instructions. You can look back at earlier
lessons, but write down your intended behavior before opening the solution.


```{include} ../../snippets/terminal-reminder.md
```

## What you're building

An **intake** is the mechanism that brings a game piece into the robot. For this
project we're modeling its decisions, not connecting a physical motor. Positive
output means collect, negative output means release, and zero means stop.

Copy a fresh project with `python tools/start_exercise.py intake-model`.
Work in `student-work/intake-model`, where `intake.py` and `main.py` are provided.
The starter runs, but its intake is deliberately inactive. Your job is to implement
the behavior and add checks; “it runs” is not yet “it meets the requirements.”

## Requirements

1. `Intake` starts with no piece and output zero.
2. `update(request, enabled, detected)` remembers the latest sensor state.
3. Disabled output is always zero.
4. A detected piece blocks positive collection, but reverse release remains possible.
5. An allowed request is limited to [-1, 1].
6. `stop()` makes output zero without inventing a new sensor reading.
7. A `Robot` object owns an Intake; `main.py` demonstrates a sequence of updates.
8. Two instances keep independent state. The logic is defined in one reusable file.

## Plan, then build

Make a table of inputs and expected outputs. Include exactly zero, both bounds,
out-of-range values, disabled requests, and detected/not-detected conditions.
Implement one rule, run the program, and add an assertion. Repeat until the table
is covered. Avoid changing all the rules at once when one check fails.

:::{hint} Which rule wins?
:class: dropdown
Check disabled first. Next check whether positive collection is blocked by a piece.
Only then limit an otherwise allowed request. Store the sensor state on every update.
:::

::::{dropdown} Compare with a completed model
The maintained solution lives in `examples/intake_model/solution`. Run it with
`python examples/intake_model/solution/main.py` after your own attempt.

```{literalinclude} ../../examples/intake_model/solution/intake.py
:language: python
```
::::

## Check your model

Run your checks for collection, detection, release, disable, and independent
instances. Explain each attribute and why a method uses `self`. Temporarily change
the piece-detection rule from `request > 0` to `request < 0`. Your checks for
collection and reverse release should catch the mistake. Restore the comparison.

Now limit forward collection to 0.4 while still allowing reverse down to -1.0.
Write the expected results for requests of 0.2, 0.8, and -0.8 before editing.
With the intake enabled and no piece detected, those results should be 0.2, 0.4,
and -0.8. Run your earlier checks too, updating only expectations affected by
the new limit.

In `student-work/intake-model/README.md`, describe how to run your model, what it
represents, and one limitation. Commit and push. The next stage uses the same
decisions inside an actual RobotPy program.
