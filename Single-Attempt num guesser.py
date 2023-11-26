import random

number = random.randrange(1, 10)
user_guess = int(input("Guess a number from 1 - 10: "))

if number == user_guess:
    print("You got it right!")

else:
    print(f"The right answer is {number}. Try again next time.")

