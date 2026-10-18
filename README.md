# Programming Fundamentals: JavaScript (with Python alongside)

A 12-lesson course in Jupyter notebooks. You learn **JavaScript**, and every idea is also shown in
**Python**. Seeing two languages side by side teaches you the ideas behind programming, not just one
language's spelling. You also learn **Git and GitHub** by using them in every session.

## Lessons

| # | Notebook | You learn | Git & GitHub |
|---|---|---|---|
| 01 | `01_getting_started` | what a program is, running code, reading errors | fork, clone, `add`, `commit`, `push` |
| 02 | `02_values_types_variables` | types, variables, trace tables, operators | `status`, `diff`, `log` |
| 03 | `03_conditionals` | booleans, `if` / `else`, truthy and falsy | good commit messages |
| 04 | `04_loops` | `while`, `for`, loop patterns | remotes, `fetch` vs `pull` |
| 05 | `05_functions` | functions, `return`, scope, decomposition | undo with `restore` |
| 06 | `06_arrays_and_objects` | arrays/lists, objects/dictionaries, JSON | changes made on GitHub |
| 07 | `07_references_and_functions_as_values` | references, copies, `map` / `filter` / `reduce` | branches and `merge` |
| 08 | `08_errors_and_debugging` | stack traces, `try` / `catch`, debugging | merge conflicts |
| 09 | `09_modules_and_testing` | modules, tests, reading documentation | `.gitignore`, Markdown |
| 10 | `10_classes` | classes, `this` / `self`, inheritance | pull requests |
| 11 | `11_async_and_fetch` | async / await, Promises, fetching from an API | code review |
| 12 | `12_capstone_project` | your own project | issues, releases |

Each lesson follows the same rhythm: **warm-up** questions from earlier lessons, **predict** before you
run, **investigate** what happened, **make** your own code, **break** things on purpose, **explain** it
back, and a **Git checkpoint** at the end.

## Setup (once)

1. Install:
   - [Node.js](https://nodejs.org), the LTS version (20 or newer)
   - [Python](https://www.python.org/downloads/) 3.10 or newer. On Windows, tick **Add python.exe to PATH**.
   - [Git](https://git-scm.com/downloads)
   - [VS Code](https://code.visualstudio.com) with the **Jupyter** and **Python** extensions
2. Check that everything works. Open a terminal and run:
   ```bash
   node --version
   python --version
   git --version
   ```
3. Tell Git who you are (use the email of your GitHub account):
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```
4. Make your own copy of this repository. On GitHub, click **Fork** at the top of this page. Then clone
   **your fork** and connect it to the teacher's repository, which is called *upstream*:
   ```bash
   git clone https://github.com/<your-username>/programming-fundamentals.git
   cd programming-fundamentals
   git remote add upstream https://github.com/<teacher-username>/programming-fundamentals.git
   ```
5. Install what the notebooks need:
   ```bash
   python -m pip install -r requirements.txt
   ```
6. Open the folder in VS Code (**File → Open Folder**), open `01_getting_started.ipynb`, choose a Python
   kernel (**Select Kernel**, top right), and run the first cell.

## Every session

```bash
git pull upstream main             # get the new lesson from your teacher
# ... work through the notebook and save often (Ctrl + S) ...
git add <the notebook>
git commit -m "Complete lesson NN"
git push                           # upload your work to your fork
```

## How the notebooks work

- The first cell of every notebook is `%load_ext course_helpers`. **Run it first, every time.**
- Normal cells run **Python**. Cells that start with `%%node` run **JavaScript** with Node.js.
- Every `%%node` cell is a **separate program**: variables don't carry over between JavaScript cells.
  Python cells share variables until you restart the kernel.
- `%%node` cells stop after 10 seconds, in case of an infinite loop. Use `%%node --timeout 30` for slow programs.
- `check(actual, expected)` shows ✅ or ❌ in both languages.
- To keep error messages short, `%%node` cells hide Node's internal stack lines, and `cell:4:30` means
  line 4, column 30 of the cell.

## Troubleshooting

| Problem | Fix |
|---|---|
| ``UsageError: Cell magic `%%node` not found`` | Run the first cell of the notebook (`%load_ext course_helpers`). |
| `No module named 'course_helpers'` | Open the course **folder** in VS Code, not just the notebook file. |
| `Node.js was not found` | Install Node.js, then restart VS Code. |
| A Python cell runs forever | Click **Interrupt** (⏹) at the top of the notebook. |
| The notebook didn't change after `git pull` / `git switch` | Close the notebook and open it again. |
| You prefer Jupyter in the browser | `python -m pip install jupyterlab`, then `jupyter lab` |

## Files

- `NN_*.ipynb`: the lessons
- `course_helpers.py`: makes `%%node` and `check()` work. You'll read it in lesson 09.
- `CHEATSHEET.md`: every JavaScript ↔ Python table from the course in one place (it arrives with lesson 12)
- `.gitignore`: files Git should ignore
