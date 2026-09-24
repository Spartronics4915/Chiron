---
title: Run the intake in simulation
---

Let's make your program's behavior visible. The course supplies a small
simulation that acts like an intake motor and piece detector. It models enough
to test decisions, not the mechanical details of a real intake.

## Launching the Copy

```{include} ../../snippets/terminal-reminder.md
```

From the Chiron root, using your environment's Python, run:

```sh
python tools/run_robot.py student-work/periodic-intake
```

The launcher finds `robot.py` in that folder and starts RobotPy's HAL simulation
window. It also makes the shared course helpers importable. Keep the terminal
open; errors from the program appear there. Ctrl+C in the terminal stops it.
If the window doesn't open, check the terminal output. A missing `robot.py` means
you need to check the assignment path; a missing module means you should repeat
the [environment check](../setup/python-environment.md#check-python-environment).
The launcher runs simulation only.

## Controls

In the simulation window, open **Robot State** and **NetworkTables** from the
available menus if they aren't visible. In NetworkTables, expand `/SmartDashboard`.
These are values shared by the robot program with diagnostic tools. Our program
creates them with `wpilib.SmartDashboard.putNumber` and `putBoolean`; `getNumber`
and `getBoolean` read current values.

| Value | What you do with it |
|---|---|
| `Intake request` | Edit a number from -1 to 1: positive collects, negative releases |
| `Piece available` | Edit a boolean: false prevents simulated acquisition |
| `Intake output` | Observe what the mechanism is actually requesting |
| `Has piece` | Observe the simulated detector |

Robot State is where you choose the robot's mode and enable it. NetworkTables
holds the named inputs and readings in the table above. The dashboard stands
in for physical controller input during this course.

## Complete Cycle

1. Start disabled. Set `Intake request` to 0.5. Output should remain zero.
2. Select **Teleoperated**, then **Enabled** in Robot State.
3. Watch output become 0.5. After roughly 0.4 seconds, `Has piece` becomes true
   and the output returns to zero on a following periodic update.
4. Set request to -0.5. The intake releases; the detector becomes false.
5. Set request to zero, then disable. Output should be zero.

If the detector begins true, restart the program to get a fresh initial state.
Always return inputs to zero before re-enabling so an old request doesn't surprise
you. Our simulated piece source can supply another piece after release.

## Model Information

`IntakeSim.set_output(request)` bounds output to [-1, 1] and inhibits it when
disabled. `step(0.02)` advances the simplified detector. Attributes `detected`,
`piece_available`, and `output` expose its state. That shared support is already
provided so you can focus on program behavior. It is not an electrical guide or
a calibration for a real motor.

Before continuing, set `Piece available` false and predict what forward collection
does. Explain the difference between an operator request, a motor output, and a
sensor result. Write down the observed values, not just “it worked.”
