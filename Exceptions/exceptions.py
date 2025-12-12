"""
Errors happens normally
Types of Errors
SYntax errors -  code not valid .Not valid python Caught before running
Ezeptions- runtime errors (runtime error) - problem which occurs while program runs
"""


try:
    x = int(input("Enter a number: "))
    results = 10 / x
    print(results)

except ValueError:
    print("That is not a valid integer")
except ZeroDivisionError:
    print("Cannot divide the function by zero")


# to catch multiple errors at once
except (ValueError, ZeroDivisionError):
    print("Invalid Number")

# to catch all exception
except Exception:
    print("Someting happened")
finally:
    print("This runs no matter what ")  # Normally for cleaning up resources
