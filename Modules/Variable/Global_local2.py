x = "global x"  # global


def test():
    x = "local_x"  # global x will not be ovewritten
    print(x)


test()  # runs the test function and prints local x

print(x)  # prints global x
