# IMPORTS
# Import the 'random' module so you can generate a secret number.
import random
# VARIABLES
#Generate a random number between 1 and 100 and save it to 'secret_number'.
SECRET_NUMBER=random.randint(1,100)

#variable to keep track of the user's current guess.
guess="0"
guess_times=0

# INTRODUCE THE GAME
print("this is a super fun game where you try guess the number between 1 and 100 that the computer chose")

# START THE GAME
guess=int(input("guess the number: "))
guess_times+=1

# 'while' loop that keeps running AS LONG AS the user's guess is incorrect
while guess!=SECRET_NUMBER:
    print()
    #'if' statement to check if their guess is TOO LOW.
    if guess<SECRET_NUMBER:
        print("too low! Try a higher number")

    # 'elif' statement to check if their guess is TOO HIGH.
    elif guess>SECRET_NUMBER:
        print("too high! Try a lower number")      

    guess=int(input("Guess again: "))
    guess_times+=1

# GAME OVER / WINNING MESSAGE
# victory message 
print()
print(f"congradulations you guessed the number in {str(guess_times)} guesses!")