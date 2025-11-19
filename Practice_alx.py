# name = input("Please enter your name ")
# noun = input("Enter a noun ")
# verb = input("Enter a verb ")
# adjective = input("Enter an adjective ")


# if len(name) <= 5:
#     message = "Brroo your name is that short?"
# else:
#     message= "Good Nice one"

# print(message)


# print("On a " + adjective + " day, I went to the zoo. I saw a funny " + noun + " from the trees. Then, I spotted a majestic " + name + " lounging in the sun.  What a wild and " + adjective + " experience! ")

day = input("Enter a day of the week (Monday - Sunday) ").lower()

match day:
    case("monday"):
        print("Ugh.....Mondays")
    case("tuesday"):
        print("Another Working Day")
    case("wednessaday"):
        print("Hump day")
    case("thursday"):
        print("Almost there")
    case("friday"):
        print("TGIF")
    case("saturday | Sunday"):
        print("Weekend Vibes")
    case _:
        print("Invalid day entered")
