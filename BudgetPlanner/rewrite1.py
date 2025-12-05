def get_valid_number(prompt):
    while True:
        value = input(prompt)
        if value.replace(".", "", 1).isdigit():
            return float(value)
        print("Please enter a valid number")


def get_user_details():
    name = input("Please Enter your name: ").strip().upper()
    income = get_valid_number("Enter your monthly income: GHS  ")
    return name, income


def get_user_expense():
    expense_category = ["Transport", "Gifts", "Food", "Entertainement"]
    expense = {}

    for category in expense_category:
        expense[category] = get_valid_number(
            f"Please enter your {category} expense: GHS")
    return expense


def calculate_expense(income, expense):
    expenses = sum(expense.values())
    balance = income - expenses
    savings_ratio = (balance / income) * 100 if expenses > 0 else 0
    return expenses, balance, savings_ratio


def show_summary(name, income, expenses, balance, savings_ratio):
    print(f"===BBUDGET SUMMARY FOR {name.upper()}====")
    print(f"Your income is {income:.2f}GHS")
    print(f"Your expense summary is {expenses:.2f} GHS ")
    print(f"Your balance is {balance:.2f} GHS")
    print(f"Your savings ratio is {savings_ratio:.2f}%")
    if savings_ratio < 20:
        print("You are fairly saving, try cutting down expense")
    elif savings_ratio < 35:
        print("Your doing well but can keep it up")
    else:
        print("Great Job keep it up")


def show_expense_breakdown(expense, expenses):
    choice = input(
        "\n Would you like to see a breakdown of your espense: ").strip().lower()
    if choice == "yes":
        total = sum(expense.values())
        print("\n Expense Breakdown :  ")
        for category, amount in expense.items():
            percent = (amount / total) * 100
            print(f"{category}: {amount:.2f} ({percent:2f}%)")


def main():
    name, income = get_user_details()
    expense = get_user_expense()
    expenses, balance, savings_ratio = calculate_expense(
        income, expense)
    show_summary(name, income, expenses, balance, savings_ratio)
    show_expense_breakdown(expense, expense)

    print("Thank you for using Personal Budget Tracker")


main()
