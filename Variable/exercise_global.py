x = "Ronard"


def tests_outer():
    x = "Issac"

    def tests_inner():
        x = "Jesse"
        print(x)  # prints x local inner
    tests_inner()

    print(x)  # prints x  local outer

tests_outer()

print(x) #prints global