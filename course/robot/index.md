---
title: Stage 1A - Make a mechanism work
---

Your intake model already makes useful decisions. In this stage we'll place
those decisions inside a RobotPy program and use a simulated sensor and motor.
That gives us repeated updates and changing inputs without needing a real robot.
We start by separating a robot's goal, its output, and the measurement that tells
us what happened. Then we'll see how the framework repeats those decisions.

```{toc}
:context: children
```

Keep the mechanism simple while learning the framework. You should finish able to
run the intake manually, stop acquisition when a piece is detected, and make a
bounded autonomous action. Stage 1B will reorganize that same behavior into commands.
