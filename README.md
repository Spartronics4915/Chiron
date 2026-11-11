# Chiron

Spartronics 4915's MyST programming course. Start at
[the course](course/index.md). It assumes no programming experience and progresses
from setup and Python to a tested intake subsystem and commands.

Students: follow [required tools](course/setup/required-tools.md), then the setup
sequence. Work goes in your fork's `student-work/`. No Node/MyST installation is
needed for programming exercises.

Contributors:

```sh
uv sync --frozen --group docs
npm ci
uv run python tools/validate.py
npm start
```

Course pages live under `course/`, with reusable example code under
`examples/course/`. Hardware guides and library references are deferred.
