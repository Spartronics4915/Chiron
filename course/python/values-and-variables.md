---
title: Values and Variables
---

Your greeting worked, but you had to edit the text to change what it said.
What if a program needs to remember a speed, a sensor reading, or a count? That's
where variables come in. We'll start with a few numbers and watch what changes.

## Naming and updating values

A **variable** is a name referring to a value. In `pieces = 2`, the `=` means
assignment: evaluate the right side, then associate that result with the name on
the left. This is different from an equation saying two expressions are equal.

Python values have **types**. An `int` is an integer such as `2`; a `float` is a
number such as `0.5`; a `str` is text such as `"intake"`; a `bool` is `True` or
`False`. Types affect what operations make sense. `"2"` is text, even though it
contains a digit. We will use booleans for decisions later.

Choose names that explain a value, such as `motor_request`, rather than `x` when
its meaning isn't obvious. Python names are case-sensitive: `pieces` and `Pieces`
are different names. Use lowercase words with underscores for our variables.
`print` can receive multiple values separated by commas and display them together.

## Read it before running it

```{include} ../../snippets/terminal-reminder.md
```

Put this worked example in `student-work/foundations/values_and_variables.py`.
Read it once and write down what you think it prints. Then save and run
`python student-work/foundations/values_and_variables.py` using your environment's Python.

```{literalinclude} ../../examples/foundations/worked/values_and_variables.py
:language: python
```

The output is `Current count: 3` and `Earlier count: 2`. Trace the assignments:

| After this line | pieces | saved_count |
|---|---:|---:|
| `pieces = 2` | 2 | not assigned |
| `saved_count = pieces` | 2 | 2 |
| `pieces = 3` | 3 | 2 |

`saved_count` receives the value at the time of assignment. It is not a formula
that keeps watching the other name. This distinction will matter when you store
a previous sensor reading. Change the first value to 5 and predict both outputs
before running.

## Try it yourself

:::{exercise} Describe an intake with variables
:label: exercise-values-and-variables
Store a robot name, an integer count, and a decimal speed request in three variables. Print each with a label. Save the old speed in another variable, change the current speed, and print both.
:::

:::{hint} A place to start
:class: dropdown
Use quotes for the name, but not for numeric values.
:::

:::{hint} A more specific hint
:class: dropdown
Assign `previous_speed = speed` before changing `speed`.
:::

::::{solution} exercise-values-and-variables
:class: dropdown
The old speed should keep its earlier numeric value. Compare the order of the assignments if both outputs show the new value.

```{literalinclude} ../../examples/foundations/solutions/values_and_variables.py
:language: python
```
::::

## Before moving on

Think about the type of each value and why a saved number does not automatically update. Recall the difference between saving this file and committing it.

