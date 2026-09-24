---
title: Functions and returned values
---

We've used our intake decision a few times now. It would be nice to write that
decision once and reuse it, especially when we need to fix a mistake. A **function**
lets us give the decision a name and try it with different inputs.

## Defining and calling a function

`def` tells Python that we're defining a function. We give it a name, then list
its inputs inside parentheses. These input names are called **parameters**.
The colon and indented body work like the blocks you've already seen.

Here's an easy detail to miss: defining a function doesn't run it. It gives Python
instructions to keep ready for when we call that function.

Calling `choose_output(0.4, True)` runs the function with those **arguments**:
the parameter `request` receives 0.4 and `enabled` receives True. `return` sends a
value back to the caller and leaves the function immediately. The caller can
save that value, print it, or use it in another decision.

Printing a value is different from returning it. A function that only prints
doesn't give the caller that number; with no return, Python returns `None`.
Names created inside a function are normally **local** to that call. That means
the caller can't use those names directly. Pass in what the function needs through
its parameters, then return the result you want the caller to use. This keeps the
connection between the two parts of your program easier to follow.

## Read it before running it

```{include} ../../snippets/terminal-reminder.md
```

Put this worked example in `student-work/foundations/functions.py`.
Read it once and write down what you think it prints. Then save and run
`python student-work/foundations/functions.py` using your environment's Python.

```{literalinclude} ../../examples/foundations/worked/functions.py
:language: python
```

The first call returns 0.4; the second returns 0.0. Follow the disabled call:
it reaches the first return, so it never executes the final return. Try changing
the first return to `print(0.0)` temporarily. The function now continues and returns
the request, which is the wrong disabled behavior. Restore it.

This is why we describe a function's **contract**: what inputs it accepts and
what result it promises. A clear contract makes the function easier to test and
reuse in a mechanism later.

## Try it yourself

:::{exercise} Reuse the intake decision
:label: exercise-functions
Write `intake_output(request, enabled, has_piece)` using your previous conditional. It should return a value rather than print inside the function. Call it for forward collection, a detected piece, reverse release, and disabled operation.
:::

:::{hint} A place to start
:class: dropdown
Move the decision into the function and pass all three changing values as parameters.
:::

:::{hint} A more specific hint
:class: dropdown
Return zero for disabled, then for a detected piece with positive request; otherwise return the request.
:::

::::{solution} exercise-functions
:class: dropdown
Printing belongs in the caller for this example. The decision function can now be reused by a terminal demonstration or a robot without changing its behavior.

```{literalinclude} ../../examples/foundations/solutions/functions.py
:language: python
```
::::

## Before moving on

Explain parameters versus arguments. Show that calling the function with two different requests does not require editing its definition.

