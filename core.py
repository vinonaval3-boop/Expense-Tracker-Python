# core.py

from utils.validator import validate_amount, validate_category
from utils.formatter import print_title, print_line
from utils.file_handler import save_expense, load_expenses
from collections import defaultdict
import matplotlib.pyplot as plt
import os

# -------------------- Core Functions --------------------

def add_expense():
    print_title("ADD NEW EXPENSE")
    date = input("Enter date (DD-MM-YYYY): ")
    
    category = input("Enter category (Food/Travel/Bills/Shopping/Other): ")
    category = validate_category(category)
    if not category:
        print("❌ Invalid category!")
        return

    amount = validate_amount(input("Enter amount: "))
    if amount is None:
        print("❌ Invalid amount!")
        return

    save_expense(date, category, amount)
    print("✔ Expense saved successfully!")

def view_expenses(data=None):
    print_title("ALL EXPENSES")
    data = data or load_expenses()
    if not data:
        print("No data found.")
        return

    print_line()
    for i, row in enumerate(data, start=1):
        print(f"{i}. {row[0]} | {row[1]} | ₹{row[2]}")
    print_line()

def total_expense():
    print_title("TOTAL EXPENSE")
    data = load_expenses()
    total = sum(float(row[2]) for row in data)
    print(f"💰 Total Spent: ₹{total}")

def search_expenses():
    print_title("SEARCH EXPENSES")
    data = load_expenses()
    if not data:
        print("No data found.")
        return

    print("Search by:\n1. Date\n2. Category")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        search_date = input("Enter date (DD-MM-YYYY): ")
        filtered = [row for row in data if row[0] == search_date]
    elif choice == "2":
        search_category = input("Enter category: ")
        filtered = [row for row in data if row[1].lower() == search_category.lower()]
    else:
        print("❌ Invalid choice!")
        return

    if not filtered:
        print("No expenses found.")
    else:
        view_expenses(filtered)

def monthly_summary():
    print_title("MONTHLY SUMMARY")
    data = load_expenses()
    if not data:
        print("No data found.")
        return

    summary = defaultdict(float)
    for row in data:
        date = row[0]
        amount = float(row[2])
        month_year = "-".join(date.split("-")[1:])  # MM-YYYY
        summary[month_year] += amount

    for month, total in summary.items():
        print(f"Month: {month} | Total Expenses: ₹{total}")

# -------------------- Analytics --------------------

def analytics():
    print_title("ANALYTICS")
    data = load_expenses()
    if not data:
        print("No data found.")
        return

    # ---------------- Basic Stats ----------------
    amounts = [float(row[2]) for row in data]
    max_amount = max(amounts)
    min_amount = min(amounts)
    avg_amount = sum(amounts) / len(amounts)

    max_row = data[amounts.index(max_amount)]
    min_row = data[amounts.index(min_amount)]

    print(f"💹 Highest Expense: ₹{max_amount} | {max_row[1]} on {max_row[0]}")
    print(f"💹 Lowest Expense: ₹{min_amount} | {min_row[1]} on {min_row[0]}")
    print(f"💹 Average Expense: ₹{avg_amount:.2f}")

    # ---------------- Totals ----------------
    category_totals = defaultdict(float)
    monthly_totals = defaultdict(float)

    for row in data:
        category_totals[row[1]] += float(row[2])
        month_year = "-".join(row[0].split("-")[1:])  # MM-YYYY
        monthly_totals[month_year] += float(row[2])

    # ---------------- Ensure charts folder exists ----------------
    os.makedirs("reports/charts", exist_ok=True)

    # ---------------- Bar Chart ----------------
    categories = list(category_totals.keys())
    totals = list(category_totals.values())

    plt.figure(figsize=(10,6))
    plt.bar(categories, totals, color='skyblue')
    plt.title("Expenses by Category", fontsize=16)
    plt.xlabel("Category", fontsize=14)
    plt.ylabel("Total Amount", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.savefig("reports/charts/category_expenses.png", dpi=300)
    plt.close()

    # ---------------- Pie Chart ----------------
    plt.figure(figsize=(8,8))
    plt.pie(totals, labels=categories, autopct="%1.1f%%", startangle=90, textprops={'fontsize':12})
    plt.title("Expenses Distribution by Category", fontsize=16)
    plt.tight_layout()
    plt.savefig("reports/charts/category_pie.png", dpi=300)
    plt.close()

    # ---------------- Monthly Trend Line ----------------
    months = sorted(monthly_totals.keys())
    monthly_values = [monthly_totals[m] for m in months]

    plt.figure(figsize=(10,6))
    plt.plot(months, monthly_values, marker='o', color='green')
    plt.title("Monthly Expense Trend", fontsize=16)
    plt.xlabel("Month-Year", fontsize=14)
    plt.ylabel("Total Expenses", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.savefig("reports/charts/monthly_trend.png", dpi=300)
    plt.close()

    print("📊 Charts saved in reports/charts/")

# -------------------- Edit/Delete --------------------

def edit_expense():
    print_title("EDIT EXPENSE")
    data = load_expenses()
    if not data:
        print("No data to edit.")
        return

    view_expenses()
    try:
        index = int(input("Enter the number of expense to edit: ")) - 1
        if index < 0 or index >= len(data):
            print("❌ Invalid selection!")
            return
    except ValueError:
        print("❌ Invalid input!")
        return

    date = input(f"Enter new date (current: {data[index][0]}): ") or data[index][0]
    category = input(f"Enter new category (current: {data[index][1]}): ") or data[index][1]
    category = validate_category(category)
    if not category:
        print("❌ Invalid category!")
        return

    amount = input(f"Enter new amount (current: {data[index][2]}): ") or data[index][2]
    amount = validate_amount(amount)
    if amount is None:
        print("❌ Invalid amount!")
        return

    data[index] = [date, category, str(amount)]
    save_expense(data, overwrite=True)
    print("✔ Expense updated successfully!")

def delete_expense():
    print_title("DELETE EXPENSE")
    data = load_expenses()
    if not data:
        print("No data to delete.")
        return

    view_expenses()
    try:
        index = int(input("Enter the number of expense to delete: ")) - 1
        if index < 0 or index >= len(data):
            print("❌ Invalid selection!")
            return
    except ValueError:
        print("❌ Invalid input!")
        return

    confirm = input(f"Are you sure you want to delete expense {index+1}? (y/n): ")
    if confirm.lower() == 'y':
        data.pop(index)
        save_expense(data, overwrite=True)
        print("✔ Expense deleted successfully!")
    else:
        print("❌ Deletion cancelled!")
