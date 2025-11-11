"""

1. START
2. DISPLAY A WECOME MESSAGE
3. TELL USER TO ENTER NAME
2. TELL THE USER TO INPUT AGE IN YEARS
3.CALCULATE AGE IN MONTHS
4.CALCULATE AGE IN DAYS
5. DISPLAY AGE AND IN MONTHS AND IN DAYS
6. END
"""
print (" == WELCOME TO AGE CALCULATOR == ")
name = input("Enter your name ")
age = int(input("Enter age in years "))
 

age_months = age * 12
age_days = age * 365

print(f"\n AGE CALCULATOR FOR {name}")
print(f"{age}years is {age_months} in months")
print(f"{age}years is {age_days} in days")