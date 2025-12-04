x = "global x"


def outer():
    x = "outer_x"  # local to outer

    def inner():
        x = "inner_x" # local to inner
        print(x) # prints local x according to LEGB  FOR INNER FUNCTION
    inner()
    print(x) #prints local function for outer function(check identation)

outer()


print(x)
