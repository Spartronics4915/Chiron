---
title: Forking and Cloning
---

Now that you know what the different copies are for, let's create yours. You'll
do this once for the course; each exercise will live inside the same repository.

## Create a Fork

1. Sign in to GitHub and open [Spartronics4915/Chiron](https://github.com/Spartronics4915/Chiron).
2. Select **Fork**. Set your personal account as the owner and keep the name `Chiron`.
3. Create the fork. Check that the page now shows **your username / Chiron**.

This creates a copy on GitHub. The files are not on your computer yet.

## Clone It

1. On your fork, select **Code**, choose **HTTPS**, and copy the repository URL.
2. In VS Code, open the Command Palette and choose **Git: Clone**.
3. Paste your fork's URL, then choose a parent folder such as `Documents/Robotics`.
   Prefer a local folder outside OneDrive or other syncing folders to avoid file-locking issues.
4. Open the cloned folder when VS Code asks. The Explorer should show Chiron's files.

Cloning is the course download; you don't also need **Download ZIP**. Choose the
parent folder once and let VS Code create `Chiron` inside it. On a later day,
open that existing folder rather than cloning another copy.

Check for `requirements.txt`, `course`, `examples`, and `tools` in Explorer.
If they are inside a second Chiron folder, use **File → Open Folder** to open
that inner folder. The commands below need the repository root.

If GitHub asks you to sign in, use its normal browser flow. Do not put passwords
or access tokens in Python files.

## Create a Branch

Open **Terminal → New Terminal**. Run this command once:

```sh
git remote add upstream https://github.com/Spartronics4915/Chiron.git
```

Then run `git remote -v`. `origin` should point to your username's fork;
`upstream` should point to Spartronics4915/Chiron. If `upstream` already exists,
inspect that output rather than adding it repeatedly.

For an individual start, use the course version you just cloned. Create your
learning branch from that checkout; you don't need to look up a commit identifier:

```sh
git switch -c learning
git push -u origin learning
```

`switch -c` creates and selects a new branch at your current version. `push -u`
uploads it and remembers where future pushes go. Your branch will not automatically
change when the team edits the course.

Run `git rev-parse HEAD` and save the displayed identifier in your notes. It names
the starting version, so you can tell which copy of the course you used. You don't
need to understand the letters and numbers or type them into another command.

Check that your clone contains `tools/start_exercise.py` and
`examples/foundations/starter/main.py`. If those files are absent, you have an older
checkout than this lesson describes. Compare the branch selected on GitHub with
the version linked by the course site. You'll need that course version before
continuing; reinstalling Python won't add the missing files.

## Authoring Commits

Git records an author with each commit. Set these for this repository, replacing
the examples with your chosen name and GitHub commit email:

```sh
git config user.name "Your Name"
git config user.email "YOUR-GITHUB-COMMIT-EMAIL"
```

You can find a private no-reply commit address in GitHub's email settings if you
don't want commits to contain your personal email. These settings identify commits;
they are not your GitHub password or a login command.

Run `git status`. It should name `learning` and have no unexpected changes.
