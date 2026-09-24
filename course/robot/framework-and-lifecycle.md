---
title: Robot Programs
---

The programs you've written so far start at the top and finish at the bottom.
A robot needs to keep responding while a match is running. RobotPy supplies a
**framework** that manages the repeated work; we write the methods it calls.
The [control overview](control-and-feedback.md) described the decisions; this
lesson explains when the program gets a chance to make them.


```{include} ../../snippets/terminal-reminder.md
```

## A class can build on another class

Earlier, `Robot` *had an* `Intake`. That was composition. Here,
`class Robot(wpilib.TimedRobot):` says our class builds on a framework class.
This is **inheritance**. `TimedRobot` supplies the robot loop; our Robot specializes
it by defining methods with names the framework recognizes.

When our class defines `teleopPeriodic`, it **overrides** the inherited behavior
for that callback. A **callback** is a method the framework calls at the appropriate
time. We don't call `teleopPeriodic()` in a while loop ourselves.

| Callback | When it runs | A useful job |
|---|---|---|
| `robotInit` | Once when the program starts | Construct mechanisms and initial settings |
| `teleopPeriodic` | Repeatedly while in enabled teleop | Read operator requests and choose outputs |
| `autonomousInit` | When entering autonomous | Reset the autonomous timer |
| `autonomousPeriodic` | Repeatedly in enabled autonomous | Advance a bounded action |
| `disabledInit` | When entering disabled | Stop requests and cancel active work |
| `simulationPeriodic` | Repeatedly in simulation | Advance the supplied model and display readings |

Periodic calls normally occur every 0.02 seconds, or about 50 times per second.
**Teleop** means operator-controlled mode; **autonomous** means the program chooses
the actions. **Disabled** is the state in which mechanisms must not be driven.

## Read, Decide, Return

A periodic method reads the current inputs, makes a decision, writes an output,
and returns so the framework can do its other work. Don't put `sleep()` or a loop
waiting for a piece inside it. While that call is blocked, other callbacks cannot
run normally. Repeated checks belong in repeated callbacks.

```{mermaid}
flowchart LR
  Framework[Framework calls periodic] --> Read[Read current input]
  Read --> Decide[Choose output]
  Decide --> Write[Write output]
  Write --> Return[Return to framework]
  Return --> Framework
```

## Framework Example

Copy the example with `python tools/start_exercise.py periodic-intake`.
Open `student-work/periodic-intake/robot.py`. `import wpilib` makes the library
available. `self.io = IntakeSim()` creates the supplied input/output model.

Find `teleopPeriodic` and explain it in your own words: read the dashboard request,
then pass it to `set_intake`. That helper applies the same piece-detection rule
you used in Stage 0. `self.io.detected` is now the input, rather than a boolean
you typed directly into a call.

Before moving on, predict what would happen if `self.io = IntakeSim()` were inside
every periodic call instead of `robotInit`. It would continually recreate the
model and lose its state. Also identify why the timer must be reset on mode entry,
not every time a periodic method runs.
