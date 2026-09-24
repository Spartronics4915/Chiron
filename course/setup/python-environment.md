---
title: Python environment
---

Our project uses libraries in addition to Python itself. A **virtual environment**
keeps those libraries together for this project so they don't clash with other
programs on your computer. Ours is a folder named `.venv` inside Chiron.

## Why use one?

Your first `print` program works without an environment. We use one because
Chiron and another robot project might need different RobotPy versions. Installing
one project's packages should not replace the other's. Python's
[virtual-environment guide](https://docs.python.org/3.14/tutorial/venv.html)
explains this separation.

The environment runs locally using the Python version you created it with. It
doesn't create a virtual computer or simulate the robot. **Activation** just
makes this terminal find the environment's Python when you type `python`.
Your `.py` files stay in `student-work`; they are not stored inside `.venv`.
Git ignores the environment because it can be recreated from the package list.

There are three separate jobs: **create** the environment once, **install** the
listed libraries into it, then **activate** it when starting a new terminal.

## Create and Install

Open Chiron in VS Code. Run these lines one at
a time, waiting for each to finish. The terminal should be in the folder containing
`requirements.txt`. That file lists the exact library versions for this course.
If you aren't sure you have the right folder, look for it in VS Code's Explorer
and open a fresh terminal with **Terminal → New Terminal**. Stop after any failed
command; later steps depend on it succeeding.

::::{tab-set}
:::{tab-item} Windows
:sync: windows
In the Terminal panel, use the arrow beside **+** and choose **Command Prompt**.
If needed, search **Terminal: Select Default Profile** in the Command Palette,
choose **Command Prompt**, and open a new terminal. These steps use Command Prompt,
not PowerShell, so activation does not require changing an execution policy.

**Create** the environment. This usually finishes without printing a message;
look for the new `.venv` folder in Explorer:

```bat
py -3.14 -m venv .venv
```

**Activate** it in this terminal:

```bat
.venv\Scripts\activate.bat
```

**Install** the course libraries:

```bat
python -m pip install -r requirements.txt
```
Activation makes the short `python` commands in later lessons use this environment.
When you open a new Command Prompt terminal, run `.venv\Scripts\activate.bat` again
from the Chiron folder. You only create the environment and install packages once.

:::
:::{tab-item} macOS / Linux
:sync: unix
Use **Terminal → New Terminal** in VS Code.

**Create** the environment, then **activate** it and **install** the libraries.
Run each line separately:

```sh
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```
Run `source .venv/bin/activate` again whenever you open a new terminal in Chiron.
You only create the environment and install packages once.
:::
::::

Installation downloads packages and can take several minutes. Wait until the
terminal's prompt returns. A successful install reports installed packages or
that they are already satisfied; a red error needs attention before continuing.
You can rerun the same install command after fixing a connection problem. A
notice offering a newer pip version is not itself an installation failure.

`-m venv` asks Python to run its environment-creation tool. `-m pip install -r`
asks the new environment to install the packages listed in a file. You aren't
expected to memorize these flags; the commands are here for reference.

In the Command Palette choose **Python: Select Interpreter** and select `.venv`.
An **interpreter** is the program that executes Python. Selecting one tells VS Code
which Python to use. VS Code may also activate it in new terminals, but let's
check instead of assuming it did.

If `.venv` is not listed, choose **Enter interpreter path** and browse to
`.venv/Scripts/python.exe` on Windows or `.venv/bin/python` on macOS/Linux.

(check-python-environment)=
## Check Python

Run this in the terminal you plan to use for the lesson:

```sh
python -c "import sys; print(sys.executable)"
```

The path should end in `Chiron\.venv\Scripts\python.exe` on Windows or
`Chiron/.venv/bin/python` on macOS/Linux. Your parent folder may be different.
The important part is **this project's `.venv`**. If another Python appears,
activate the environment using your operating-system tab above, then check again.

You can now use the short `python` commands throughout the course. If a later
lesson says a library is missing, repeat this check before reinstalling anything.

## Check Environment

Using the environment's Python as explained in the tabs, run:

```sh
python --version
python -m pip check
python -c "import wpilib, commands2; print('RobotPy is ready')"
python tools/start_exercise.py foundations
python student-work/foundations/main.py
```

Expected: Python 3.14.7, `No broken requirements found.`, `RobotPy is ready`,
a message saying the exercise was created, and
`Hello, Spartronics!`. The helper copies starter files into `student-work/foundations`.
The maintained originals stay in `examples`, and your copies are yours to edit.
If you run the copy command twice it refuses to overwrite your first attempt.

If a command reports “no such file”, check the terminal's folder and the path.
If it reports “No module named ...”, check which Python you used. Keep the command
and complete error message together in your notes so you can compare the result
after each change. The table below covers the common setup problems.

| What you see | First thing to check |
|---|---|
| Cannot open `requirements.txt` or `tools/start_exercise.py` | Open the Chiron root folder, then a new terminal |
| Activation says the file is missing | Confirm `.venv` was created in this folder and that you chose the correct terminal tab |
| `No module named wpilib` | Check the Python path above; activate this environment, then rerun the package install if needed |
| Windows reports `DLL load failed` while importing RobotPy | Confirm the X64 Visual C++ runtime from [Required Tools](required-tools.md) is installed, reopen the terminal, and repeat the import check |
| Download or connection error | Keep the error text; restore network access and retry the same install command |
| No matching package version | Compare your OS, processor type, and Python version with [Required Tools](required-tools.md); keep the pinned requirements intact |

(returning-to-chiron)=
## Next Time

1. In VS Code, choose **File → Open Recent** and your existing Chiron folder.
2. Open a terminal. On Windows choose **Command Prompt**, then run
   `.venv\Scripts\activate.bat`. On macOS/Linux run `source .venv/bin/activate`.
3. Run the lesson's `python ...` command from the Chiron root. If there is any
   doubt about the interpreter, use [Check your Python](#check-python-environment).

That's all you need for a normal session. Don't recreate the environment or
copy an exercise again to resume working on it. Open your existing assignment.
Closing the terminal ends activation; it does not remove packages or your work.

## Try one edit

Open `student-work/foundations/main.py` in Explorer. Change the greeting inside
the quotation marks, save, and run it again. Confirm the new greeting appears.
We'll explain every part of that line in the first Python lesson.

[Next: save your first Git checkpoint](saving-your-work.md).
