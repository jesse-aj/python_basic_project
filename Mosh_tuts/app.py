# # Variables stores data eg.
# students_counts = 1000  # students_count is a variable and can be used anywhere in code
# # eg.
# print(students_counts)

# # PRIMITIVE DATA TYPES
# # 1.Boleans 2.Integer or float 3.String

# students_count = 1000  # integer
# rating = 4.99  # float
# is_published = False  # Bolean
# # Python is case Sensitive
# course_name = "Python Programming"  # String

# # Always use descriptive and meaningful names for variables
# # Always use lower case to name variables
# # you can use underscores to make variables readable
# # Space must be around equal to (code must be formatted properly)

# ### STRINGS###
# course = "Python Programming"
# # To display a long string of text you can use tripple quotes eg.
# message = """
# This is  Jesse from BD bussinesses

# i am a billionaire blah blah blah

# """


# # To get a lenght of strings
# len(course)
# print(len(course))

# # To get access to a particular string or set of  eg. Use indexes
# course[0]
# print(course[-1])
# print(course[0:3])  # Returns the first 3 characters (slicing)

# # \" is an escape elememt
# # \'
# # \n is used as a new line

# first = "Jesse"
# last = "Appiah"
# # f allows to use variables and create expresions in expressions itself
# full = f"{first} {last}"
# print(full)

# # STRINGS METHODS
# print(course.upper())  # This format course to upper case
# print(course.lower())  # This formats course to lower case
# print(course.title())  # This formats the first letter to captal
# print(course.strip())  # This allows to trim white  spaces in text or strings
# print(course.lstrip())  # left trip
# print(course.rstrip())  # right strip
# print(course.find("pro"))  # index or sequence of a string (returns an index)
# # To replace something
# # check existense of character data or variable (returns a boolean)
# print("pro" in course)
# print("swift" not in course)  # opposite of in

# # NUMBERS
# print(round(2.9))  # For rounding a number
# print(abs(-23.5))  # returns absolute

# # TYPE CONVERSION
# x = input(" x:")


# temperature = 345

# if temperature > 30:
#     print("Fool")
#     print("Big fool")


# score = int(input("Please enter your score?"))

# if score >= 80:
#     grade = "A"
# elif score >= 60:
#     grade = "B"
# elif score >= 40:
#     grade = "C"
# else:
#     grade = "F"

# print("Your grade is:", grade)


# high_income = True
# good_credit = True
# student = True

# if (high_income or good_credit) and not student:
#     print("You are eligible for a loan")
# else:
#     print("Not Eligible")


# age = 45
# if 18 <= age < 65:
#     message = "You are grown ass man stop fooling around"
# else:
#     message = "Continue to fool"

# print("You can and are", message)

# house_addresses = ["Race Course", "Apremedo", "Kwesimintsin"]

# address_found = False
# while not address_found:
#     address = input("Please Enter your home Address  (Enter q to quit) ")
#     if address.lower() == "q":
#         break
#     if address in house_addresses:
#         address_found = True
#         print(f"{address} is found")
#     else:
#         print(f"{address} is not found")
# counter = 1
# while counter <= 5:
#     print("Jesse", end="")
#     s_count = 1
#     while s_count <= 4:
#         print("will make it", end="")
#         s_count += 1

#     counter = counter + 1
#     print()


# repe_count = 0
# while repe_count < 4:
#     number = 1
#     while number <= 100:
#         if number % 3 == 0 and number % 5 == 0:
#             print(number, end=" ")
#         number = number + 1

#     print()

#     repe_count = repe_count + 1

# counter_count = 11

# while counter_count > 0:
#     inner_count = 1
#     while inner_count <= counter_count:
#         print(inner_count, end="")
#         inner_count += 1
#     print()
#     counter_count -= 1


# for i in range(1, 11):
#     for j in range(1, 11):
#         product = i * j
#         print(f"{i} * {j} is {product}", end="\t")
#     print()

# rows = 5

# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()


