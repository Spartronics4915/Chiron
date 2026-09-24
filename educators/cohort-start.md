---
title: Starting a student or cohort
---

An individual student creates `learning` from the version they cloned. For a
group, choose and publish one reviewed version so everyone starts with the same
lessons and dependencies.

## Before sending students a repository link

1. Confirm the intended branch actually contains this course and its examples.
   A local uncommitted draft is not a version students can clone from GitHub.
2. Run `uv run python tools/validate.py` on the intended source and review its CI
   results after pushing. Test setup from a fresh clone, not your author environment.
3. Have a student who hasn't used these instructions follow the early lessons and
   final intake checks. Record where the written steps were incomplete and revise them.
4. For a cohort, choose the reviewed commit from the successful GitHub validation
   run. Open that run's commit link, copy its full identifier, and confirm it includes
   all intended lesson changes. Create a release tag for that exact commit through
   the repository's release process; do not tag an unreviewed moving branch head.
5. In release notes record Python/RobotPy versions, significant changes, known issues,
   and whether fixes remain compatible with the previous cohort.

No release has been published as part of this local implementation. Publishing the
reviewed source and baseline is a maintainer action, not something students must
guess their way through during setup.

## Give the group a complete starting instruction

Send the course URL, repository/fork instructions, **actual published tag**, and an
exact `git switch --detach TAG` command with that real tag already filled in.
Students run `git fetch upstream --tags`, then your checkout command, then the
lesson's `git switch -c learning`. Don't send a placeholder for students to resolve.

Verify that `git rev-parse HEAD` agrees across the group before assignments begin.
Record that identifier once in the cohort notes. Keep compatible fixes on that
baseline and announce approved update commands; don't silently switch students to
a new season's dependencies.

For an early pilot without a tag, distribute a reviewed **published** branch and
record its exact commit before the session. Help students check out that recorded
version before making their learning branch. A pilot can use reviewed commits;
it must not depend on unpublished files existing only on an author's laptop.
