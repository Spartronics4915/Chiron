---
title: Mechanism Project - Build your own intake
---

You now have the pieces needed to write an intake subsystem. Let's put them
together and check what happens when you use it, including when a piece never
arrives or another command takes over.


```{include} ../../snippets/terminal-reminder.md
```

## Required behavior

Your assignment must have one Intake subsystem with an explicit public interface,
Acquire and Release commands with requirements and cleanup, a teleop default,
and input bindings created once. The same intake rules must serve manual and
autonomous requests. Keep the supplied simulator; don't spend this project writing
physics or wiring real hardware.

Run the maintained solution only as a comparison:
`python tools/run_robot.py examples/mechanism/solution`. It is not evidence that
your own assignment meets the requirements.

## Check the important paths

Restart between scenarios when you need a known state. Record expected behavior
before running and actual behavior afterward:

| Scenario | Required observation |
|---|---|
| Acquire with available piece | Detects a piece, stops, reports success |
| Acquire with no available piece | Times out, stops, reports no success |
| Release a held piece | Negative output, detector clears, output stops |
| Schedule Release during Acquire | Acquire is interrupted; replacement owns intake |
| Disable during either action | Active command ends; output is zero |
| Re-enable with manual request zero | No stale active behavior restarts unexpectedly |
| Schedule Acquire again | Timer and success state start fresh |
| Default after command ends | Resumes only when free; live teleop request is used |

The repository's automated tests cover the maintained example. Run the scenarios
above using your own assignment, then add the local tests described below.
`python -m pytest -q` uses the repository's configured test folders, which exclude
unfinished assignments in `student-work`. You'll give pytest your assignment's
path explicitly to check your copy.

## Make one new feature

Implement a **gentle acquisition** command that uses 0.25 instead of 0.5, still
stops on detection, times out if no piece appears, and cleans up on interruption.
Decide whether to parameterize Acquire or add another command. Explain the tradeoff
and preserve existing callers. Bind the new action to a new dashboard boolean.
The supplied detector is deliberately idealized; don't claim this proves real
low-speed acquisition performance.

:::{hint} Separate variation from shared rules
:class: dropdown
The collection request differs, but possession and stop rules belong in the
subsystem. A parameter can avoid copying the entire command. If you add one,
choose a compatible default and test both behaviors.
:::

## Check your copy automatically

Copy `tests/test_mechanism.py` to `student-work/intake-subsystem/test_commands.py`,
keeping the subsystem checks you already wrote in `test_intake.py`.
Replace its two example imports with `from intake_subsystem import Intake` and
`from intake_commands import Acquire, Release, ManualIntake`. Keep the shared
simulator import. From the repository root run
`python -m pytest student-work/intake-subsystem -q`.
Pytest is a test runner: functions whose names start with `test_` describe checks.
The **fixture**, named `rig`, gives each test a fresh simulator, intake, and
`tick` function. Each tick advances simulated time by 0.02 seconds and runs one
scheduler update.

Start with `test_acquire_success_and_stop`. It creates and schedules Acquire,
then calls `tick(30)` to advance 0.6 simulated seconds. Its assertions check
that acquisition succeeded, the command ended, a piece was detected, and the
output stopped. Read `test_timeout_is_not_success` next: it removes the available
piece and expects the attempt to end without success. Use those two cases to
write checks for your gentle-acquisition command, including its 0.25 output
while collecting and zero output after interruption.

## Explain and review

Draw your program's structure with the names from your
own files. Trace one acquisition request and its detector reading through it.
Explain which decisions choose the action and which rules protect the mechanism
for every caller. Identify what you would change for a different detector and
what should stay the same.

Then use the [feedback lesson](feedback-control.md) to explain why this intake
doesn't regulate roller speed, and what measurement that would require. For a
future arm, distinguish target angle, measured angle, and motor effort. You do
not need to build or tune that arm to complete this intake project.

In your assignment README, include environment, launch command, controls, expected
behavior, known limitations, and how to run your tests. You can use
[a pull request within your fork](../setup/saving-your-work.md#code-review)
to read through the changes together and record your own review notes.

Trace a button press through the trigger, scheduler, command, subsystem, output,
and sensor. Explain how interruption differs from timeout. Then temporarily
remove Acquire's `addRequirements` call in your assignment. Run the conflicting
requirement test and explain why it fails. Restore the call and rerun the tests.

Finally, give gentle acquisition a one-second timeout while keeping ordinary
Acquire at two seconds. With no piece available, check that each attempt lasts
its intended duration and stops without claiming success. This should change
the command configuration while leaving the shared intake rules alone.

Once those checks pass and you can explain their results, you've completed this
project. Keep your README and tests with the code so you can return to it later.
The examples use simulation; physical device setup will have its own guides.
