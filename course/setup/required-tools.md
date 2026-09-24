---
title: Required Tools
---

We use several tools when programming a robot, but each has a different job.
Installing everything without knowing why can get confusing, so let's start with
the tools you'll actually need for this course.

| Tool | What it does |
|---|---|
| Python | Runs the instructions you write in the Python language |
| VS Code | Lets you create, read, and edit your program's files |
| Git | Records checkpoints of those files so you can review or recover changes |
| GitHub | Hosts a copy online and lets you share changes with other people |

RobotPy is a collection of Python libraries for FRC. A **library** is code someone
else has already written for you to use. We'll install the course's libraries 
together after cloning the repository; you don't need to choose individual versions.

## Install Python

This course baseline uses **Python 3.14.7** and **RobotPy 2026.2.2**. Install the
matching version from the [Python 3.14.7 release page](https://www.python.org/downloads/release/python-3147/).
Use a regular desktop installation, not Python compiled for a robot controller.
If these tools are already installed, start with the version checks below;
you don't need another copy. You'll need a computer where you can install these
tools; school-managed computers may restrict installation.

::::{tab-set}
:::{tab-item} Windows
:sync: windows
1. On the release page, scroll to **Files** and choose **Windows installer (64-bit)**
   for a usual Intel/AMD Windows laptop. The embeddable package is not the installer.
   RobotPy's Windows baseline supports 64-bit Intel/AMD Windows 10 or 11;
   ARM Windows laptops need a different supported computer for these exercises.
2. Open the downloaded installer and keep its Python launcher option enabled.
   Finish installation before continuing.
3. Open **Command Prompt** from Start. Enter `py -3.14 --version` and press Enter.
   You should see `Python 3.14.7`.

If `py` is not found, reopen Command Prompt. If it still fails, reopen the Python
installer, choose **Modify**, and check that the launcher is selected. Finish the
installation and try a new Command Prompt. We'll use this terminal type in VS Code too.

RobotPy also needs Microsoft's **Visual C++ Redistributable** on Windows.
Open [Microsoft's runtime downloads](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)
and choose **X64** under the latest supported v14 package. Run that installer;
if it reports an existing compatible installation, keep it. This installs runtime
libraries used by RobotPy, not the Visual Studio editor. The requirement comes
from [RobotPy's installation guide](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/python-setup.html).
:::
:::{tab-item} macOS
:sync: unix
1. On the release page, choose **macOS installer** and open the downloaded `.pkg`.
2. Complete the installer, then open **Terminal** from Applications → Utilities.
3. Run `python3.14 --version`. You should see `Python 3.14.7`.

The RobotPy baseline needs macOS 13.3 or newer even if Python itself supports an
older macOS. Leave the operating system's Python in place.
:::
:::{tab-item} Linux
:sync: linux
These instructions target 64-bit Ubuntu 22.04/24.04. First run
`python3.14 --version` in Terminal. If it reports `Python 3.14.7`, you're ready.

If that version is missing, use **uv**, a tool that can install a separate Python
without replacing Ubuntu's own copy. Follow the Linux steps on
[uv's installation page](https://docs.astral.sh/uv/getting-started/installation/),
then close and reopen Terminal. Check that `uv --version` reports a version and run:

```sh
uv python install 3.14.7
```

This downloads the course's Python version. Reopen Terminal and check
`python3.14 --version` again. If the command is not found, follow the PATH
instructions printed by uv's installer. The
[Python installation guide](https://docs.astral.sh/uv/guides/install-python/)
explains how uv makes the versioned command available. After this step, use the
same `python3.14` commands as macOS throughout setup.
:::
::::

:::{note}
The **terminal** is an application where you type commands for your computer to run. 
The text already shown before your cursor is its prompt; you do not type that prompt as part of a command. 
We will use VS Code's built-in terminal shortly.
:::

## First Instruction

Before installing the rest, let's use Python for something you can change yourself. 
In the terminal you just used to check its version, run the command for your system:

::::{tab-set}
:::{tab-item} Windows
:sync: windows
```bat
py -3.14 -c "print('Hello, Spartronics!')"
```
:::
:::{tab-item} macOS / Linux
:sync: unix
```sh
python3.14 -c "print('Hello, Spartronics!')"
```
:::
::::

You should see `Hello, Spartronics!`. Change the words inside the single quotes to
a greeting of your own and run it again. Keep the quotes and parentheses in place.
`print` displays the text you give it; `-c` lets us run that tiny program directly
from the command line. We'll learn to save programs in files next.

That's your first edit-and-run cycle. The remaining setup gives you a comfortable
place to write longer programs and a way to keep your work.

## Install VS Code and Git

Download [VS Code](https://code.visualstudio.com/download) for your operating
system. Open the download and finish installation; on macOS, move the app into
Applications. Launch VS Code and confirm that its window opens.

Then follow [Git's installation page](https://git-scm.com/downloads) for your
operating system. On Windows, the standard installer options are sufficient.
Reopen your terminal after installation and run `git --version`; a version
number confirms Git is available. You do not need to memorize it. Close and
reopen VS Code too if it was open before you installed Git.

Open VS Code's Extensions view using the blocks icon on the left. Search for **Python**
published by Microsoft and install it. Also install Microsoft's **Jupyter** extension
for the notebook lesson. Extensions add capabilities to the editor; they are
different from the Python libraries your program imports.

## Create a GitHub account

Visit [GitHub](https://github.com/) and create an account if you don't have one.
Use an account you can keep using for team projects. Complete account setup yourself
and keep your password private. GitHub will guide you through email verification.
Our next pages explain what you're going to store there.

## What can wait?

Driver Station controls a physical FRC robot; dashboards such as Elastic and
analysis tools such as AdvantageScope help us interact with and inspect robot data.
They are useful team tools, but our local lessons use WPILib's simulation window.
You do not need to install every competition tool before your first Python program.
Website tools such as Node and MyST are for site contributors, not course students.

Before continuing, confirm Python and Git both report versions and VS Code opens.
