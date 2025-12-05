
x = "global"


def outer():
    x = "outer_x"  # local to outer

    def inner():
        # nonlocal x # to change the variable of our outer function
        x = "inner_x"  # local to inner
        print(x)  # prints local x according to LEGB  FOR INNER FUNCTION
    inner()
    print(x)  # prints local function for outer function(check identation)


outer()

print(x)
