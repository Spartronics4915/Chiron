---
title: Your first Python program
---

You've already changed a greeting during setup. Now let's look at what made
that work. A **program** is a set of instructions. A Python source file stores
those instructions as text, and the Python interpreter carries them out.

## Text and instructions

`print("Hello, Spartronics!")` asks Python to display text in the terminal.
`print` is the name of a built-in **function**, a reusable action. The parentheses
contain the information we give it. Here that information is a **string**: text
surrounded by quotation marks. The quotation marks tell Python where the text
starts and ends; they are not part of the displayed greeting.

Python runs these statements from top to bottom. An empty line makes the file
easier for people to read. A line starting with `#` is a **comment** for people;
Python ignores the comment when running the file. Comments explain a purpose,
but changing a comment alone won't change what the program does.

## Read it before running it

```{include} ../../snippets/terminal-reminder.md
```

Put this worked example in `student-work/foundations/first_program.py`.
Read it once and write down what you think it prints. Then save and run
`python student-work/foundations/first_program.py` using your environment's Python.

```{literalinclude} ../../examples/foundations/worked/first_program.py
:language: python
```

You should see two separate lines, in the same order as the statements. Swap
the two `print` lines, save, and run again. Did the order change as you expected?
Now change only the comment and run once more. That change should not affect output.

Keep code and terminal commands separate: `python ...` is the command that starts
the interpreter; it does not belong inside the file being interpreted.

## Try it yourself

:::{exercise} Introduce your practice robot
:label: exercise-first-program
Print three lines introducing your imaginary practice robot: its name, one thing it can do, and one thing it cannot do yet. Add a comment explaining the purpose of the program.
:::

:::{hint} A place to start
:class: dropdown
Start by changing text inside one existing pair of quotation marks.
:::

:::{hint} A more specific hint
:class: dropdown
Use one print call for each line. Keep parentheses and matching quotes around each string.
:::

::::{solution} exercise-first-program
:class: dropdown
One possible result names a robot, describes an intake, and notes that autonomous is not implemented. Your wording can differ; the order and separate lines should match your plan.

```{literalinclude} ../../examples/foundations/solutions/first_program.py
:language: python
```
::::

## Before moving on

Without looking back, explain what the quotes, parentheses, and comment each do. Change the final line, save, rerun, and point to the changed output.

