set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a.union(set_b))

print(set_a.intersection(set_b))

print(set_a.difference(set_b))

print(set_b.difference(set_a))

set_e = 10

print(set_e in set_a)

# Order doesnt matter

x = {12, 76, 66}
y = {66, 76, 12}

print(x == y)


range_numbers = range(1, 11)
range_set = set(range_numbers)
print(range_set)

list_numbers = [1, 12, 13, 11, 1, 12]
list_set = set(list_numbers)
print(list_set)