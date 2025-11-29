def my_var_sum(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


sum = my_var_sum(123, 152, 3627, 773)
print(f"The sum is {sum}")
