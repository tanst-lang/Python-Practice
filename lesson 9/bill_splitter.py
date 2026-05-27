#Create a program that calculates how much 3 different people should
# pay for their portion of a food bill by storing their percentage in a variable
total_cost=int(input("what is the total cost of the food bill: "))
person1=int(input("what percentage is person 1 paying: "))
person2=int(input("what percentage is person 2 paying: "))
person3=int(input("what percentage is person 3 paying: "))

p1_cost=total_cost*person1/100
p2_cost=total_cost*person2/100
p3_cost=total_cost*person3/100
print("person 1 pays $"+str(p1_cost))
print("person 2 pays $"+str(p2_cost))
print("person 3 pays $"+str(p3_cost))