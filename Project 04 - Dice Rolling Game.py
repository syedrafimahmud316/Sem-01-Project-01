# Make a game where a dice will provide a random number from 1 to 6 upon rolling.

import random

while True:
    choice = input("Roll a dice? (y/n): ").lower()

    if choice == "n":
        print("Thanks for playing the game!")
        break
    elif choice == "y":
        print(f"{(random.randint(1,6))}")     # randint = random + integer. It's like math.pi .
    else:
        print("Invalid input.")
