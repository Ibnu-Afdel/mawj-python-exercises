"""Tests for Birr Ledger v1 (lesson 9.5). Run them with: uv run pytest"""

from ledger import add_expense, total_by_category


def test_add_expense():
    expenses = []
    add_expense(expenses, 250, "food", "ቡና", "2026-10-01")
    assert expenses == [
        {"date": "2026-10-01", "amount": 250, "category": "food", "note": "ቡና"},
    ]


def test_total_by_category():
    expenses = []
    add_expense(expenses, 250, "food", "ምሳ", "2026-09-29")
    add_expense(expenses, 60, "food", "ቡና", "2026-09-30")
    assert total_by_category(expenses) == {"food": 310}


# Milestone 2: a sample_expenses fixture with 8.9's three expenses, made with
# add_expense and fixed dates (import pytest for @pytest.fixture). Then make
# both tests above use it.

# Milestone 3: one parametrized test for each category's total, including a
# category with no expenses; then the totals of an empty ledger.

# Milestone 4: add_expense should raise ValueError for an amount of 0 or -50.
# Write the test first and watch it fail, then fix add_expense in ledger.py
# (and let main() handle the error).

# Milestone 5: save sample_expenses to a file in tmp_path and load it back;
# then load a file that doesn't exist. Also check that the saved file's text
# keeps the Amharic notes readable.
