cost=0
print("welcome to papa's pizzaria what would you like to order?")
base=input("Would you like a small(S)$5, medium(M)$7 or large(L)$10 base?\n").strip().lower
if base=="l" or base=="large":
    cost+=10
elif base=="m" or base=="medium":
    cost+=7
elif base=="s" or base=="small":
    cost+=5
else:
    input("Please restart program and enter valid answer")
print("Which of the following flavours would you like\n1) plain cheese\n2) peperroni\n3) hawian\n4) meatlover\n5) vegetarian")
flavor=input("answer using the corresponding number\n")
if flavor