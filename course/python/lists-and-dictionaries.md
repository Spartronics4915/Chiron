---
title: Lists and dictionaries
---

One sensor reading is useful, but sometimes we want to look at several readings
together. Instead of inventing a new variable for each one, we can put them in a
**list**. We'll also meet **dictionaries**, which let us find values by a name.

## Storing related values

A **list** stores items in order: `readings = [False, False, True]`. Square
brackets create the list; commas separate its items. An **index** selects one
item, starting from zero: `readings[0]` is the first. `readings[-1]` selects the
last. An index outside the list raises `IndexError`.

`len(readings)` gives its length. `readings.append(False)` adds an item to the
existing list. The dot accesses an operation belonging to that object; this
operation is called a **method**. A `for reading in readings:` loop visits each
item directly, so you often don't need to manage indexes yourself.

A **dictionary** stores values under named keys:
`inputs = {"request": 0.5, "enabled": True}`. Curly braces create it; each colon
separates a key from its value. `inputs["request"]` retrieves the matching value.
An absent key raises `KeyError`. Use a list for an ordered sequence and a dictionary
when meaningful names make the data clearer.

## Read it before running it

```{include} ../../snippets/terminal-reminder.md
```

Put this worked example in `student-work/foundations/lists_and_dictionaries.py`.
Read it once and write down what you think it prints. Then save and run
`python student-work/foundations/lists_and_dictionaries.py` using your environment's Python.

```{literalinclude} ../../examples/foundations/worked/lists_and_dictionaries.py
:language: python
```

The output reports three samples, one detected sample, and request 0.5. Append
another True reading and predict which outputs change. Notice that counting true
samples does not count separate physical pieces: one piece might remain detected
for many samples. Choose names that match what your program actually measures.

Temporarily misspell `"request"` when looking up the key. Compare that `KeyError`
with the `NameError` from earlier. One is a missing dictionary key; the other is
a missing Python name.

## Try it yourself

:::{exercise} Filter motor requests
:label: exercise-lists-and-dictionaries
Store `[0.2, 0.8, 0.4, 0.9]` in a list. Build a new list containing only requests above 0.5. Print both lists and their lengths. Then put the limit and the filtered list in a dictionary with descriptive keys.
:::

:::{hint} A place to start
:class: dropdown
Start with an empty result list: `high_requests = []`.
:::

:::{hint} A more specific hint
:class: dropdown
Inside the loop, append the current request only when it passes the comparison.
:::

::::{solution} exercise-lists-and-dictionaries
:class: dropdown
The filtered result is [0.8, 0.9], length 2; the original remains length 4. A value exactly 0.5 does not pass `> 0.5`.

```{literalinclude} ../../examples/foundations/solutions/lists_and_dictionaries.py
:language: python
```
::::

## Before moving on

Explain why the first item uses index zero and why a dictionary key uses quotes here. Revisit your loop accumulator: what happens if you reset the result list inside the loop?

