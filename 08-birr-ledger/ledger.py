"""Birr Ledger v1: a personal expense tracker that remembers between runs.

See README.md in this folder for what to build. Keep the names below exactly:
the next versions of Birr Ledger build on them.
"""

import datetime
import json
from pathlib import Path

# Saved next to this file, whatever folder the terminal is in.
LEDGER_FILE = Path(__file__).parent / "ledger.json"


def load_expenses():
    """Return the list of expenses saved in LEDGER_FILE.

    If the file doesn't exist yet, return an empty list.
    """
    # TODO: open LEDGER_FILE with encoding="utf-8" and json.load it.
    # TODO: catch FileNotFoundError (lesson 7.2) and return [] instead.
    pass


def save_expenses(expenses):
    """Write the list of expenses to LEDGER_FILE as JSON."""
    # TODO: json.dump with ensure_ascii=False and indent=2.
    pass


def add_expense(expenses, amount, category, note, date=None):
    """Add one expense to the list, dated `date` (text like "2026-10-01").

    With no date, it's dated today. Each expense is a dict:
    {"date": "2026-10-01", "amount": 250, "category": "food", "note": "ቡና"}
    """
    # TODO: if date is None, use datetime.date.today().isoformat();
    # then build the dict and append it to expenses.
    pass


def total_by_category(expenses):
    """Return a dict of category -> total birr, like {"food": 380}."""
    # TODO: the tally plan from lesson 4.4, or collections.Counter.
    pass


def main():
    """The menu: add, list, summary, quit. The only function that prints."""
    # TODO: load the expenses, then loop: ask for a command and handle it.
    # Reject amounts that aren't whole numbers (try/except ValueError).
    # Save after every change.
    print("Birr Ledger isn't built yet. Start with milestone 1 in README.md.")


if __name__ == "__main__":
    main()
