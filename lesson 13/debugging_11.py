banned_items = ["slingshot","laser"]
inventory = ["apple","slingshot","book","laser"]
confiscated = []
print(f"Scanning inventory: {inventory}")
for item in inventory:
    if item in banned_items:
        print(f"Alert! Found banned item: {inventory.index(item)}")
        confiscated.append(item)
        inventory.pop(inventory.index(item))
    print(f"Scan complete. Total flag matches: {len(banned_items)}")
if len(confiscated) > 0:
    print("Items confiscated:")
    for i in confiscated:
        print(f"{confiscated.index(i)+1} {i}")
    # FOR the number of items in the confiscated list (use index)
        # PRINT the item listed with a number (eg. 1. Laser)