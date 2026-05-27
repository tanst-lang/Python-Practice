# --- THE HERO'S INVENTORY ---

# Section 1
hero_name = input("What's your name hero?")
gold_found = 50
gold_lost = 20
current_gold = gold_found - gold_lost

# Section 2
weapon = "Sword"
damage = 15
level_up_bonus = 5
total_damage = damage + level_up_bonus


# Section 3
print("Hero Name: " + hero_name)
print("Gold Coins: " + str(current_gold))
print("Weapon Damage: "+ str(total_damage))