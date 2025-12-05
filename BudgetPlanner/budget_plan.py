"""
PERSONAL BUDGET SUMMARY

1.Start
2.Display a welcome message 
3.Ask user to enter name and work type
4.Ask user to enter income
5.Ask the user to enter their expense
 -Transport
 -Airtime
 -Food
 -Gifts
6.Calculate total expense
7.Calculate the remaining balance
8.Display the savings ratio
9.Display 
-user name with welcome message
-Total income
-Total expense
-Total remaining balance
-savings ration
10.End
"""


print("=== PERSONAL BUDGET PLANNER ===")


def get_valid_number(prompt):
    while True:
        value = input(prompt)

        if value.replace(".", "", 1).isdigit():
            return float(value)
        else:
            print("Enter a valid number for monthly income")


def get_user_details():
    name = input("Please Enter your name ")
    income = get_valid_number("Enter your monthly salary: GHS")
    return name, income


def get_expenses():
    expense_categories = ["Transport", "Food", "Gifts", "Entertainment"]
    expenses = {}

    for category in expense_categories:
        expenses[category] = get_valid_number(
            f"Enter your {category} expense: GHS")
    return expenses


def calculate_budget(income, expenses):
    expenses = sum(expenses.values())
    balance = income - expenses
    savings_ratio = (balance / income) * 100 if income > 0 else 0

    return expenses, balance, savings_ratio


def display_summary(name, income, expenses, balance, savings_ratio):
    print(f"\n === PERSONAL BUDGET FOR {name.upper()} ===")
    print(f"Your total monthly income is {income:.2f} GHS")
    print(f"Your total monthly expense is {expenses:.2f} GHS")
    print(f"Your total balance is {balance:.2f} GHS")
    print(f"Your Savings ratio is {savings_ratio:.2f}%")

    if savings_ratio < 10:
        print("You are saving too low! Try reducing your expnses")
    elif savings_ratio < 30:
        print("You're saving fairly! Keep improving")
    else:
        print("Great job! You are saving well")


def show_expense_breakdown(expenses):
    choice = input(
        "\n Would you like to see a breakdown of your expense? (yes/no)").strip().lower()
    if choice == "yes":
        total = sum(expenses.values())
        print("\n Expense Breakdown: ")
        for category, amount in expenses.items():
            percent = (amount / total) * 100
            print(f"{category}: ${amount:.2f}    ({percent:.2f}%)")


def main():
    name, income = get_user_details()
    expense = get_expenses()
    expenses, balance, savings_ratio = calculate_budget(
        income, expense)
    display_summary(name, income, expenses, balance, savings_ratio)
    show_expense_breakdown(expense)
    print("Thank you for using the personal budget tool")


main()
