# =====================================================================
# PROGRAM: Safe Cracker (The Digital Vault)
# =====================================================================

# SETUP YOUR VARIABLES
# TODO: Create a variable for the correct vault combination (e.g., "742").
SAFE=268
# TODO: Create a variable to keep track of how many attempts the player has used (start at 0).
atempts=0

# INTRODUCE THE GAME

print("you are trying to crack a safe by guessing the 3 digit code to unlock it")
print("By typing exit for your guess you will exit the experience")

# LOOP
while True:
    user_input=input("Your guess: ").strip().lower()

    # -----------------------------------------------------------------
    # SCENARIO A: The user wants to quit
    # -----------------------------------------------------------------
    if user_input=="exit":
        print("aborting mission")
        break
    # -----------------------------------------------------------------
    # SCENARIO B: Invalid Input
    # -----------------------------------------------------------------
    try:
        user_input=int(user_input)
    except:
        print("The safe only accepts digits. Try again")
        continue
    # -----------------------------------------------------------------
    # SCENARIO C: Processing a valid attempt
    # -----------------------------------------------------------------
    # If the code gets past Scenario B, it means they entered a valid 3-digit attempt!
    
    # TODO: Increase your attempts tracker variable by 1.
    atempts+=1

    # TODO: Check if 'user_input' matches the correct vault combination.
    #       If it does: Print "Vault unlocked! You found the treasure!" and 'break' out of the loop.
    #       If it doesn't: Print a message telling them the combination failed.
    if user_input==SAFE:
        print(f"vault unlocked! You found the treaure in {atempts} guess(es)")
        break
    else:
        print("combination failed. Try again")

# GAME OVER
# ---------------------------------------------------------------------
print("\n--- Game Over ---")



# =========================================
# EXTENSION
# TODO Add a scenario D to your loop: Running out of time
    # -----------------------------------------------------------------
    # SCENARIO D: Running out of time (EXTENSION)
    # -----------------------------------------------------------------
    # TODO: Check if their attempts tracker has reached 5.
    #       If it has, print "Alarm triggered! Security is on the way!" and 'break' the loop.

# =========================================
# EXPERT
# Mastermind Version:
# Add a part that lets you check each digit (you'll need to use split()) and tells the user how many digits are correct in their guess