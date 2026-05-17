### WHAT ANIMAL ARE YOU QUIZ ###

# FIRST, create a basic Flowchart using the FLowchart Shapes to plan the flow of your 'what animal are you' quiz. 
# __________________________

# Write a 'what animal are you' quiz. 
# You can base this on the picture from last lesson, but make it simpler - 
# 3 questions and 4 animals.


# Ask your user a question about themselves, giving them 2 options
qestion_1= input("are you more of a morning or night person?\na: morning\nb: night\na or b: ")
# Check if they picked the first option
if qestion_1=="b":
    # Ask the next question
    question_1_2= input("are you more quiet or curious?\na: quiet\nb: curious\na or b:")
    # Check if they picked the first option
    if question_1_2=="a":
        # Tell them they're animal 1
        print("you are a greater glider!")
    # Otherwise
    else:
        print("you are a platypus!")
        # Tell them they're animal 2

# Otherwise
else:
    qestion_2=input("would you rather chat with people or have an adventure\na: chat\nb: adventure\na or b:")

    if qestion_2=="a":
        print("you are a swift parrot!")
    # Otherwise
    else:
        print("you are a wallaby!")


# __________________________

# EXTENSION
# Extend the quiz so there are 8 possible animals
# Create a Flowchart using the FLowchart Shapes to 

# __________________________

# EXTENSION 2
# Create a 'Which ??? are you?' Quiz
# This time allow all questions to have 4 possible answers (a,b,c and d) 
# and tally how many times they choose each
# Determine what they are at the end using the letter with the highest tally.
# Eg. If they picked mostly As, maybe they are Pikachu.