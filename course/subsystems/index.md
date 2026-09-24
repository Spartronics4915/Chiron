---
title: Stage 1B - A mechanism subsystem
---

Your periodic intake works, but adding more buttons and autonomous actions can
make it harder to follow. It becomes easy for two parts of a program
to write different outputs in the same loop. Command-based code gives those
behaviors a consistent lifecycle and a way to claim ownership.

We will refactor the intake you already understand. The mechanism and sensor
rules stay familiar while the organization changes.
First, map the responsibilities and trace a request through the program. After
building the command-based intake, we'll use an arm as a thought experiment to
explain feedback and PID before the final project.

```{toc}
:context: children
```

By the end, you should be able to write an intake subsystem, give commands its
requirements, bind inputs once, and explain what happens when an action finishes
or is interrupted. You'll also add a new behavior from a written requirement.
