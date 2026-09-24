---
title: Calculations and comparisons
---

Now that we can store values, let's do something with them. If the robot travels
three metres in two seconds, how fast is it moving? Python can calculate that for
us. The symbols used for calculations and comparisons are called **operators**.

## Calculations, comparisons, and units

For numbers, `+`, `-`, `*`, and `/` mean addition, subtraction, multiplication,
and division. `**` raises to a power. `//` performs floor division and `%` gives
the remainder. For example, `7 // 3` is 2 and `7 % 3` is 1. Use parentheses to
make grouping clear: `2 + 3 * 4` is 14, while `(2 + 3) * 4` is 20.

Comparisons return a boolean. `==` means equal, `!=` not equal, `<` less than,
`>` greater than, and `<=`/`>=` include equality. Remember that `=` assigns;
`==` asks a question. Combine boolean questions with `and`, `or`, and `not`:
`and` needs both conditions, `or` needs at least one, and `not` reverses a boolean.

Units are part of the meaning even when Python doesn't enforce them. Dividing
metres by seconds gives metres per second. Use names or comments that make units
clear; dividing centimetres by seconds would produce a different numeric scale.

## Read it before running it

```{include} ../../snippets/terminal-reminder.md
```

Put this worked example in `student-work/foundations/operators.py`.
Read it once and write down what you think it prints. Then save and run
`python student-work/foundations/operators.py` using your environment's Python.

```{literalinclude} ../../examples/foundations/worked/operators.py
:language: python
```

This prints speed 1.5 and allowed `True`. Change the distance to 6 metres:
the speed becomes 3.0 and the combined question becomes false. Then make
`enabled` false and use a small distance. Why does the result remain false?

Try to calculate speed with zero elapsed time and you'll get `ZeroDivisionError`.
There isn't a meaningful speed calculation from those inputs, so read that error
as a clue to check your measurements.

One detail we'll return to later: computers store many decimal numbers approximately.
When checking real measurements, we'll allow a small range around the target
instead of expecting every decimal to match exactly. You don't need that extra
machinery for this exercise.

## Try it yourself

:::{exercise} Check a speed limit
:label: exercise-operators
Calculate speed for 4 metres over 2 seconds. Decide whether it is at or below a 2 m/s limit, then repeat for 5 metres. Print the speed and comparison for each case.
:::

:::{hint} A place to start
:class: dropdown
Separate “calculate the speed” from “compare with the limit”.
:::

:::{hint} A more specific hint
:class: dropdown
Use `<=`, not `<`, if a speed exactly at the limit is allowed.
:::

::::{solution} exercise-operators
:class: dropdown
The first speed is 2.0 and passes; the second is 2.5 and fails. This boundary case distinguishes the two comparisons.

```{literalinclude} ../../examples/foundations/solutions/operators.py
:language: python
```
::::

## Before moving on

Explain the difference between `=` and `==` without looking. Predict the result for exactly 0 metres in 2 seconds, then check it.

