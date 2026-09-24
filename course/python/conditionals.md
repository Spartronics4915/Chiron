---
title: Making decisions with conditionals
---

Imagine holding the collect button after a game piece is already in the intake.
We probably don't want the motor to keep pulling it in. How can our code handle
that? A **conditional** lets it ask a question and choose what to do with the answer.

## Choosing which instructions run

Start with `if condition:`. If the condition is true, Python runs the indented
lines beneath it. Otherwise it skips them. The colon introduces the block;
indentation shows where that block belongs. Use four spaces for each level.

Add `else:` for what should happen when the condition is false. An `else` doesn't
take a new condition. If there are more than two possibilities, `elif` means
“otherwise, if ...”. In a single `if`/`elif`/`else` chain, Python chooses the first
true branch, or the final else if none match. It does not run every branch.

Be a little careful with two separate `if` statements: Python considers both of
them. The second can change an output the first just chose. When you want exactly
one decision to win, keep those alternatives in one `if`/`elif`/`else` chain.

## Read it before running it

```{include} ../../snippets/terminal-reminder.md
```

Put this worked example in `student-work/foundations/conditionals.py`.
Read it once and write down what you think it prints. Then save and run
`python student-work/foundations/conditionals.py` using your environment's Python.

```{literalinclude} ../../examples/foundations/worked/conditionals.py
:language: python
```

Here the disabled question is false, the possession question is false, and
the final branch sets output to 0.6. The unindented print runs afterward regardless
of the branch selected. Try all four combinations of enabled and has_piece.
Write the selected branch next to each result.

Now set `request = -0.4` while holding a piece. This version blocks release too.
That is a missing requirement, not a Python error. We need to distinguish forward
acquisition from reverse release.

## Try it yourself

:::{exercise} Choose the intake output
:label: exercise-conditionals
Update the decision so positive intake stops when a piece is detected, but negative output can release it. Disabled output must still always be zero. Check positive, zero, and negative requests with both sensor states.
:::

:::{hint} A place to start
:class: dropdown
Decide which rule has highest priority before writing the branches.
:::

:::{hint} A more specific hint
:class: dropdown
The middle condition should ask both whether a piece is held and whether the request is positive.
:::

::::{solution} exercise-conditionals
:class: dropdown
The middle branch blocks only `has_piece and request > 0`. An early disabled branch prevents later requests from overriding the disabled result.

```{literalinclude} ../../examples/foundations/solutions/conditionals.py
:language: python
```
::::

## Before moving on

Without opening the solution, write down which branch handles an enabled intake
holding a piece with a request of -0.3. Then explain what changes when enabled
becomes False. Run both cases and compare the outputs with your predictions.

Explain why the disabled check is first. Show the exact boundary at request 0.0, and explain what would happen with two unrelated if statements that overwrite output.

