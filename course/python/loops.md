---
title: Repeating work with loops
---

What if you want to check several sensor readings? You could copy the same lines
over and over, but changing all those copies would get tedious. A **loop** repeats
a block for you. Let's follow a small one, one repetition at a time.

## Following each repetition

`for sample in range(4):` runs its block four times, assigning `sample` the
values 0, 1, 2, and 3. The stop value 4 is excluded. The loop variable changes
each time. A total you initialize before the loop can keep accumulating across
repetitions; initialize it inside and it starts over each time instead.

A `while` loop repeats as long as a boolean condition is true. For example,
`while count < 3:` requires something in its body to change `count` if it is to
finish. An accidental infinite loop can be stopped with Ctrl+C in the terminal.
We'll mostly use bounded for loops for our early exercises.

Indentation matters here too. An indented print shows every repetition; an
unindented print after the loop shows only the final state. Trace the values at
the end of each repetition rather than trying to guess the whole loop at once.

## Read it before running it

```{include} ../../snippets/terminal-reminder.md
```

Put this worked example in `student-work/foundations/loops.py`.
Read it once and write down what you think it prints. Then save and run
`python student-work/foundations/loops.py` using your environment's Python.

```{literalinclude} ../../examples/foundations/worked/loops.py
:language: python
```

The running totals are 0, 1, 3, and 6; the final line reports 6. Move the
initialization inside the loop temporarily and compare: each repetition starts
from zero, so you no longer accumulate a total. Restore it afterward.

Change `range(4)` to `range(1, 5)`. This form starts at 1 and stops before 5.
Predict the new total. Later a robot framework will call our code repeatedly;
we won't put a never-ending loop inside a callback that must return.

## Try it yourself

:::{exercise} Add a total and count down
:label: exercise-loops
Use a loop to add the numbers 1 through 5. Print each running total and the final total. Then write a while loop that prints a countdown 3, 2, 1 and finishes.
:::

:::{hint} A place to start
:class: dropdown
Initialize an accumulator once before the for loop. For the countdown, identify which value moves toward the stopping condition.
:::

:::{hint} A more specific hint
:class: dropdown
Use `range(1, 6)` for the sum. In the while body, subtract 1 from the countdown after printing it.
:::

::::{solution} exercise-loops
:class: dropdown
The final sum is 15. The countdown ends when its condition becomes false at zero; it does not need to print zero.

```{literalinclude} ../../examples/foundations/solutions/loops.py
:language: python
```
::::

## Before moving on

Predict the effect of moving a print one indentation level left. Recall how a NameError differs from a loop that produces the wrong total.

