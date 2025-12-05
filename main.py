# main.py

from core import add_expense, view_expenses, total_expense, search_expenses, monthly_summary, analytics, edit_expense, delete_expense
from utils.formatter import print_title, print_line

def main_menu():
    while True:
        print_title("EXPENSE TRACKER")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Search Expenses")
        print("5. Monthly Summary")
        print("6. Analytics")
        print("7. Edit Expense")
        print("8. Delete Expense")
        print("9. Exit")
        print_line()

        choice = input("Enter choice (1-9): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            search_expenses()
        elif choice == "5":
            monthly_summary()
        elif choice == "6":
            analytics()
        elif choice == "7":
            edit_expense()
        elif choice == "8":
            delete_expense()
        elif choice == "9":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please select 1-9.")

if __name__ == "__main__":
    main_menu()
