---
title: Timed actions and debugging
---

When nobody is holding a controller, our program still needs to know when an
action should finish. A sensor can confirm success, and a timer can keep the
program from trying forever if the expected event never happens.

## The Timer

In your periodic example, `self.timer = wpilib.Timer()` creates a timer.
`restart()` resets and starts it in `autonomousInit`. `get()` returns elapsed
seconds. Autonomous requests collection while elapsed time is below two seconds,
then requests zero. Piece detection may stop the motor sooner through `set_intake`.

```{literalinclude} ../../examples/mechanism/basic/robot.py
:language: python
```

This is the full maintained example. Compare the callbacks to your copy rather
than pasting it over your work. The simulation callbacks are supplied infrastructure;
you should understand their purpose without having to implement a simulator.

## Both Outcomes

Restart with a piece available, enable autonomous, and observe detection stop the
intake. Then restart with `Piece available` false. It should stop after about two
seconds without reporting a held piece. A **timeout** means time ran out; it does
not mean acquisition succeeded. That distinction matters before any later action
that assumes the robot has a piece.

## Small Change

Change the acquisition limit to one second. Then add a dashboard status string
using `wpilib.SmartDashboard.putString("Intake status", text)`. Use three messages:
`collecting`, `piece detected`, and `timed out`. Choose the message from observed
conditions; don't report success merely because the timer expired.

:::{hint} Order the questions
:class: dropdown
Ask whether a piece is detected first, then whether time remains. If neither
condition allows collection, stop and report timeout. Keep each periodic call short.
:::

## Diagnosing Faults

Temporarily change the sensor rule so it blocks negative output instead of positive
output. Predict the symptom, reproduce it, inspect request/output/detection, then
repair the comparison. Use the same reproduce–inspect–change–rerun process from
the first debugging lesson.

To finish this stage, run teleop collection and release, timed autonomous with
and without a piece, and disable during motion. Write down what you expect in
each case and compare it with the result. Explain why resetting the timer in
every periodic call would prevent timeout. Commit your working version before
reorganizing it in the next stage.
