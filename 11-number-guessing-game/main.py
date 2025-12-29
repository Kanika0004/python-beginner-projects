import random
import art

def guess_num_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    num=random.randint(1,100)
    print(num)
    lvl=input("Choose a difficulty. Type 'easy' or 'hard':")
    no_guess=0
    if lvl=="easy":
        no_guess=10
    else :
        no_guess=5
    while no_guess :
        print(f"You have {no_guess} attempts remaining to guess the number.")
        guess=int(input("Make a guess:"))
        if guess==num :
            print(f"You got it! The answer was {num}.")
            return
        elif guess > num :
            print("Too high.\nGuess again.")
            no_guess=no_guess-1
        else :
            print("Too low.\nGuess again.")
            no_guess = no_guess - 1
    print("You've run out of guesses. Refresh the page to run again.")
guess_num_game()