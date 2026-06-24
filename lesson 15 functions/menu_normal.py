"""
PROGRAM: Menu
This starts with a menu so users can run 1 of 3 different programs:
1. wordle
2. magic 8 ball
3. 5 question quiz
"""

# INSTRUCTIONS
# TODO Copy over the code from 3 of your other programs into their own function.
# TODO If you have any imports, make sure to move them out of the function to IMPORTS section 
# (everything else can stay in the functions)
# TODO Create a menu program in the main function and call each program function based on user input

#===============================
# IMPORTS
#===============================
import random

#===============================
# FUNCTIONS
#===============================

# Run program 1
def play_wordle():
    words=["audio","hello","mafia","trick","fleas"]
    play=True
    # INTRODUCTION
    print("you are now playing wordle! How to play: guess a 5 letter word and you will see which letters are correct, incorrect or in the wrong place ")
    random_word=random.choice(words)
    # MAIN
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
            for i in range(5):
                if (user_guess[i])==(random_word[i]):
                    print(f"you got letter {i} correct")
                elif (user_guess[i]) in random_word:
                    print(f"letter {i} is in the wrong place")
                else:
                    print(f"letter {i} is not in the word")
            continue

        play_again=input("would you like to play again? ").strip().lower()
        while play_again!="yes" and play_again!="no":
            print("ERROR invalid answer. Please answer using yes or no")
            play_again=input("would you like to play again? ").strip().lower()
        if play_again=="no":
            play=False
        else:
            random_word=random.choice(words)

# Run program 2
def magic_8_ball():
    responses=['yes','no','maybe','most likely','probably not','definetely','ask again later','uncertain']
    while True:
        question=input("what yes or no question would you like to ask the magic 8 ball (or type quit to leave)\n").strip().lower()

        # Check if the user wants to exit and break from the loop if they do.
        if question=="quit":
            break
        # RANDOM REPSONSE
        print(responses[random.randint(0,7)])
    #end program
    print("program ended")

# Run program 3
def play_quiz():
    #valid answers
    valid=['a','b','c']
    #intro
    print()
    print("Welcome to the 5 question general knowledge quiz")
    print("When a question gives options a, b or c please use either a,b or c to answer")
    print("Good luck!")
    print()

    #scoring
    score= 0
    #instructions for if user can quit program
    #question 1 
    print("What is the fastest animal?\na: cheetah\nb: swordfish\nc: peregrine falcon")
    question_1= input("Your answer:").strip().lower()
    answer_1= "c"
    #while loop for invalid answer
    while not question_1 in valid:
        question_1=input("ERROR please answer using a, b or c\nYour answer: ")
    #check answer
    if question_1==answer_1:
        print("Correct!")
        score +=1
    else:
        print("Whoops that's incorrect, the correct answer was peregrine falcon (c)")
    print()

    #question 2
    print("What is acrophobia a fear of?\na: Spiders\nb: Hieghts\nc: Water")
    question_2=input("your answer:").strip().lower()
    answer_2="b"
    #while loop for invalid answer
    while not question_2 in valid:
        question_2=input("ERROR please answer using a, b or c\nYour answer: ")
    #check answer
    if question_2==answer_2:
        print("Correct!")
        score +=1
    else:
        print("whoops that's incorrect, the correct answer was hieghts (b)")
    print()

    #question 3
    print("What color is aureolin a shade of?\na: blue\nb: green\nc: yellow")
    question_3 = input("your answer:").strip().lower()
    answer_3 = "c"
    #if user wants to exit
    #while loop for invalid answer
    while not question_3 in valid:
        question_3=input("ERROR please answer using a, b or c\nYour answer: ")
    #check answer
    if question_3==answer_3:
        print("Correct!")
        score +=1
    else:
        print("whoops that's incorrect, the correct answer was yellow")
    print()

    #question 4
    question_4= input("What year was the video game 'Minecraft' officially released?\nyour answer:").strip().lower()
    answer_4= "2011"
    #check answer is valid
    try:
        question_4=int(question_4)
        question_4=str(question_4)
    except:
        print("please answer using numbers and no spaces")
        question_4=input("your answer: ").strip()
    #check answer
    if question_4==answer_4:
        print("Correct!")
        score +=1
    else:
        print("Whoops That's incorrect, the correct answer was 2011")
    print()

    #question 5
    question_5= input("how many time zones are there in the world?\nyour answer:").strip()
    answer_5= "24"
    try:
        question_5=int(question_5)
        question_5=str(question_5)
    except:
        print("please answer using numbers and no spaces")
        question_5=input("your answer: ").strip()
    #check answer
    if question_5==answer_5:
        print("Correct!")
        score +=1
    else:
        print("Whoops that's incorrect, the correct answer was 24")
    print()

    print(f"You got {score} out of 5 questions correct!")


# Run main code
def main():
    while True:
        user_choice=input("what program would you like to run\n1. wordle\n2. magic 8 ball\n3. 5 question quiz\n")
        try:
            user_choice=int(user_choice)
        except:
            print("ERROR invalid answer, please use the program's corresponding number")
            continue
        if user_choice==1:
            play_wordle()
        elif user_choice==2:
            magic_8_ball()
        elif user_choice==3:
            play_quiz()
        else:
            print("ERROR invalid answer, please use the program's corresponding number")
            continue
        play_again=input("would you like to use another program? ").strip().lower()
        if play_again=="yes":
            continue
        elif play_again=="no":
            break
        else:
            print("ERROR please answer with yes or no")
            play_again=input("would you like to use another program? ").strip().lower()
#===============================
# EXECUTION
#===============================

# Execute main code
main()

#===============================
#===============================
# EXTENSION
# TODO Go back to each program you chose and structure them with functions. 
# TODO Then recopy them over as multiple functions (rather than one)
# NOTE The main() function in your programs can be renamed as run_program_name() so it doesn't clash with this program's main()