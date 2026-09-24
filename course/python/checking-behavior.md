---
title: Checking behavior with assertions
---

So far you've run a program and compared its output with what you expected.
Let's have Python help with that comparison. A **check** describes an expected
result and tells you when the program doesn't match it. That makes it easier to
try a new idea without losing track of what already worked.

## Checking an expected result

`assert condition` continues if the condition is true and raises `AssertionError`
if it is false. Use it to describe expected behavior in exercises and tests.
For example, `assert result == 0.0` means that this particular result must be zero.
Keep the motor's disabled rule in the ordinary `if` statements that choose its
output. An assertion checks that the rule works; it doesn't replace the rule.

:::{note} Why keep those separate?
:class: dropdown
Python can be started with assertions turned off. They're useful while developing
and testing, but the program must still make safe decisions without them.
:::

Choose cases before writing the solution: a normal request, the boundary, and a
case that must be rejected. Our model accepts motor requests from -1 to 1.
Values above 1 should be limited to 1; values below -1 should become -1. This is
called **clamping**. We'll write it with conditionals you already understand.

## Read it before running it

```{include} ../../snippets/terminal-reminder.md
```

Put this worked example in `student-work/foundations/checking_behavior.py`.
Read it once and write down what you think it prints. Then save and run
`python student-work/foundations/checking_behavior.py` using your environment's Python.

```{literalinclude} ../../examples/foundations/worked/checking_behavior.py
:language: python
```

If all assertions hold, you see the final message. Change the first comparison
to `request < 1.0` and rerun. Which claim catches the mistake? Read its source line,
explain the failure, then repair it. A passing check only covers what you actually
checked; one successful request does not prove every input is correct.

## Try it yourself

:::{exercise} Check the intake rules
:label: exercise-checking-behavior
Add clamping to your intake function. Write assertions for forward/no piece, forward/held piece, reverse/held piece, disabled, and requests outside both bounds.
:::

:::{hint} A place to start
:class: dropdown
Keep the decision order visible: disable, block unwanted forward acquisition, then bound an allowed request.
:::

:::{hint} A more specific hint
:class: dropdown
Reuse `clamp_request` in `intake_output` instead of repeating its comparisons.
:::

::::{solution} exercise-checking-behavior
:class: dropdown
Check both high and low bounds. A held piece must not prevent reverse release, and disabling must override either direction.

```{literalinclude} ../../examples/foundations/solutions/checking_behavior.py
:language: python
```
::::

## Before moving on

Choose a value exactly at an output limit, then one just beyond it. Write down
the expected result for each before running. If either result surprises you,
trace the comparisons and note where your prediction went wrong.

Show a deliberate broken rule that your checks detect, then restore it. Explain one behavior your current checks do not cover.

