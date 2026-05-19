user_age = input("Enter your age: ")
user_age=int(user_age)
if user_age < 18:
    discount = 20.0
elif user_age == 18:
    discount = 10.0
else:
    discount = 0.0
item_price = 50
final_price = item_price - discount
gst = 0.12
final_price = final_price -(final_price * gst)
print("The total is: " + str(final_price))
if final_price > 40:
    print("Expensive")
else: 
    print("Affordable")