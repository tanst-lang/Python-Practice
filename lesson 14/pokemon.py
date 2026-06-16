# =====================================================================
# PROJECT: Pokemon
# Create a battle program where you battle a random pokemon
# =====================================================================

# TODO Import random module
import random
# Wild Pokemon
# TODO Create a multidimensional list that holds 4 pokemon names and their max health (you choose)
pokemons=[
    ['Greninja',10],
    ['pikachu',8],
    ['charmander',9],
    ['jigglypuff',6],
]
# User Pokemon
# TODO Create a multidimensional list that holds 4 pokemon attacks and their different damage
attacks=[
    ['fire blast',5],
    ['water blast',2],
    ['ground shock',3],
    ['surprise attack',4],
]
# TODO Create a variable to hold a randomised wild pokemon
random_pokemon=pokemons[random.randint(0,3)]
# TODO Create a current_health variable and set it to the max health of the random pokemon
current_health=random_pokemon[1]
# TODO Tell the user what pokemon they're facing
print(f"You are facing {random_pokemon[0]}")
# TODO Create a while loop that continues until current health <= 0
while not current_health<=0:
    print(f"{random_pokemon[0]} current health: {str(current_health)}")
    user_attack=input(f"which attack would you like to use:\n1. {attacks[0][0]}\n2. {attacks[1][0]}\n3. {attacks[2][0]}\n4. {attacks[3][0]}\n")
    try:
        user_attack=int(user_attack)
        user_attack-=1
    except:
        print("ERROR please answer using the corresponding number")
        continue
    current_health-=attacks[user_attack][1]
    # TODO Ask the user which attack they'd like to use (list all 4 options, numbered); save input
    # TODO Use try except to ensure the user has input a number; if they didn't tell them so and then use 'continue' to restart the loop
    # TODO Using the number, get the attack damage value and minus it from current health

# TODO Tell the user they defeated the pokemon
print(f"congradulations, you defeated {random_pokemon[0]}")
# ====================================================
# EXTENSION
# NOTE: Only do the extension once you have completed the project update (with dictionaries)

# TODO: Give your wild pokemon each an attack value as well, then allow it to attack the user back each turn (You'' need a player health)
# TODO: Change your 'user pokemon' to a list of different pokemon they can choose from. Each pokemon will have their own list of attacks.
# TODO: Give all pokemon a type. Create a new dictionary of types that each has a dictionary of strengths and weaknesses. Use this to change the damage.