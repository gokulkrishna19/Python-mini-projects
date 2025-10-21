
def add_expense(expenses, category, amount):
    """Add a new expense entry."""
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

def show_expenses(expenses):
    """Display all expenses."""
    print("\n=== Expense Summary ===")
    total = 0
    for category, amount in expenses.items():
        print(f"{category}: ₹{amount:.2f}")
        total += amount
    print(f"------------------\nTotal: ₹{total:.2f}")

def main():
    expenses = {}
    print("💰 Simple Expense Tracker 💰")

    while True:
        print("\n1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category (e.g., Food, Travel, Bills): ")
            amount = float(input("Enter amount: ₹"))
            add_expense(expenses, category, amount)
            print("✅ Expense added!")
        elif choice == "2":
            show_expenses(expenses)
