---
title: Organizing code into files
---

Your program is getting longer, so let's make it easier to find things. We'll
put the intake in one file and the program that uses it in another. A Python file
you import is called a **module**. The behavior stays the same; we're giving the
code a clearer place to live.

## Splitting a program into modules

Create `intake.py` in your assignment folder and move your Intake class there.
In a new `robot_model.py`, write `from intake import Intake`. This means “from
the module named intake, make the name Intake available here.” The import uses
the module name without `.py`. The spelling and capitalization must match.

An import also executes top-level statements in that module on its first import,
so don't leave a surprise demonstration running underneath your reusable class.
Keep the class in `intake.py` and the demonstration in `robot_model.py`.

**Composition** means building an object out of other objects. A robot *has an*
intake, so a Robot class can hold an Intake instance. The robot decides when to
request an action; the intake owns the details of its own behavior. This is the
same relationship we'll use with a subsystem later.

## Read it before running it

```{include} ../../snippets/terminal-reminder.md
```

Put this worked example in `student-work/foundations/modules_and_composition.py`.
Read it once and write down what you think it prints. Then save and run
`python student-work/foundations/modules_and_composition.py` using your environment's Python.

```{literalinclude} ../../examples/foundations/worked/modules_and_composition.py
:language: python
```

Read `robot.intake.stop()` from left to right: find the robot object, get its
intake attribute, call that intake's stop method. It prints zero. When you split
this example into files, the relationship doesn't change; the import simply
makes the class definition available where you need it.

Run your file from the repository root with
`python student-work/foundations/robot_model.py`. Python can find a sibling
`intake.py` beside the script. Don't name your file `math.py`, `wpilib.py`, or
`commands2.py`: it can hide a library with the same name.

## Try it yourself

:::{exercise} Build a two-file robot model
:label: exercise-modules-and-composition
Split your complete Intake class and Robot class into `intake.py` and `robot_model.py`. Have the robot collect, detect, and release a piece using the contained intake. Put assertions beside the demonstration for now.
:::

:::{hint} A place to start
:class: dropdown
Move the existing Intake implementation; do not rewrite a second copy.
:::

:::{hint} A more specific hint
:class: dropdown
Import Intake at the top of robot_model.py, construct it once in Robot.__init__, and call its methods through self.intake or robot.intake.
:::

::::{solution} exercise-modules-and-composition
:class: dropdown
The next project has a complete two-file solution for comparison. Your two files should reproduce the same decisions as the previous single-file version.
::::

## Before moving on

Explain what happens during import and which object owns output. Show that changing the intake logic in one file changes the demonstration using it.

