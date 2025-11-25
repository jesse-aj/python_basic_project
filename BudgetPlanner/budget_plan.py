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

# Step 1
name = input("Please Enter your name  ")

# step 2
valid = False
while not valid:
    total_income = (input("Enter your monthly salary: GHS"))
    if total_income.replace(".", "", 1).isdigit():
        total_income = float(total_income)
        valid = True
    else:
        print("Enter a valid number for monthly income")


valid = False
while not valid:
    transport = input("Enter the amount you spend on transport: GHS")
    if transport.replace(".", "", 1).isdigit():
        transport = float(transport)
        valid = True
    else:
        print("Please Enter a valid number for transport ")

valid = False
while not valid:
    food = input("Enter the amount you spend on food: GHS")
    if food.replace(".", "", 1).isdigit():
        food = float(food)
        valid = True
    else:
        print("Please enter a correct value for food")

valid = False
while not valid:
    gifts = input("Enter the amount you spend on gift GHS")
    if gifts.replace(".", "", 1).isdigit():
        gifts = float(gifts)
        valid = True
    else:
        print("Enter a correct value for gifts")


valid = False
while not valid:
    entertainment = input("Enter the amount you spend on entertainment")
    if entertainment.replace(".", "", 1).isdigit():
        entertainment = float(entertainment)
        valid = True
    else:
        print("Enter a valid number for entertainment")

# step 3
expense = transport + food + gifts + entertainment
balance = total_income - expense
if total_income > 0:
    savings_ratio = (balance / total_income) * 100
else:
    savings_ratio = 0

# step 4
print(f"\n === PERSONAL BUDGET FOR {name.upper()} ===")
print(f"Your total monthly income is {total_income:.2f} GHS")
print(f"Your total monthly expense is {expense:.2f} GHS")
print(f"Your total balance is {balance:.2f} GHS")
print(f"Your Savings ratio is {savings_ratio:.2f}%")

# step 5
if savings_ratio < 10:
    print("You are saving too low! Try reducing your expnses")
elif savings_ratio < 30:
    print("You're saving fairly! Keep improving")
else:
    print("Great job! You are saving well")

# step 6
choice = input(
    "\n Would you like to see a breakdown of your expense? (yes/no)").strip().lower()
if choice == "yes":
    categories = ("transport", "food", "gifts", "entertainment")
    values = [transport, food, gifts, entertainment]
    total = expense

    print("\n Expense Breakdown: ")
    i = 0
    while i < len(categories):
        percent = (values[i] / total) * 100
        print(f"{categories[i]} : GHS{values[i]:.2f} {percent:.2f}%")
        i += 1


print("Thank you for using the personal budget tool")
