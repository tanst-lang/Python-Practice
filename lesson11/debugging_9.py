ATM_BALANCE=500
while True:
    user_input = input("Enter withdrawal amount (or 'exit' to quit): ")
    if user_input.lower().strip() == "exit":
        break
    amount = int(user_input)
    if amount <= 0:
        print("Invalid amount. Try again.")
        continue
    if amount > ATM_BALANCE:
        print("Insufficient funds!")
        continue
    ATM_BALANCE = ATM_BALANCE - amount
    print(f"Withdrawal successful. Remaining balance: {ATM_BALANCE}")
    # IF ATM_BALANCE is equal to 0 THEN print "ATM Empty" and BREAK out of the loop
    if ATM_BALANCE==0:
        print("ATM empty")
        break
print("exited")