name = input("Please enter your name ")
noun = input("Enter a noun ")
verb = input("Enter a verb ")
adjective = input("Enter an adjective ")


if len(name) <= 5:
    message = "Is your name is that short?"
else:
    message = "Good Nice name"

print(message)

print(f"On a {adjective} day, I went to the zoo. I saw a funny {noun} from the trees. Then, I spotted a majestic {name} lounging in the sun.  What a wild and {verb} experience! ")
