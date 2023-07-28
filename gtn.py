from art import gtn_logo
from random import randint


print(gtn_logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = randint(1, 100)
# print(f"Pssst, the correct answer is {number}")


difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    lives = 10
else:
    lives = 5


def check_guess(guess):
    if guess == number:
        print(f"You got it! The answer was {number}.")
        return True
    elif guess > number:
        print("Too high.")
        return False
    else:
        print("Too low.")
        return False


while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if check_guess(guess):
        break
    lives -= 1
    if lives == 0:
        print("You've run out of guesses, you lose.")
    else:
        print("Guess again.")
