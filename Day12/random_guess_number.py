import random

import art

EASY_TURN = 10
HARD_TURN= 5

def play(random_guess_check, turn):
    left_attempt = turn
    while left_attempt > 0:
        your_guess = int(input("Make a guess:"))
        if your_guess == random_guess_check:
            print(f"You got it! The answer was {your_guess}.")
            return
        elif your_guess < random_guess_check:
            print("Guess too low \nGuess again")
        else:
            print("Guess too high \nGuess again ")
        left_attempt -= 1
        if left_attempt >0:
            print(f"You have {left_attempt} attempts remaining to guess the number.")
        else:
            print(f"You've run out of guesses. The guess value is {random_guess_check}")


def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of number between 1 and 100.")
    random_guess = random.randint(1, 100)
    # print(random_guess)
    set_difficulty(random_guess)

def set_difficulty(random_guess):
    your_choice =input("Choose a difficulty. Type 'easy' or 'hard': ")
    if your_choice == "easy":
        play(random_guess,EASY_TURN)
    else:
        play(random_guess,HARD_TURN)

game()
