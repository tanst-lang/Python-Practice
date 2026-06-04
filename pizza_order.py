cost=0
#intro
print("welcome to papa's pizzaria what would you like to order?")

#base selection
base=input("Would you like a small(S)$5, medium(M)$7 or large(L)$10 base?\n").strip().lower()
if base=="l":
    base="Large"
    cost+=10
elif base=="m":
    base="Medium"
    cost+=7
elif base=="s":
    base="Small"
    cost+=5
else:
    input("Please restart program and enter valid answer")

#flavour selection
print("Which of the following flavours would you like\n1) plain cheese\n2) pepperoni\n3) hawian\n4) meatlover (+$1.50)\n5) vegetarian (+$1.00)")
flavor=input("answer using the corresponding number\n").strip().lower()
if flavor=="1":
    flavor="plain cheese"
elif flavor=="2":
    flavor="pepperoni"
elif flavor=="3":
    flavor="hawian"
elif flavor=="4":
    flavor="meatlover"
    cost+=1.5
elif flavor=="5":
    flavor="vegetarian"
    cost+=1
else:
    input("Please restart program and enter valid answer")

#extra topping selection
print("Extra toppings\n1) pepperoni\n2) mushrooms\n3) pineapple\n4) tomato\n5) ham\n6) BBQ chicken")
topping=input("answer using the corresponding number or press enter to skip\n")
if topping=="1":
    topping="pepperoni"
elif topping=="2":
    topping="mushrooms"
elif topping=="3":
    topping="pineapple"
elif topping=="4":
    topping="tomatoes"
elif topping=="5":
    topping="ham"
elif topping=="6":
    topping="BBQ chicken"
elif topping=="":
    topping="none"
else:
    input("Please restart program and enter valid answer")

#promo code
PROMO="promo"
promo=input("Do you have a promo code you would like to use?\n").strip().lower()=="yes"
if promo==True:
    promo=f"15% off"
    code=input("Enter promo code or press enter to skip ").strip().lower()
    if code==PROMO:
        print(f"Code valid\nYou get 15% off your meal!")
        cost= cost-((cost/100)*15)
    elif code=="":
        promo="none"
    else:
        print("ERROR code invalid")
        promo="none"
else:
    promo="none"

#notes
notes=input("Add any notes for your order or press enter to skip\n")
print()

#reciept
print("FINAL ORDER")
print(f"{base} base\n{flavor} flavour\nExtra toppings: {topping}\nPromo discount: {promo}\nTOTAL= ${cost}")
if not notes=="":
    print(f"Customer notes: {notes}")

