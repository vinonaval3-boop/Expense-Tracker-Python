# utils/file_handler.py
import csv
import os
from typing import List, Optional

FILE = "data/expenses.csv"

def load_expenses() -> List[List[str]]:
    """
    Loads expenses from the CSV file.

    Returns:
        List[List[str]]: A list of [date, category, amount] entries.
    """
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r", newline="") as f:
            reader = csv.reader(f)
            rows = list(reader)
            # Skip header if present
            data = []
            for row in rows[1:] if rows and rows[0] == ["Date", "Category", "Amount"] else rows:
                if len(row) == 3 and row[2].replace(".", "", 1).isdigit():
                    data.append([row[0].strip(), row[1].strip(), row[2].strip()])
            return data
    except Exception as e:
        print(f"Error loading expenses: {e}")
        return []


def save_expense(date_or_data: str | List[List[str]], 
                 category: Optional[str] = None, 
                 amount: Optional[str] = None, 
                 overwrite: bool = False) -> None:
    """
    Saves an expense entry or list of expenses to the CSV file.

    Args:
        date_or_data (str | List[List[str]]): Either a date string for a single expense, 
                                              or a list of expenses for overwrite.
        category (Optional[str]): Category of the expense.
        amount (Optional[str]): Amount of the expense.
        overwrite (bool): Whether to overwrite the existing file.
    """
    os.makedirs(os.path.dirname(FILE), exist_ok=True)
    mode = "w" if overwrite else "a"

    try:
        with open(FILE, mode, newline="") as f:
            writer = csv.writer(f)
            if overwrite and isinstance(date_or_data, list):
                writer.writerow(["Date", "Category", "Amount"])
                for row in date_or_data:
                    writer.writerow(row)
            elif isinstance(date_or_data, str):
                writer.writerow([date_or_data, category, amount])
    except Exception as e:
        print(f"Error saving expense: {e}")