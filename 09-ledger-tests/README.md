# Test Birr Ledger

A test suite for Birr Ledger v1, with **pytest**. You build it step by step in
the browser in lesson 9.5 of the Mawj Python course; here you run the same tests
on your computer or in a codespace.

`ledger.py` is Birr Ledger v1, finished: the program from lesson 8.9's last
milestone. (If you built your own in `08-birr-ledger`, you can copy yours in
instead, as long as the names match.) `test_ledger.py` starts with the two tests
from milestone 1.

## Run the tests

In a terminal, in this folder:

```
uv run pytest
```

`pyproject.toml` lists pytest as a **dev dependency**: a package you need to work
on the project (to test it), not to run it. The first time, `uv run` installs
pytest into this folder's `.venv`, then runs it. After that it starts straight
away.

Without uv, install pytest in a virtual environment (lesson 8.8) and run
`python -m pytest`.

pytest prints a header first (your platform, Python and pytest versions, and this
folder), then a dot for each passing test and the summary, like `2 passed`. It
also makes a `.pytest_cache` folder, which is ignored by Git. To get the short
report the website shows, run `uv run pytest -q`.

## The names (fixed)

| Name | What the tests check |
| --- | --- |
| `add_expense(expenses, amount, category, note, date=None)` | Adds one expense dict. Tests always pass a fixed `date`, so the result is the same every day. |
| `total_by_category(expenses)` | Returns each category's total (a `Counter`). |
| `save_expenses(expenses, path=LEDGER_FILE)` | Writes the list as JSON. Tests pass a file in `tmp_path`, never the real `ledger.json`. |
| `load_expenses(path=LEDGER_FILE)` | Reads it back; a missing file gives `[]`. |
| `sample_expenses` | Your fixture (milestone 2): 8.9's three expenses. |

The tests go in `test_ledger.py`. pytest finds files named `test_*.py` and runs
the functions in them whose names start with `test`.

## What the suite must test

- **Adding:** an expense added with a fixed date gives exactly the dict you expect.
- **Totals:** each category's total, a category with no expenses (0), and an
  empty ledger (no totals).
- **Bad amounts:** an amount of 0 or less raises `ValueError` (`pytest.raises`).
- **Files:** a save and load in `tmp_path` gives back the same list, Amharic notes
  included; the saved file's text keeps Amharic readable (`ensure_ascii=False`);
  loading a file that doesn't exist gives `[]`.

## Milestones

Run `uv run pytest` after each one.

1. **Two happy paths.** Already in `test_ledger.py`: adding one expense, and one
   category's total. `2 passed`.
2. **The fixture.** Write `sample_expenses` with `@pytest.fixture` (it needs
   `import pytest`): 8.9's three expenses, made with `add_expense` and fixed
   dates. Make both tests use it. `2 passed`.
3. **Totals.** One test with `@pytest.mark.parametrize` over each category's
   total, including one with no expenses, and a test for an empty ledger. A test
   can take a fixture and parametrize's names together:
   `def test_category_total(sample_expenses, category, expected):`. `6 passed`.
4. **Bad amounts, test-first.** Test that `add_expense` raises `ValueError` for 0
   and -50 (the rule: an amount must be more than 0). Run it: `2 failed, 6 passed`,
   with `DID NOT RAISE`, because v1 accepts any whole number. That's a real bug. Fix it in `ledger.py`: `add_expense` raises the
   error, and `main()` catches it, says the expense wasn't added, and saves
   nothing.
5. **Files.** A round trip with `tmp_path` (save `sample_expenses`, load it back,
   compare), and loading a file that doesn't exist. `10 passed`.
6. **Check your suite.** Plant each bug below in `ledger.py`, one at a time, and
   run the tests. At least one test should fail every time. Undo each bug after.
   - In `total_by_category`, loop over `expenses[:-1]` (the last expense is
     skipped).
   - In `save_expenses`, leave out `ensure_ascii=False` (Amharic is saved as
     `\u` escapes).
   - In `load_expenses`, remove the `try`/`except` (a missing file crashes).

   The Milestone 5 suite misses the second bug: escaped Amharic loads back the
   same, so the round trip still passes. Add a test that reads the saved file's
   text and checks the Amharic is in it. If any other bug gets through, add the
   test that catches it.

## Hints

- `tmp_path` is a fixture that comes with pytest: name it as a parameter and you
  get a new, empty folder for that test. `tmp_path / "ledger.json"` is a file in it.
- A round trip can't see how the file looks: escaped Amharic loads back the same.
  To check the text, read it with `path.read_text(encoding="utf-8")`.
- A `Counter` equals a dict with the same keys and values, so
  `total_by_category(...) == {"food": 310}` works.
