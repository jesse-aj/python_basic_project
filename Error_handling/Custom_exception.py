class ValueTooHighError(Exception):
    pass

num = int(input("Please Enter a number: "))

if num > 100:
    raise ValueTooHighError("The Value is too high")


print("Number Accepted")
