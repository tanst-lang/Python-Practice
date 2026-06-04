### Budget Tracker ###
# Create a budget tracker that gives financial recommendation around an item

# Create a constant to hold your budget
budget=250
# Create a constant to hold your savings (percentage) goal
savings=500

# Ask user for item name and save in variable
item=input("what item do you want to buy?\n")
# Ask user for cost and save in variable
cost=input("what is the price of "+str(item)+"?\n")
# Change the cost into an integer
cost=int(cost)
# Calculate the percentage of budget (cost / budget) * 100
percent=(cost/budget)*100
# Tell your user the percentage of your budget
print(str(item)+" will be "+str(percent)+"%"+" of your budget")
# Check if percentage is 0 and say it's free if it is
if percent==0:
    print(f"it is 0% so it is free!")
# Check if the percentage is less then 10 and say it's a small treat so enjoy
elif percent<10:
    print("it is a small treat so enjoy")
# Check if it is less than 50 percent and if it is tell them it's a major spend and should sleep on it
elif percent<50:
    print("This would be a major spend, you should sleep on it")
# Check if it's over 100 and if it is tell them they don't have enough money
elif percent>100:
    print("This costs more than you have so you can't afford it")
# Otherwise, tell them it costs way too much and isn't worth it
else:
    print("the cost is too much, it isn't worth it")
# _______________________

# EXTENSION
# Include an item type question and change answers based on this. 
# Eg. food shouldn't cost as much as a bill so if it's a food, 
# tell them to not buy it at a lower percentage


# _______________________

# EXPERT
# Try to create a budget tracker that saves data in a file 
# so the remaining_budget can be updated every time the program is used
# You will need to create a save.txt file to go with this (keep it in the same folder)
# If you're not sure how to do this check here: https://www.w3schools.com/python/python_file_write.asp 