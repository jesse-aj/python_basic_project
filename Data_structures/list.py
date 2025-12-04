my_list = [10, 20, 30, 40, 50, "apple", "apple"]
iterable = [12, 14, 16, 182, 400]
my_list[0]
(my_list[::-1])  # slicing reverse
(my_list[::2])  # slicing (two two intwervals)
(my_list[1:4])  # slicing from index to index

my_list.append(60)  # add a value to lists
my_list.append(30)  # add value to lists
my_list.remove(30)  # remove value from lists

my_list.extend(iterable)  # adds another iterable or list to the current list
my_list.insert(0, 33)  # appends or change vaalue at a given index
my_list.pop()  # removes the last element
my_list.count("apple")

# print(my_list)

fav_fruits = ["apple", "banana", "orange", "pineapple"]
print(fav_fruits[1])
