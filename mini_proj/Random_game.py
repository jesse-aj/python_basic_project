import random

play = True

while play:
    secret_number = random.randint(1, 10)
    count = 1

    guess = int(input("I am thinking  of a number, Can you guess it? (1-10) "))

    while guess != secret_number:
        match guess:
            case _ if guess < secret_number:
                print("Nope your guess is a bit low.Give it another try ")
            case _ if guess > secret_number:
                print("Opps, your guess is a bit high. Try again ")

        count += 1
        guess = int(input("Try again "))

    print(f"Congratulations you are correct and guessed it {count} of times!")

    play_again = input("Do you want to play again (yes or no) ").lower()
    if play_again == "no":
        play = False
