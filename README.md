# Mawj Python exercises

Practice projects for the free [Mawj Python course](https://mawj.ibnuafdel.com/courses/python).
Each folder is one project, named after the module it belongs to. It has a
README with what to build and a starter file with the function names already
in place. There are no solutions here: the lessons walk you through each one.
(The one exception is `09-ledger-tests`, which tests a finished Birr Ledger v1,
so it includes one.)

Projects:
- [`08-birr-ledger`](08-birr-ledger/): Birr Ledger, a personal expense tracker
  that remembers your expenses between runs (Module 8, lesson 8.9).
- [`09-ledger-tests`](09-ledger-tests/): a pytest test suite for Birr Ledger v1,
  run with `uv run pytest` (Module 9, lesson 9.5).

You need Python 3.14 and an editor. Pick one of the two ways below.

## Option 1: in your browser, with GitHub Codespaces

No installing. Good if your computer can't run Python, or you only have a
laptop that isn't yours to set up.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Ibnu-Afdel/mawj-python-exercises?quickstart=1)

1. Sign in to GitHub (a free account is enough).
2. Press the button above, then **Create codespace**. The first start takes a
   few minutes; after that it opens faster.
3. You get VS Code in your browser with Python 3.14, the Python extension, and
   `uv` ready. Open a terminal with **Ctrl + `** (backtick) and try:
   ```
   python --version
   uv --version
   cd 08-birr-ledger
   python ledger.py
   ```

You need a steady internet connection the whole time you work.

### What's free, and how not to run out

Personal GitHub accounts get a free amount of Codespaces use every month
(check [GitHub's billing page](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces)
for the current numbers):

| Account | Compute | Storage |
| --- | --- | --- |
| GitHub Free | 120 core hours a month | 15 GB-month |
| GitHub Pro | 180 core hours a month | 20 GB-month |

A core hour is one processor core for one hour. The smallest codespace has 2
cores, so one hour of work uses 2 core hours: a free account gets about **60
hours a month** on it. That's plenty for this course if you stop your codespace
when you're done.

- **Stop it when you finish.** A codespace you leave open keeps using hours
  until it times out. To stop it: in the codespace, press **F1**, type
  `Codespaces: Stop Current Codespace`, and press Enter. Or go to
  [github.com/codespaces](https://github.com/codespaces), open the **...** menu
  next to it, and choose **Stop codespace**.
- **Storage counts even while it's stopped.** A stopped codespace keeps your
  files, and that uses your storage allowance until it's deleted. GitHub
  deletes a codespace after it has been stopped and unused for 30 days (you can
  make that shorter in your
  [Codespaces settings](https://github.com/settings/codespaces)).
- **Delete codespaces you don't need.** At
  [github.com/codespaces](https://github.com/codespaces), open the **...** menu
  and choose **Delete**. Keep one codespace for this repo and reuse it, instead
  of making a new one each time.
- **Save your work first.** Deleting a codespace deletes the files in it. To
  keep your code, fork this repo before you make your codespace and commit and
  push your changes, or download the files you want (right-click a file,
  **Download**).

When you've used up the free amount, codespaces stop working until next month,
unless you've added a payment method. Without one, you're never charged.

## Option 2: on your own computer, with VS Code

1. Install Python 3.14 (Module 0 of the course shows how on Windows, macOS, and
   Linux).
2. Install [VS Code](https://code.visualstudio.com/) and its **Python**
   extension (by Microsoft).
3. Get this repo: press the green **Code** button above, then **Download ZIP**,
   and unzip it. (If you use Git: `git clone https://github.com/Ibnu-Afdel/mawj-python-exercises.git`.)
4. In VS Code: **File → Open Folder**, and pick the `mawj-python-exercises`
   folder.
5. Open a terminal (**Terminal → New Terminal**) and run a project from its
   folder:
   ```
   cd 08-birr-ledger
   python ledger.py
   ```
   On Windows, use `py ledger.py` if `python` isn't found.

`uv` is optional for the early projects. Lesson 8.8 shows how to install it and
use it for projects that need packages.

### Optional: the same setup as Codespaces, on your computer

If you have Docker, VS Code's **Dev Containers** extension can open this folder
in the same container Codespaces uses (**F1 → Dev Containers: Reopen in
Container**).

## License

MIT. See [LICENSE](LICENSE).
