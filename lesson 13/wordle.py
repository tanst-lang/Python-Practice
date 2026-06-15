# =====================================================================
# PROJECT: Wordle
# Create a program where the user must guess the 5 letter word.
# =====================================================================

# TOOLS
# TODO Import random so you can randomise the word
import random
# VALUES
# TODO Create a list of at least 5 different 5-letter words
words=["audio","hello","mafia","trick","fleas"]
# TODO Create a variable called play and set it to True
play=True
# INTRODUCTION
# TODO Tell your user how to play wordle (make sure they know they must input 5 letter words)
random_word=random.choice(words)
# MAIN
# TODO Create a while loop that runs if play is true
while play==True:

    # USER INPUT
    user_guess=input("your guess: ")
    # while loop if the guess is not 5 characters long
    while len(user_guess)!=len(random_word):
        user_guess=input("ERROR word needs to be 5 letters. Guess again: ")
    #if they got it correct
    if user_guess==random_word:
        print("congatulations you guessed correctly!")
    else:
        # TODO Create a for loop that loops 5 times
        for i in range(5):
            # TODO Check if the current letter of user_input (user_input[i]) is the same as the i letter of the word and if it is tell them they got that letter correct
            if (user_guess[i])==(random_word[i]):
                print(f"you got letter {i} correct")
            # TODO Otherwise check if the current letter of user_input is in the word and if it is, tell them that letter is in the wrong position
            elif (user_guess[i]) in random_word:
                print(f"letter {i} is in the wrong place")
            # TODO Else tell them that letter is wrong
            else:
                print(f"letter {i} is not in the word")
        continue
# TODO Ask if they want to play again. If they don't, set play to false.

    play_again=input("would you like to play again? ").strip().lower()
    while play_again!="yes" and play_again!="no":
        print("ERROR invalid answer. Please answer using yes or no")
        play_again=input("would you like to play again? ").strip().lower()
    if play_again=="no":
        play=False
    else:
        random_word=random.choice(words)

# ==========================================================
# EXTENSION
# Instead of telling the user one by one about their letters, put each correct letter and _ for a wrong letter into a list. 
# Then finally print the list (you can use "".join(list_name) to merge them into a string if you like)

# ==========================================================
# EXPERT
# Following on from the extension, add colour to the letters instead (Don't use _ for incorrect anymore). Green for correct, orange for wrong place, red for incorrect. You'll need to add the colour as you add them to the list

# print("\033[31mThis is Red Text\033[0m")
# print("\033[38;2;255;165;0mThis is Orange Text\033[0m")
# print("\033[32mThis is Green Text\033[0m")

# Further Extension: Structure with user defined functions