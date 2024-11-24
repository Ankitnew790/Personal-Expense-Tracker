import json


def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r") as file:
            expenses = json.load(file)
            print("Expenses loaded successfully.")
    except FileNotFoundError:
     
        print("No saved expenses found. Starting fresh.")
        expenses = []
    return expenses


def set_budget():
    while True:
        try:
            budget = float(input("Enter your budget for the month: "))
            if budget < 0:
                print("Budget cannot be negative. Please enter a valid amount.")
            else:
                return budget
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def add_expense(expenses):
    name = input("Enter the name of the expense: ")
    try:
        amount = float(input("Enter the amount of the expense: "))
        category = input("Enter the category of the expense: ")
        expense = {
            "name": name,
            "amount": amount,
            "category": category
        }
        expenses.append(expense)
        print(f"Expense '{name}' added successfully.")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses to show.")
    else:
        print("\nExpenses:")
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense['name']} - ${expense['amount']} ({expense['category']})")


def track_budget(expenses, budget):
    total_expenses = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: ${total_expenses:.2f}")
    print(f"Budget: ${budget:.2f}")
    if total_expenses > budget:
        print("You have exceeded your budget!")
    else:
        print("You are within your budget!")


def save_expenses(expenses, filename="expenses.json"):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)
    print("Expenses saved successfully.")


def main():
    expenses = load_expenses()  # Load previous expenses
    budget = set_budget()       # Set the budget

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            track_budget(expenses, budget)
        elif choice == '4':
            save_expenses(expenses)
        elif choice == '5':
            save_expenses(expenses)
            print("Exiting...")
            break
        else:
            print("Invalid choice, please select a valid option.")


if __name__ == "__main__":
    main()