rows = int(input("Enter the number of rows: "))
current_rows = 1
while current_rows <= rows:
    # print spaces
    space_counter = rows - current_rows
    while space_counter > 0:
        print(" ", end="")
        space_counter -= 1
    # print star
    star_counter = (current_rows * 2 - 1)
    while star_counter > 0:
        print("*", end="")
        star_counter -= 1

    print()
    current_rows += 1
