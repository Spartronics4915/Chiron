---
title: Git and GitHub
---

Imagine spending a meeting getting your intake working, changing it the next
day, and realizing it no longer behaves correctly. You could keep folders named
`robot-final` and `robot-final-really-final`, but they quickly become hard to compare.
**Git** gives us a more useful way to remember what changed.

## Repository

A **repository**, often shortened to **repo**, is a project whose history Git
tracks. You edit files normally, then choose when to record a checkpoint called
a **commit**. Each commit has a description and an identifier. You can compare
commits to see exactly which lines changed instead of trying to remember.

Saving in VS Code updates a file on your computer. Committing records a checkpoint
in your local repository. Neither operation automatically puts your work online.

**GitHub** is the website that stores a remote copy of a Git repository. A **push**
sends your local commits to that remote. This lets you share your work and
gives you another copy if something happens to your computer.

```{mermaid}
flowchart LR
  Edit[Edit a file] --> Save[Save to disk]
  Save --> Stage[Choose changes to stage]
  Stage --> Commit[Commit locally]
  Commit --> Push[Push to your GitHub fork]
```

**Staging** means choosing which saved changes belong in the next commit. A
**diff** shows additions and removals. Reviewing a diff is how you check that a
commit contains the changes you meant to make.

## Forking and Cloning

A **fork** is your own GitHub copy of someone else's repository. You'll fork
Chiron so your assignments have somewhere to live without changing the team's
official course. A **clone** downloads a repository and its history onto your
computer. We'll clone your fork, then write code in that local folder.

| Place | What it is for |
|---|---|
| Team's Chiron repository | Maintained lessons and examples |
| Your GitHub fork | Online home for your commits |
| Your local clone | Files you edit and run in VS Code |

Git calls a named remote connection a **remote**. Our clone calls your fork
`origin`. We will add the team repository as `upstream` so you can receive course
fixes later. These are names pointing to URLs, not separate folders on your laptop.

## Branches

A **branch** is a named line of work. We'll use a branch called `learning` for
your course progress. Later a short-lived branch lets you try a change and ask for
a **pull request** review, a discussion of proposed changes before merging them.
You do not need to master branching today; start by knowing where your work is saved.

Before continuing, think about these two situations:

1. You saved a **file** but did not commit. What has Git recorded?
2. You committed but cannot see the new commit on GitHub. What step might be missing?

:::{hint} Check your explanation
:class: dropdown
Saving alone does not create a commit. A local commit reaches GitHub after a
successful push to the expected remote and branch.
:::

[Next: fork and clone Chiron](forking-and-cloning.md).
