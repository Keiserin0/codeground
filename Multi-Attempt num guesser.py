import random

number = random.randrange(1, 10)
user_guess = int(input("Guess a number from 1 - 10: "))


while number != user_guess:
    if user_guess < number:
        print("Your guess is too small")
        user_guess = int(input("Guess a number from 1 - 10: "))

    elif user_guess > number:
        print("Your guess is too big")
        user_guess = int(input("Guess a number from 1 - 10: "))

    else:
        break

print("You got it!")