"""Birr Ledger v1, finished: the program from lesson 8.9's last milestone.

In lesson 9.5 you test it. Keep the names exactly: test_ledger.py imports them.
"""

import datetime
import json
from collections import Counter
from pathlib import Path

LEDGER_FILE = Path(__file__).parent / "ledger.json"


def load_expenses(path=LEDGER_FILE):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_expenses(expenses, path=LEDGER_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)


def add_expense(expenses, amount, category, note, date=None):
    if date is None:
        date = datetime.date.today().isoformat()
    expenses.append({
        "date": date,
        "amount": amount,
        "category": category,
        "note": note,
    })


def total_by_category(expenses):
    totals = Counter()
    for e in expenses:
        totals[e["category"]] = totals[e["category"]] + e["amount"]
    return totals


def main():
    expenses = load_expenses()
    while True:
        command = input("Command: ")
        match command:
            case "add":
                amount = None
                while amount is None:
                    try:
                        amount = int(input("Amount: "))
                    except ValueError:
                        print("Amount must be a whole number of birr.")
                category = input("Category: ")
                note = input("Note: ")
                add_expense(expenses, amount, category, note)
                save_expenses(expenses)
                print(f"Added {amount} birr for {category}.")
            case "list":
                if not expenses:
                    print("No expenses yet.")
                for e in expenses:
                    print(e["date"], e["amount"], "birr", e["category"], e["note"])
            case "summary":
                for category, total in total_by_category(expenses).most_common():
                    print(f"{category}: {total} birr")
            case "quit":
                print("Goodbye!")
                break
            case _:
                print("Unknown command. Try add, list, summary, or quit.")


if __name__ == "__main__":
    main()
