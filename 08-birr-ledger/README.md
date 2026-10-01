# Birr Ledger v1

A personal expense tracker that **remembers your expenses between runs**. You
built it step by step in the browser in lesson 8.9 of the Mawj Python course;
here you build it for real, on your computer or in a codespace, where
`ledger.json` stays after the program ends.

Birr Ledger grows through the rest of the course, so the names below are fixed
from now on. Keep them exactly.

## What it does

Run it with `python ledger.py`. It shows a menu and asks for a command:

| Command | What happens |
| --- | --- |
| `add` | Asks for an amount in birr, a category, and a note, then saves the expense. |
| `list` | Prints every expense, one per line. |
| `summary` | Prints the total for each category. |
| `quit` | Ends the program. |

Your expenses are saved to `ledger.json`, in the same folder as `ledger.py`.
Run the program again tomorrow and they're still there.

## The rules

- **Each expense is a dict** with these four keys:
  ```python
  {"date": "2026-10-01", "amount": 250, "category": "food", "note": "ቡና"}
  ```
  `amount` is a whole number of birr (an `int`) for now; santim come in a later
  version. `date` is the day it was added, written as text: `"2026-10-01"`.
- **Saved as JSON** with `json.dump(expenses, f, ensure_ascii=False, indent=2)`,
  so the file is readable and Amharic notes stay Amharic. Open files with
  `encoding="utf-8"`.
- **A missing file means an empty ledger.** The first time you run it, there's
  no `ledger.json` yet: start with an empty list instead of crashing.
- **Bad amounts are rejected** with the `try`/`except` pattern from lesson 7.2:
  if the user types `abc` or `25 birr`, say so and ask again (or go back to the
  menu). Nothing bad gets saved.
- **Only `main()` prints** (and asks with `input()`). The other functions take
  values and return values, so they're easy to test and reuse later.

## The names (fixed for the whole course)

| Name | What it is |
| --- | --- |
| `LEDGER_FILE` | Where the ledger is saved: `ledger.json` next to `ledger.py`. |
| `load_expenses()` | Returns the list of expenses from `LEDGER_FILE` (an empty list if the file doesn't exist). |
| `save_expenses(expenses)` | Writes the list to `LEDGER_FILE` as JSON. |
| `add_expense(expenses, amount, category, note)` | Adds one expense dict, dated today, to the list. |
| `total_by_category(expenses)` | Returns a dict: category to total birr, like `{"food": 380, "transport": 40}`. |
| `main()` | The menu: asks for commands, calls the functions, prints results. |

## Milestones

Build it in this order, running it after each step:

1. **The data shape.** Write `add_expense`. Test it with a few lines at the
   bottom of the file: add two expenses to an empty list and print how many there
   are. (These test lines print only until `main()` takes over in milestone 3.)
2. **Save and load.** Write `save_expenses` and `load_expenses`. Run twice: the
   second run should load what the first one saved. Open `ledger.json` and read
   it.
3. **The menu.** Turn `main()` into the `add` / `list` / `quit` loop, like the
   contact book in lesson 4.9. Reject bad amounts.
4. **Summary.** Write `total_by_category` (a tally, or `collections.Counter`)
   and add the `summary` command.
5. **Stretch: commands from the terminal.** Use `argparse` so this works
   without the menu:
   ```
   python ledger.py add 250 food "ቡና"
   python ledger.py summary
   ```

## Hints

- `LEDGER_FILE = Path(__file__).parent / "ledger.json"` saves next to the
  script, whatever folder your terminal is in (lesson 8.2).
- Today's date as text: `date.today().isoformat()` (from `datetime import date`).
- `ledger.json` is in `.gitignore`, so your own expenses are never committed.
