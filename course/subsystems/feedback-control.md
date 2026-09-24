---
title: How feedback chooses motor effort
---

Our intake needs a simple decision: collect until a detector changes. An arm
needs something more: move toward an angle, slow down, and stay near it. Both
use feedback, but a boolean possession rule cannot tell us how strongly to drive
an arm motor.

Before the final project, let's connect the [control overview](../robot/control-and-feedback.md)
to that more general problem. This is a paper-and-pencil lesson. You should leave
able to explain a feedback loop and reason about its measurements, without having
to implement a tuned arm controller yet.

## Choose a quantity you can measure

**Position** tells us where something is, such as an arm angle in degrees.
**Velocity** tells us how quickly position changes, such as degrees per second.
Holding an angle and maintaining a speed are different goals.

Suppose an arm is at 20 degrees and we want 50 degrees. The desired value is the
setpoint; their difference is the **error**:

$$
e = r - y
$$

Here $r$ is the requested angle and $y$ is the measured angle. In this example,
50° minus 20° gives an error of 30°. Positive error
means we need to move in the direction of increasing angle. Before using this
rule, agree on where zero is, which direction is positive, and which units the
sensor provides. Subtracting degrees from encoder rotations gives a meaningless
answer even if Python accepts both numbers.

```{mermaid}
flowchart TD
  Target[Target angle] --> Error[Subtract measured angle]
  Error --> Rule[Controller chooses effort]
  Rule --> Limit[Limit the allowed output]
  Limit --> Arm[Motor and arm move]
  Load[Gravity and changing load] --> Arm
  Arm --> Sensor[Sensor measures angle]
  Sensor --> Error
```

The controller repeats this calculation using a new measurement each update.
The arrow back from the sensor closes the loop. The mechanism still takes time
to move; calling a calculation does not instantly place it at the target.

## Proportional control: respond to the current error

A proportional controller chooses effort by multiplying error by a gain:

$$
u = k_P e
$$

For this thought experiment, $u$ is voltage and $k_P$ is 0.1 volts per degree.
These are invented arithmetic examples, not settings for a real arm.

| Target | Measured angle | Error | Requested voltage |
|---|---|---|---|
| 50° | 20° | 30° | 3 V |
| 50° | 40° | 10° | 1 V |
| 50° | 50° | 0° | 0 V |
| 50° | 55° | -5° | -0.5 V |

As error shrinks, the correction shrinks. If we pass the target, the sign
reverses. Increasing the gain gives a stronger correction for the same error,
but does not guarantee a better response. Motion has momentum, measurements
arrive at intervals, and output is limited.

For example, if the allowed output were -4 to 4 V and the calculation requested
7 V, only 4 V could be applied. This is **saturation**. A controller cannot
produce effort beyond the mechanism's permitted range.

## The I and D terms

PID combines proportional, integral, and derivative contributions. You can
understand their purposes before learning the full equation:

| Term | Information it uses | What it can help with |
|---|---|---|
| P | Error now | Move toward the target |
| I | Error accumulated over time | Correct a persistent offset |
| D | How quickly error changes | Reduce overshoot by damping motion toward a fixed target |

Integral can keep accumulating while output is saturated, leading to excessive
correction later; this is **windup**. Derivative reacts to changes, including
measurement noise. Adding all three terms is not automatically an improvement.
WPILib recommends feedforward rather than integral for many FRC applications.
Its [PID introduction](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/introduction/introduction-to-pid.html)
includes equations and response plots when you're ready for more detail.

## Anticipate a load, then correct what remains

At the target, our proportional calculation asks for zero volts. A real arm may
still need effort to oppose gravity. **Feedforward** estimates the effort needed
from a model of the mechanism; feedback corrects the remaining error. They can
be added together before applying limits. An arm's gravity term depends on its
angle; it is not one universal number to copy between mechanisms.
[WPILib's feedforward introduction](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/introduction/introduction-to-feedforward.html)
explains how gravity, friction, and motion enter those estimates.

## Read a response before changing a gain

Imagine recording these angles at equal time intervals after changing the target
to 50 degrees. These are illustrative readings, not simulated or measured results:

| Trace | Readings in degrees | What to investigate |
|---|---|---|
| A | 20, 35, 46, 50, 50 | Approaches and stays near the target at these sample times |
| B | 20, 45, 62, 43, 56 | Overshoots and crosses the target repeatedly |
| C | 20, 33, 40, 43, 43 | Settles short; inspect load, allowed output, and control effort |
| D | 20, 15, 7, -4, -18 | Moves away; check sensor and output signs before tuning |

**Overshoot** means going beyond the target. **Settling** means staying within
an agreed band around it. A few samples suggest behavior but don't prove what
happened between them. Log the target, measurement, and applied effort together
so you can relate cause to effect. A timeout alone cannot establish that a target
was reached, and crossing it once cannot establish that the mechanism settled.

## Where does this belong in robot code?

For a future arm, a command could request an angle while the subsystem repeatedly
updates a position controller. The command decides when to finish; the subsystem
owns measurement conversion, limits, and the agreed holding behavior. Decide
explicitly what happens after interruption and disabling. Holding position may
require continuing control while enabled; “command finished” and “motor off”
are not always the same requirement.

Some device controllers run a feedback loop themselves. In that arrangement the
subsystem sends a setpoint and reads status instead of independently issuing a
second competing effort command. The ownership principle stays the same.

Our course intake needs neither an angle setpoint nor PID. Its possession rule
already fits its goal. Learning control means choosing a suitable method and
measurement, not adding PID to every motor.

## Check your reasoning

1. With a 50° target and a 30° measurement, calculate the requested voltage using
   the example gain. What changes if you double the gain?
2. Which trace would make you check direction conventions before any gain changes?
3. Why can zero position error still require a nonzero holding effort?
4. What would you need to measure to regulate intake roller speed?

::::{dropdown} Compare after writing your answers
1. Error is 20°, so the request is 2 V. Doubling the gain requests 4 V; it does
   not prove the arm will arrive twice as fast.
2. Trace D. A correction intended to reduce error appears to increase it.
3. Gravity or another load may still act at the target. A model can estimate
   holding effort, with feedback correcting differences.
4. Roller speed, directly or derived from suitable position measurements over
   time. A game-piece detector cannot provide that information.
::::

[Next: demonstrate and extend your mechanism subsystem](mechanism-project.md).
