# j = "jesse"


# def test():
#     j = "Issac"
#     print(j)


# test()

# print(j)


# def test_one():
#     count = 5
#     print(count)


# def test():
#     count = 60
#     print(count)


# test_one()
# test()


x = "Jesses"


def tests_outer():
    x = "Issac"

    def tests_inner():
        x = "Jesse"
        print(x)  # prints x local inner
    tests_inner()

    print(x)  # prints x  local outer

tests_outer()

print(x) #prints global
