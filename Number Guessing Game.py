"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    # Display intro
    print("------------------------------------")
    print("Welcome to the Number Guessing Game.")
    print("------------------------------------")
    print("This is a number guessing game. There is no current high score.")
    score = 0
    while True:
        secret_number = random.randint(1,10)
        print("I am thinking of a number between 1 and 10.")
        guess_taken = 1
        while True:
            guess = input("Take a guess: ")
            try:
                if int(guess) == secret_number:
                    print("That's correct!")
                    print("It took you " + str(guess_taken) + " tries.")
                    if score == 0:
                        score = guess_taken
                    elif int(guess_taken) < score:
                        score = guess_taken
                    elif int(guess_taken) > score:
                        print("Sorry but you did not beat the high score.")
                    break
                elif int(guess) < 1 or int(guess) > 10:
                    print("Sorry but that is outside of the numbers I told you. Remember it is between 1 and 10. Try again.")
                elif int(guess) < secret_number:
                    print("That's not it. It is higher.")
                elif int(guess) > secret_number:
                    print("That's not it. It is lower.")
                else:
                    print("Please type in a number between 1 and 10.")
                guess_taken += 1
            except ValueError:
                print("Please type in a number between 1 and 10.")
            
        play_again = input("Would you like to play again? yes or no: ")
        if play_again.lower() == "yes":
            print("The current high score is " + str(score) + ".")
            continue
        elif play_again.lower() == "no":
            break
        else:
            print("I didn't understand what you typed so I'm going to end the game.")
            break

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
    print("Thanks for playing!")



















