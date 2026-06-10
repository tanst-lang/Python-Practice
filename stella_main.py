shopping_cart=[]
price_list=[]
while True:
    shopping_list="\n".join(shopping_cart)
    print(f"current shopping list:\n{shopping_cart}")
    print(shopping_cart)
    # Current prices
    current_prices="\n".join(price_list)
    print(f"current price list:\n{price_list}")
    # TODO Output Options for user: 1. Add item to cart, 2. Remove item from cart, 3. Clear cart and restart, 4. View total and checkout
    # TODO Get user input (1-4) and save in variable
    user_action=input("select either 1 to add item to cart, 2 to remove item from cart, 3 to clear cart or 4 to checkout")
    # -----------------------------------------------------------------
    # OPTION 1: ADD ITEM 
    # -----------------------------------------------------------------
    if user_action=="1":
        item_name=input("Name of the item you adding: ")
        shopping_cart.append(item_name)
        item_price=input(f"price of {item_name}: $")
        item_price=float(item_price)
        price_list.append(item_price)
        continue