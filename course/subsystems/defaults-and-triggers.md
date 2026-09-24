---
title: Default Commands and Triggers
---

We have a mechanism and behaviors. Now connect them to the robot without
creating new commands or bindings on every periodic call.

## Let the framework run the scheduler

Change your robot base class to `commands2.TimedCommandRobot`. This framework
class runs the command scheduler for you. Do not add a second scheduler call.
Construct one Intake in `robotInit`, then give that same object to Acquire,
Release, and the manual behavior. Keep the supplied `simulationPeriodic` support.

## A supplier gives the latest value

`ManualIntake` receives `read_request`, a function it can call later. Passing
`self.read_request` without parentheses passes the callable. Passing
`self.read_request()` would call it immediately and pass a number instead.
This callable is often called a **supplier** because it supplies a current value.

During every `execute`, ManualIntake calls the supplier and sends its result to
the subsystem. Its `end` stops the output. It has no custom `isFinished`; the base
command's default doesn't finish on its own.

Assign it with `intake.setDefaultCommand(...)`. A **default command** runs when
that subsystem is free. It is interrupted when another command needs the intake,
and can resume afterward. Our supplier returns zero outside enabled teleop so
an autonomous timeout cannot resume an old operator request.

## Trigger on a changing condition

`Trigger` watches a boolean supplier. `onTrue(command)` schedules when the condition
changes from false to true. It does not schedule repeatedly just because a button
stays true. In our dashboard demonstration, set Acquire false before setting it
true again to create another press.

Construct and bind triggers once in `robotInit`. A physical controller button
can provide an equivalent boolean later. For now the dashboard keeps hardware
setup separate from learning scheduling.

```{literalinclude} ../../examples/mechanism/solution/robot.py
:language: python
```

## Connect your version

```{include} ../../snippets/terminal-reminder.md
```

Implement ManualIntake and the robot setup in your assignment. Use imports from
your own sibling `intake_subsystem.py` and `intake_commands.py`, as the example does.
The launcher puts the selected assignment on the import path. Run:

```sh
python tools/run_robot.py student-work/intake-subsystem
```

Use zero manual request first. In enabled teleop, set Acquire true; the output
should collect then stop. After detecting a piece, set Release true; it should
reverse and stop after release. Reset each dashboard button to false before its
next use. Watch `Acquire succeeded` to distinguish sensor success from timeout.

Now hold a nonzero manual request and observe what happens after a command releases
the intake. The default can resume the request; that is expected ownership behavior,
not a reason to remove cleanup. Return all requests to zero before the next test.

Explain why `self.read_request` has no parentheses where it is passed to the
command, and why trigger bindings belong in initialization. Next, explore
[how feedback chooses motor effort](feedback-control.md) before the final project.
