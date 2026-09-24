---
title: Saving and Git
---

You changed your first program. Let's record that change so you can find it later.
Use the terminal in your Chiron folder; these are Git commands, not Python code.


```{include} ../../snippets/terminal-reminder.md
```

## Make a commit

Run `git status`. New files appear as **untracked** until you ask Git to track them.
Select your assignment folder for the next checkpoint:

```sh
git add student-work/foundations
git diff --staged
```

`add` stages the saved files. `diff --staged` shows what the commit will record;
new lines are marked with `+`. If the display opens a pager, press `q` to return
to the prompt. Check that you staged your assignment, not `.venv` or unrelated files.

```sh
git commit -m "Change my first greeting"
git push
```

The message explains what changed. The earlier `push -u` tells Git which fork and
branch to push to now. Open your GitHub fork, select `learning`, and confirm your
new commit and assignment appear. If push fails, your local commit still exists;
read the message before trying again.

## Routine

Save files, run the program, inspect `git diff`, stage the intended changes, commit,
and push. Commit after a meaningful small step; don't wait for the whole course to
be finished. `git status` shows what remains unsaved in Git history, although it
cannot see unsaved editor buffers.

## Inspect or Recover

`git log --oneline` lists commits with short identifiers. To view an older file
without changing your current one, substitute an identifier in:

```sh
git show COMMIT:student-work/foundations/main.py
```

Copy a needed line back into the editor, save, and check it. If you want a completely
fresh starter while preserving your first attempt, use
`python tools/start_exercise.py foundations --name foundations-retry`.

Before moving on, think to yourself what Save, Commit, and Push each did.

(code-review)=
## Later: Review

You can use a pull request to read a change as one diff and leave notes beside
the code. With your work saved and committed on `learning`, create a branch
for the next change:

```sh
git switch -c mechanism-review
```

Make your change, test it, and commit it as before. Upload the branch:

```sh
git push -u origin mechanism-review
```

On GitHub, open **Pull requests → New pull request** in **your fork**. Set both
repositories to your fork, the base branch to `learning`, and the compare branch
to `mechanism-review`. Read the displayed diff before creating the review. It
should show the new change, not the whole course. This review proposes adding your change to your learning branch; it doesn't
submit an assignment to the team's official repository.

:::{note} Receiving course fixes
Before an update, save, commit, and push your assignment changes. Run
`git fetch upstream` to download information about team changes; fetching alone
does not change your working files. Apply fixes marked compatible with your
course version, using the update command in that release's notes. If no compatible
update is listed, keep working from your current version. If a merge reports a
conflict you aren't ready to resolve, `git merge --abort` returns to the state
before that merge; this is why you committed your work first. Test your work after
a completed update, then push it. A new course release may use different libraries.
:::
