#Import the 'random' module
import random


# Create a list 
responses=['yes','no','maybe','most likely','probably not','definetely','ask again later','uncertain']

# MAIN LOOP
while True:
    question=input("what yes or no question would you like to ask the magic 8 ball (or type quit to leave)\n").strip().lower()

    # Check if the user wants to exit and break from the loop if they do.
    if question=="quit":
        break
    # RANDOM REPSONSE
    print(responses[random.randint(0,7)])
#end program
print("program ended")
