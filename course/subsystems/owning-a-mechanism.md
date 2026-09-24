---
title: A subsystem owns a mechanism
---

A **subsystem** is the part of a command-based robot program responsible for a
mechanism and its shared resources. Our Intake subsystem is the single place that
writes the intake's output and knows how to read its piece detector.
Keep the [program structure diagram](robot-code-structure.md) nearby as you
connect these responsibilities to Python methods.


```{include} ../../snippets/terminal-reminder.md
```

## Separate decisions from requests

The operator might request collection, autonomous might request collection, and
a release action might request reverse. They should all use the same intake rules.
Put those rules behind methods such as `set_output`, `has_piece`, and `stop`.
Callers ask for an action instead of reaching through and changing `io.output`.

The subsystem is not the whole robot and it is not a task with a finish condition.
It persists for the life of the program. A command, introduced next, describes
one behavior using that subsystem.

## Build on the framework

```{literalinclude} ../../examples/mechanism/solution/intake_subsystem.py
:language: python
```

`commands2.Subsystem` is the base class supplied by RobotPy's command framework.
We inherit its framework behavior while adding our mechanism methods.
`super().__init__()` runs the base class initializer so the framework can register
the subsystem. It belongs before our own setup; don't omit it because the code
seems to work on one run.

The `io` parameter is an object given to us by the robot. `self.io = io` stores
that same object; it does not make a new simulator. This is composition again:
the subsystem has an input/output adapter. Tests can supply the same small simulator
without constructing a whole application.

`has_piece()` returns a boolean to the caller. `set_output` blocks forward
collection when detected, while reverse remains available. The adapter already
handles normalized limits and disabled outputs. `stop()` requests zero. Each layer
has a stated responsibility; callers don't need to duplicate all of those rules.

## Refactor

Copy your known periodic starting point with
`python tools/start_exercise.py intake-subsystem`. In `student-work/intake-subsystem`,
create `intake_subsystem.py` and implement the subsystem. Keep your earlier
periodic assignment intact for comparison. Use `import commands2` and the supplied
`IntakeSim`; you do not need vendor libraries for this exercise.

Create `test_intake.py` beside it. **Pytest** is the check runner installed with
the course: it calls functions whose names begin with `test_` and reports failed
assertions. Start with this check:

```{literalinclude} ../../examples/mechanism/solution/test_intake_contract.py
:language: python
```

Run `python -m pytest student-work/intake-subsystem/test_intake.py -q` from the
Chiron root. The project's test configuration makes shared helpers importable.
Add checks for detected forward, reverse, stop, and independent instances. These
calls test the subsystem's contract before involving scheduling. The final project
adds a fresh scheduler and simulated time for command checks.

:::{hint} Test the observation
:class: dropdown
After calling `intake.set_output(0.5)`, inspect `io.output`. Set `io.detected = True`
and repeat. Don't write a second copy of the rule in your check and compare two
copies of the same mistake.
:::

Explain why other behaviors should use the subsystem instead of writing directly
to the adapter. Then move on to [commands](command-lifecycle.md).
