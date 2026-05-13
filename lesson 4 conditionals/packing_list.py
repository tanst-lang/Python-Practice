### Create a packing checklist based on input

# Tell the user what this program is about
print("this program will help make a packing list for where you want to go")
# Ask the user for the current temperature and save it
temp=input("what is the average tempature of the destination you plan to visit?\n")
# Change the temperature input into an integer
temp= int(temp)
# If the temperature is below 15, tell them to pack a jacket
if temp<15:
    print("that's below 15 degrees, you should bring a jacket")
# If the temperature is above 15, tell them to pack sunscreen
if temp>=15:
    print("over 15 degrees means it will be sunny, be sure to pack sunscreen")
# Ask the user their destination (beach or mountains)
destination=input("is your destination in the mountains or the beach?\n")
# If beach, tell them to pack a towel
if str(destination)=='beach':
    print("since you're going to the beach you should pack a towel")
# If mountains, tell them to pack hiking boots
if str(destination)=='mountains':
    print("walking in the mountains can be tricky, be sure to bring hiking boots")
# ___________________________

# EXTENSION

# Add some more conditions (eg. one day or overnight? solo or with others?)

# ____________________________

# EXPERT (for those who already know Python)

# Create a packing checklist (start with something similar to the main program) then 
# display all items to pack with a X or O for packed or not. 
# Allow the user to select an item to change its status.