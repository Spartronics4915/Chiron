---
title: Goals, Outputs, and Feedback
---

Imagine telling a teammate to collect a game piece. They understand the goal,
watch the intake, and stop when the piece arrives. A motor understands none of
that. It receives an electrical input and turns. Our program has to connect
the goal to that physical result.

You already wrote the intake's decision rules in the Stage 0 project. Before
putting them inside RobotPy, let's explain what those rules are controlling.
By the end, you should be able to draw the path from a request to a result and
explain what information tells you whether the action worked.

## Two different questions

**High-level control** chooses what should happen: collect a piece, hold it,
or release it. It also decides when an action is complete and what to do if it
fails. **Low-level control** turns that request into outputs for a mechanism,
using measurements and limits where needed. These are responsibilities, not
particular Python keywords or mandatory filenames.

For our intake, a high-level decision is “collect until detected, but give up
after a timeout.” A lower-level rule is “block positive output while a piece
is detected, but still allow reverse.” A future arm has a different lower-level
problem: choose motor effort repeatedly so its measured angle approaches a target.

```{mermaid}
flowchart TD
  Goal[Goal: collect a piece] --> Action[Choose action and completion rule]
  Action --> Request[Request forward intake output]
  Request --> Rules[Apply mechanism rules and limits]
  Rules --> Motor[Motor moves the rollers]
  Motor --> Piece[Piece moves into intake]
  Piece --> Sensor[Detector reports a piece]
  Sensor --> Rules
  Sensor --> Action
```

Read the arrows as information or effects, not as a list of Python calls.
The action requests motion; the detector reports what happened. Detection can
both stop a behavior and enforce a shared mechanism rule.

## Translating the Output

Our model accepts an output between -1 and 1. The sign selects a direction;
the magnitude requests more or less effort. A request of 0.5 does **not** mean
the rollers will spin at a measured speed of 0.5, or that a real mechanism will
reach half its maximum speed. Load, battery voltage, friction, and the device's
control mode affect motion.

Separate three things when debugging:

| Thing | Intake example | What it tells you |
|---|---|---|
| Request | Collect at 0.5 | What the caller wants |
| Applied output | Zero because a piece is already detected | What was allowed |
| Measurement | Detector is true | What the sensor reports |

If request and output differ, first inspect the rules between them. If the
output looks right but the result does not, investigate the model, mechanism,
or measurement. Changing the request blindly hides which part is wrong.

## Open loop and Closed loop

An **open-loop** action chooses an output without using a measurement of the
controlled result to correct it. Running the rollers for one second is open loop
with respect to acquiring a piece: the same time passes even when no piece arrives.

A **closed-loop** action uses feedback from the result. Stopping when the detector
reports a piece uses feedback about possession. That still does not regulate
roller speed; we have no speed measurement in this model. Always name the
quantity you mean when calling something closed loop.

In control terminology, the **plant** is the physical mechanism and the
**controller** is the rule choosing its input. A **setpoint** is a desired measured
value, such as an arm angle. Feedback compares what happened with what we wanted.
See [WPILib's control-system introduction](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/introduction/control-system-basics.html)
for these terms and a more formal block diagram.

## State, Completion, and Failure

An action has **state**: information about where it is in its progress. These
states belong to an acquisition attempt; they are different from the robot's
teleop, autonomous, and disabled modes.

```{mermaid}
stateDiagram-v2
  [*] --> Idle
  Idle --> Collecting:  acquire requested 
  Collecting --> Acquired: detector reports piece
  Collecting --> TimedOut: no detection before deadline
  Collecting --> Cancelled: interrupted or disabled
  Acquired --> [*]
  TimedOut --> [*]
  Cancelled --> [*]
```

Every exit from collecting must clean up its output. Only detection provides
evidence of acquisition. A timeout means the attempt has ended, not that it
succeeded. A new attempt starts fresh; last time's success flag cannot answer
whether this attempt worked.

Feedback is only as trustworthy as its measurement. A detector stuck false can
cause a timeout; one stuck true can produce a false success. Our simulator gives
ideal readings, so these are reasoning exercises rather than claims that it
models real sensor faults.

## Predict Before Programming

Write your answers before opening the explanation:

1. A timer finishes with no piece detected. What can the robot honestly report?
2. The rollers slow under load. Can our detector tell us how much they slowed?
3. An arm reaches its target angle but is still moving quickly. Is “at the target
   once” a good completion rule?

:::{hint} Start with the information available
:class: dropdown
List what each sensor measures. Then separate an action ending from its goal
being achieved. For the arm, think about what will happen just after the reading.
:::

::::{dropdown} Compare your reasoning
1. The attempt timed out without evidence of success. Stop and report that outcome.
2. No. Possession and speed are different quantities; speed control needs a
   suitable measurement.
3. It may immediately pass the target. Position tolerance and sufficiently low
   speed make a stronger completion rule than crossing one angle.
::::

Draw the request/output/measurement path for a different mechanism and explain
each arrow in your notes. You can plan this part before writing any Python.
