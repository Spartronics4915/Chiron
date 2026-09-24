---
title: Commands and Lifecycles
---

A command describes a behavior such as “collect until a piece is detected.”
The **scheduler** manages active commands. Each robot loop, it gives them a chance
to run, asks whether they are finished, and calls their cleanup when they end.

## The four lifecycle methods

| Method | Responsibility |
|---|---|
| `initialize()` | Set up each new run, such as restarting a timer |
| `execute()` | Perform a short repeated step |
| `isFinished()` | Return True when the action should end |
| `end(interrupted)` | Stop outputs and clean up, whether finished or canceled |

Constructing a command object doesn't schedule it. Calling `schedule()` asks the
scheduler to start it. `cancel()` interrupts it. `interrupted` is a boolean passed
by the scheduler: True for interruption, False for normal completion. Cleanup
must work on both paths.

## Requirements prevent competing writers

`self.addRequirements(intake)` says this command needs exclusive use of that
subsystem while scheduled. If another interruptible command owns the same subsystem,
scheduling this one interrupts the old command. Its `end(True)` cleans up before
the replacement begins its work. The scheduler uses the declared requirements
to decide which commands conflict, so each command needs to list its subsystem.

The subsystem object must be the same shared instance. Constructing a second Intake
inside each command would produce different resources and defeat that ownership.

## Read the acquisition command

Open `examples/mechanism/solution/intake_commands.py`. Focus on `Acquire` first:
its constructor saves the shared intake and creates a timer. `initialize` restarts
the timer and clears the previous success flag. `execute` requests collection.
`isFinished` returns true for a detected piece **or** an expired timeout. `end`
records success only when not interrupted and a piece is actually detected, then
stops the intake and timer.

```{literalinclude} ../../examples/mechanism/solution/intake_commands.py
:language: python
```

`timeout=2.0` in a parameter list is a **default argument**: callers can omit it
to use two seconds or supply another value. `not interrupted and ...` is the same
boolean combination you learned in Stage 0. The larger structure is new, but the
decisions are familiar.

## Implement one behavior at a time

In your assignment create `intake_commands.py` and implement Acquire with a
requirement and cleanup. Then implement Release: request -0.5, finish when no piece
is detected or after one second, and always stop in `end`. You can leave
ManualIntake for the next page.

Before running, trace these cases on paper: detected piece, absent piece, cancellation,
and a second command requiring the same intake. For each, state whether `end`
receives True or False and whether acquisition can claim success. A timeout is
normal command completion but unsuccessful acquisition.

[Next: connect the robot and operator controls](defaults-and-triggers.md).
