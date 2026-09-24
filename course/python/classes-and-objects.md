---
title: Classes and objects
---

Our intake now has a few things to remember and a few actions it can take.
Let's give them a home together. A **class** describes a kind of object, such as
an intake. An **instance** is one particular intake made from that description.
Those words take some getting used to; the two-intake example below will help.

## Creating separate instances

Think about two intakes on two different robots. They follow the same rules,
but one may hold a piece while the other is empty. They should not accidentally
share the same possession value. Each instance needs its own **attributes**:
named values stored on that object.

`class Intake:` introduces the class. Inside it, `def __init__(self):` defines
the initializer, which runs when we create an instance with `Intake()`. Keep both
underscores on each side of `init`; this is a special Python method name.

`self` means the particular instance we're setting up or working with.
`self.has_piece = False` stores a value on that instance. Later, when you call a
method through an intake object, Python passes that intake as `self` for you.

If this still feels abstract, that's okay. Start by following the two objects in
the example. Watch which one changes and which one stays the same; we'll add more
methods after that distinction is comfortable.

## Read it before running it

```{include} ../../snippets/terminal-reminder.md
```

Put this worked example in `student-work/foundations/classes_and_objects.py`.
Read it once and write down what you think it prints. Then save and run
`python student-work/foundations/classes_and_objects.py` using your environment's Python.

```{literalinclude} ../../examples/foundations/worked/classes_and_objects.py
:language: python
```

The front prints True while the rear prints False. `Intake` is the class;
`front` and `rear` name different instances. The dot selects an attribute of the
object on its left. Creating the rear intake does not reset the front intake.

Try `rear.output = -0.3` and print both outputs. They remain independent. Note
that none of this connects a motor: we're modeling values in memory. In Stage 1,
we'll give an object an output adapter that talks to a simulated mechanism.

## Try it yourself

:::{exercise} Model two launchers
:label: exercise-classes-and-objects
Create a `Launcher` class with `target_speed` and `measured_speed`, both initially zero. Make two instances, change one target, and demonstrate that the other is unaffected.
:::

:::{hint} A place to start
:class: dropdown
Initialize attributes through `self` inside `__init__`.
:::

:::{hint} A more specific hint
:class: dropdown
Create two objects with separate calls to `Launcher()`, rather than assigning one name to the other.
:::

::::{solution} exercise-classes-and-objects
:class: dropdown
A class describes the structure; two construction calls create independent instances. Two names for one instance would share the same attributes.

```{literalinclude} ../../examples/foundations/solutions/classes_and_objects.py
:language: python
```
::::

## Before moving on

Point to the class, initializer, instances, and attributes in your file. Explain why the second object still has a zero target.

