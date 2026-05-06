# Create a calculator that asks the user for a number (of days)
# and outputs how many seconds in that number of days

# Values - start by writing constants to hold:
# The number of seconds in a minute
seconds= 60
# The number of minutes in an hour
minutes=60
# The number of hours in a day
hours=24

# Get input from the user and save it in a variable
days=int(input("days:"))


# Calculate the number of seconds using * with the input and your constants.
seconds_in_days= days*hours*minutes*seconds 
# Save it in a new variable.
print("seconds in",days,"days=",seconds_in_days)
# Output the answer

# ---------------------------------

# EXTENSION
# Also output how many total hours and how many total minutes in the days
# Create another calculator that does the opposite (input is seconds, output is days)

# ---------------------------------

# EXPERT (for those who already know some Python)
# Create the calculator above, but...
#   allow your user to choose the input and output type (seconds, minutes, hours, days)
#   Loop the calculator so they can do it again with having to reopen the program.