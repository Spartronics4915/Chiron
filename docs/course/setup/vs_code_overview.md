---
title: VS Code Overview
---

# Qué es VS Code?

**Visual Studio Code (VS Code)** is a free and open source code editor created by Microsoft. It’s available on Windows, macOS, and Linux and can support virtually every programming language through available extensions on its **Extension Marketplace**. It also has integrated Git support which lets you stage, commit, push, pull, and view diffs from the Source Control panel without leaving the editor.

The **Extension Marketplace** is a super useful tool, and it is what makes VS Code extremely unique. If you ever have extra time consider messing around with extensions and themes!

# Welcome Screen

When you first open up VS Code, you are greeted with a welcome screen that has a few options. From here you can select “File” and the file menu will appear. Many options are available, but the main ones are:

:::{note}
When opening a new folder, VS Code will have a message that asks “Do you trust the authors of the files in this folder?” For this website, you can click “Yes, I trust the authors”.
:::

:::{warning}
When creating a new robot project, do not save it to the OneDrive! Creating new projects on OneDrive is not supported.
:::

# Navigating the Interface

VS Code’s layout is categorized into a few key regions:

1. **Activity** Bar which is at the far left, consists of vertical icons which can be used to switch between the major views (Explorer, Search, Source Control, Run & Debug, Extensions).
2. **Side Bar** which is next to the activity bar shows details for the selected view (for example: file tree in Explorer).
3. **Panel** is at the bottom of the screen. It has four main views, which are the Terminal, Problems, Output, and Debug Console.
4. **Editor** is the center area. The editor is star of the show and it is where you can view and edit files.
5. **Command Palette** is accessed through `Ctrl+Shift+P` / `Cmd+Shift+P` and it allows for you to search and run any command in VS Code.

# Saving and Opening Files

## Opening Files:

- Open a single file: `File > Open File...` or `Ctrl+O / Cmd+O`
- Open a folder/project: `File > Open Folder...` or `Ctrl+K Ctrl+O` / `Cmd+K Cmd+O`
- Quickly open a file: `Ctrl+P` / `Cmd+P`, then start typing the filename
- Reopen a recently closed file: `Ctrl+Shift+T` / `Cmd+Shift+T`

## Saving Files

- Save current file: `Ctrl+S` / `Cmd+S`
- Save as (new name/location): `Ctrl+Shift+S` / `Cmd+Shift+S`
- Save all open files: `Ctrl+K S` / `Cmd+K S`

:::{tip}
**Auto Save** can be enabled via `File > Auto Save` which saves your work automatically after a pause, making it way harder to lose your work
:::

A dot on a file’s tab indicates **unsaved changes**. The dot will disappear and turn into an “X” (close icon) once the file is saved.