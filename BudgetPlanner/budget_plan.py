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
#step 2
print ("=== PERSONAL BUDGET PLANNER ===")
 
#Step 3 
name = input("Please Enter your name  ")

#step 4
total_income = float(input("Enter your monthly salary "))

#step 5
transport = float(input("Enter your transport "))
food = float(input("Enter the amount you spend on food "))
gifts = float(input("Enter the amount you spend on gift "))

expense = total_income + food + gifts 
balance = total_income - expense
savings_ratio = ( balance / total_income) * 100

print(f"\n === PERSONAL BUDGET FOR {name} ===")
print(f"Your total monthly income is {total_income:.2f} $")
print(f"Your total monthly expense is {expense:.2f} $")
print(f"Your total balance is {balance:.2f} $")
print(f"Your Savings ratio is {savings_ratio:.2f} $")


