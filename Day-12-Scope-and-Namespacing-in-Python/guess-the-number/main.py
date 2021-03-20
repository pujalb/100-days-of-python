import art
import random
from replit import clear

HARD = 5
EASY = 10

def play_game():

    # Welcome message
    print(art.logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    # Difficulty level
    difficulty_level = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
    no_of_attempts = EASY if difficulty_level == "easy" else HARD
    
    print(f"\nYou have {no_of_attempts} attempts remaining to guess the number.")

    # Number to be guessed between 1 and 100
    answer = random.randint(1, 101)
    #print(answer)

    while (no_of_attempts > 0):
        # Re-prompt until input is of type int
        while True:
            try:
                guess = int(input("\nMake a guess: "))
                break
            except:
                print("Input an interger between 1 and 100")
                print(f"You have only {no_of_attempts} attempts remaining to guess the number.\nGuess Again!")
        # Check answer
        if guess == answer:
            print(art.win)
            print(f"You got it. The answer was {answer}")
            break 
               
        elif guess < answer:
            print("Too Low!")
            no_of_attempts -= 1

            if no_of_attempts > 0:
                print(f"You have only {no_of_attempts} attempts remaining to guess the number.\nGuess Again!")
            else:
                print("You've run out of guesses, you lose.")
                print(art.lose)

        elif guess > answer:
            print("Too High!")
            no_of_attempts -= 1

            if no_of_attempts > 0:
                print(f"You have only {no_of_attempts} attempts remaining to guess the number.\nGuess Again!")
            else:
                print("You've run out of guesses, you lose.")
                print(art.lose)

    restart = input("\nType 'Y' to restart the game, or type 'N' to exit: ").lower()
    if restart == 'y':
        clear()
        play_game()

play_game()