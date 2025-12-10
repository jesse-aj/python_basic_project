num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))


try:
    results = num1/num2
except ZeroDivisionError:
    print("Cannot divide by zero")
