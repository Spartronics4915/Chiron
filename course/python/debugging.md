---
title: Debugging Code
---

At some point you'll run a program and get an error instead of the result you
expected. That happens to all of us, including experienced programmers. You don't
need to understand the entire error message at once. Let's practice finding the
part that tells us where to look.

## Reading an error message

A **syntax error** means Python cannot understand the written structure, such
as a missing closing quote. A **runtime error** occurs while executing understood
instructions, such as using a name that has not been assigned. A **logic error**
means the program runs but does the wrong thing.

For an exception, start with the last line: it gives the error's name and message.
Then find the filename and line number pointing into your code. A **traceback**
shows the calls that led there; it is not necessarily asking you to edit a library.
For syntax errors, also check the preceding line for an unclosed bracket or quote.

Use a repeatable process: reproduce the problem, state what you expected, inspect
the relevant values, make one change, then rerun. Keep the smallest example that
still shows the problem. Save the code, full error, and expected output together
so you can check whether each change addressed the original problem.

## Read it before running it

```{include} ../../snippets/terminal-reminder.md
```

Put this worked example in `student-work/foundations/debugging.py`.
Read it once and write down what you think it prints. Then save and run
`python student-work/foundations/debugging.py` using your environment's Python.

```{literalinclude} ../../examples/foundations/worked/debugging.py
:language: python
```

First confirm this prints `Requested: 0.4`. Then change only the final name
to `request_speed` and run again. You should get a `NameError`, because that name
hasn't been assigned. Read the message and repair the spelling.

Next temporarily remove a closing parenthesis. This time Python cannot parse the
file. Restore it. Finally change the number to `4`: the program runs, but if you
intended forty percent output, the value is wrong. Python cannot know your intent.

## Try it yourself

:::{exercise} Make and repair a mistake
:label: exercise-debugging
Create and repair one name error and one syntax error in this small program. Write comments describing the symptom, the cause, and your repair. Then make a logic error that still runs and explain how you noticed it.
:::

:::{hint} A place to start
:class: dropdown
Keep a working version first. Introduce only one mistake at a time.
:::

:::{hint} A more specific hint
:class: dropdown
A misspelled variable creates a different name. A missing quote changes syntax. An unintended number changes behavior without necessarily raising an exception.
:::

::::{solution} exercise-debugging
:class: dropdown
There is no single required broken file. Your finished file must run, and your explanation must distinguish what Python detected from what you detected by checking expected behavior.
::::

## Before moving on

Pick one error you encountered and find the line it refers to. Write down what
caused it, make that mistake again, and repair it in place. The error message
should now give you enough information to find the problem.

