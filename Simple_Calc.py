num1 = int(input("Please enter your first number "))
num2 = int(input("Please enter your second Numer "))
operator = input("Please enter an Operator(+, -, *, /) ")

match operator :
    case "+":
        print(f"Results = {num1 + num2}")
    case "-":
        print(f"Results = {num1 - num2}")
    case "*":
        print(f"Results = {num1 * num2}")
    case "/" if num2 != 0:
        print(f"Results = {num1 / num2}")
    case "/" if num2 == 0:
        print("Cannot divide by Zero")
    case _:
        print("Invalid Operator")
