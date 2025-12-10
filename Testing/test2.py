def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiple(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y