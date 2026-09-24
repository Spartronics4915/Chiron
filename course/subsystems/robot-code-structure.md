---
title: How the pieces of a robot program fit together
---

Your periodic intake already works. Before moving methods into new classes,
let's decide what each part of the program should be responsible for. Otherwise
we can end up with more files and exactly the same confusion.

This lesson builds on the working periodic intake. Your goal is to explain where
a behavior belongs and trace one request through the whole program. You don't
need to know the command API yet; the following lessons implement this design.

## Start with a conflict

Suppose manual control writes forward output, then an autonomous helper writes
reverse output during the same update. The motor cannot do both. Whichever write
happens last wins, which makes behavior depend on code order.

Moving those writes into different files does not solve the conflict. We need
one owner of the mechanism's output and a rule for deciding which behavior may
use it. This is the purpose of the subsystem and scheduler arrangement.

## Give each part a job

| Part | Question it answers | In our course robot |
|---|---|---|
| Robot setup | Which objects exist, and how are they connected? | Construct one intake; connect controls to actions |
| Trigger | Has an input condition changed? | A dashboard Acquire button becomes true |
| Scheduler | Which actions may run and when do they end? | Coordinate commands using declared requirements |
| Command | What behavior are we trying to perform now? | Acquire with detection, a deadline, and cleanup |
| Subsystem | What can this mechanism do, and what rules always apply? | Read possession; block forward collection when full |
| Input/output adapter | How do requests and readings reach the mechanism? | Our supplied `IntakeSim` model |

A command **requires** the subsystem it uses. The scheduler coordinates those
requirements so conflicting scheduled commands do not both own it. It cannot
protect against code that bypasses the subsystem and writes outputs directly.
See [WPILib's subsystem explanation](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html).

```{mermaid}
flowchart TD
  Button[Operator input] --> Trigger[Trigger notices a change]
  Trigger --> Scheduler[Scheduler coordinates ownership]
  Auto[Autonomous entry] --> Scheduler
  Scheduler --> Command[Acquire or Release command]
  Command --> Intake[One shared Intake subsystem]
  Intake --> IO[Input/output adapter]
  IO --> Mechanism[Simulated mechanism]
  Mechanism --> Reading[Detector reading]
  Reading --> Intake
  Intake -->|has_piece result| Command
```

Requests travel toward the mechanism; observations return to the behavior.
The scheduler coordinates software tasks, while the detector reports the
mechanism's condition. Scheduling Acquire does not itself mean a piece arrived.

## The same mechanism must mean the same object

Acquire, Release, and manual control receive references to the **same Intake
instance**. Think back to the object-state lesson: several names can refer to
one object. Here that is intentional.

Creating a separate Intake for every command tells the scheduler they are
different resources. If those objects refer to the same physical motor, the
software's ownership model no longer matches the robot. Construct persistent
mechanisms once, then give their references to the behaviors that need them.

An **interface** is the set of operations callers are meant to use. Our intake
offers `set_output`, `has_piece`, and `stop`. Keeping device details behind that
interface is **encapsulation**. If a detector changes, callers should still be
able to ask `has_piece()` without learning how the new device communicates.

## Files and responsibilities

This is the small layout you will build; these are files, not a call sequence:

```text
student-work/intake-subsystem/
    robot.py
    intake_subsystem.py
    intake_commands.py
    test_intake.py
    test_commands.py
```

`robot.py` connects the objects. The subsystem file holds shared mechanism
rules; the commands file holds Acquire, Release, and manual behavior. The two
test files check mechanism rules and command behavior respectively. Use those
responsibilities to decide where to look when a check fails.

Larger projects often move construction and bindings into a `RobotContainer`
and group mechanisms and commands into folders. The purpose is to keep related
decisions easy to find. Our small example keeps construction in `robotInit`;
adding a container is useful when that setup becomes difficult to navigate.
[WPILib's project-structure guide](https://docs.wpilib.org/en/stable/docs/software/commandbased/structuring-command-based-project.html)
shows the larger pattern. Its templates need not match our Python filenames.

## Follow one attempt through time

At startup, create the intake and its commands. On a button press, request that
the scheduler start Acquire. While it runs, repeatedly request collection and
check detection and elapsed time. When it ends, stop its output. A later attempt
uses the same mechanism but resets the command's timer and result.

These jobs happen at different times. Creating objects is setup; updating an
active behavior is repeated work. This is why moving initialization into a
periodic method loses state, and why a long waiting loop prevents other robot
work from progressing. The next lesson gives the mechanism its interface;
the command lesson gives each phase a method name.

## Place a new requirement

For each requirement, name the responsible part and explain why:

1. Change which button requests release.
2. Apply the “don't collect while full” rule in teleop and autonomous.
3. Give Acquire a shorter deadline without changing Release.
4. Replace the simulator with a device adapter that reports the same readings.

::::{dropdown} Compare after making your choices
1. Change the input binding in robot setup.
2. Change the shared subsystem rule, so all callers receive it.
3. Change Acquire's behavior or configuration.
4. Change the adapter and how setup supplies it. Preserve the subsystem's
   meaning and tests; matching method names alone does not prove equivalent behavior.
::::

Now draw two commands pointing to one intake. Explain why two separate Intake
objects would be wrong for the same motor. Keep that drawing beside your code
while you [build the subsystem](owning-a-mechanism.md).
