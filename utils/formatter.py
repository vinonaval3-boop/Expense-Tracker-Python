# utils/formatter.py

def print_title(title: str) -> None:
    """
    Prints a formatted title for sections in the console.
    
    Args:
        title (str): The title text to display
    """
    print("\n" + "-" * 40)
    print(f"{title.center(40)}")
    print("-" * 40)


def print_menu() -> None:
    """
    Prints the main menu options for the Expense Tracker.
    """
    print("\n" + "-" * 40)
    print("CHOOSE AN OPTION:".center(40))
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Delete Expense")
    print("4. Edit Expense")
    print("5. Exit")
    print("-" * 40)


def print_line() -> None:
    """
    Prints a horizontal separator line.
    """
    print("-" * 40)