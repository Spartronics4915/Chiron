---
title: Methods and changing state
---

You can now make two intake objects and keep their information separate.
Next, let's give each intake an action it can perform. That action is a **method**.
It works much like the functions you've already written, with `self` identifying
which intake we're working on.

## Keeping state between calls

**State** is information a program keeps between operations. `has_piece` is
state: another part of the program may ask about it after an update finishes.
In contrast, a method's plain local name, such as `request`, belongs to that call.
Using `self.output` means we intentionally keep the output on the object.

Calling `intake.update(0.5, True, False)` supplies three explicit arguments.
Python also supplies `intake` as `self`, so the definition has four parameters.
Don't pass `self` a second time in a normal bound-method call.

An update method can apply all the mechanism's rules in one place. This keeps
callers from needing to remember the same safety decisions every time. A `stop`
method can communicate intent clearly even though its body only assigns zero.

## Read it before running it

```{include} ../../snippets/terminal-reminder.md
```

Put this worked example in `student-work/foundations/methods_and_state.py`.
Read it once and write down what you think it prints. Then save and run
`python student-work/foundations/methods_and_state.py` using your environment's Python.

```{literalinclude} ../../examples/foundations/worked/methods_and_state.py
:language: python
```

Trace the outputs: 0.5, 0.0, -0.5, 0.0. The same instance persists through
the calls; we aren't constructing a new intake each time. Stop sets an output,
but it does not pretend that the sensor no longer sees a piece.

Objects and lists are **mutable**, meaning they can change. If you write
`other_name = intake`, both names refer to the same object. That differs from
creating a second `Intake()`. This explains why changing a list through an alias
changes the list seen through its original name as well.

## Try it yourself

:::{exercise} Record each intake output
:label: exercise-methods-and-state
Add your clamp function to the intake behavior and store output history in a list on each instance. Append once per update. Create two intakes and prove their histories are separate.
:::

:::{hint} A place to start
:class: dropdown
Create each history in `__init__` with `self.history = []`.
:::

:::{hint} A more specific hint
:class: dropdown
After deciding the final output, append it once outside the branches. Do not create a shared history list directly under the class definition.
:::

::::{solution} exercise-methods-and-state
:class: dropdown
Each update records the final bounded output. Separate construction calls create separate history lists. A stop method can either record an event or not, but document the choice consistently.
::::

## Before moving on

Create two names for the same intake and a separate intake instance. Give both
instances nonzero outputs, then call `stop` through the second name. Predict
which outputs will change before printing them. If the result surprises you,
look back at the assignments that created each name.

Explain `self.output` versus a local variable. Predict what happens after `other = intake; other.stop()`, then verify that both names refer to the same changed object.

