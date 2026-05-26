# Create a roller coaster access screener (determine if the user is allowed to ride)
# Rules:    They must be over 150cm and over 10 years old
#           They must not have a heart condition
#           OR they can ride if they have a VIP pass

# Get input
height=int(input("enter height in cm: "))
age=int(input("enter age: "))
heart=input("do you have any heart conditions? ").strip().lower()
vip=input("do you have a vip pass? ").strip().lower()


# Check conditions and output verdict
if height>150 and age>10 and heart=="no":
    print("you are able to ride the roller coaster")
elif vip=="yes":
    print("you are able to ride the roller coaster")
else:
    print("you are unable to ride the roller coaster")

# ------------------------------
# EXTENSION
# Change your screener to work for 3 different rides (ask user which ride at the beginning) with different rules

# ------------------------------
# EXPERT
# Follow the same task (with extension), but use dictionaries to make the code more efficient