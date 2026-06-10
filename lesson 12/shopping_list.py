# =====================================================================
# PROJECT: Shopping List & Budget Tracker
# GOAL: Practice adding items to lists and calculating data from them.
# =====================================================================

# INITIALIZE YOUR LISTS
# TODO: Create an empty list called 'shopping_cart' to hold item names.
# TODO: Create an empty list called 'price_list' to hold item prices.
shopping_cart=[]
price_list=[]
# MAIN
# TODO Create an infinite while loop
while True:
    print()
    print("current shopping list:",*shopping_cart, sep="\n")
    print()
    print("current price list:",*price_list, sep="\n$")
    print()
    user_action=input("select either 1 to add item to cart, 2 to remove item from cart, 3 to clear cart or 4 to checkout\n")
    # -----------------------------------------------------------------
    # OPTION 1: ADD ITEM 
    # -----------------------------------------------------------------
    if user_action=="1":
        item_name=input("Name of the item(s) you adding: ")
        shopping_cart.append(item_name)
        item_price=input(f"price of {item_name}: $")
        item_price=float(item_price)
        price_list.append(item_price)
    # -----------------------------------------------------------------
    # OPTION 2: REMOVE ITEM 
    # -----------------------------------------------------------------
    elif user_action=="2":
        remove_item=input("What item do you want to remove: ")
        try:
            remove_item_num=shopping_cart.index(remove_item)
            shopping_cart.pop(remove_item_num)
            price_list.pop(remove_item_num)
        except:
            print("That item is not in your cart")
    # -----------------------------------------------------------------
    # OPTION 3: CLEAR CART (Practice clearing a list)
    # -----------------------------------------------------------------
    elif user_action=="3":
        shopping_cart.clear()
        price_list.clear()
        print("your cart is now empty")

    # -----------------------------------------------------------------
    # OPTION 4: CHECKOUT
    # -----------------------------------------------------------------
    elif user_action=="4":
        total_cost = sum(price_list)
        print(f"Total cost: ${total_cost}")
        break

    # -----------------------------------------------------------------
    # NO OPTION
    # -----------------------------------------------------------------
    else:
        print("ERROR invalid input, please use either 1, 2, 3 or 4 to answer")
print("quit program")
# ====================================================================
# EXTENSION
# Add a budget to the list
# TODO Tell them if their cart is over budget
# TODO Recommend items to remove based on their price.

# =====================================================================
# EXPERT
# Change your program to use dictionaries so prices are connected to shopping items
# Display the cart in alphabetical order
# Add an option to display the cart in order of price.