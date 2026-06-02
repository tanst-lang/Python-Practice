MEMBER_STATUS = "gold"
passenger_row = input("Enter your seat row: ")
has_ticket = input("Do you have a valid ticket? (yes/no): ")
if has_ticket.lower() == "yes":
    if passenger_row.strip() <= 8 and MEMBER_STATUS == "gold":
        print("Welcome to priority boarding! Please make your way on board now.")
    elif passenger_row.strip() <= 8 or MEMBER_STATUS == "gold":
     print("Welcome to priority boarding! Please wait for our Gold Business Flyers to finish boarding.")
    else:
     print("Please wait for general boarding.")
     destination = input("Enter your destination code: ")
    if destination == "AKL" or "WLG":
     print("Flight is delayed 5 minutes.")
    if not destination =="CHC": 
     print("Flight is on time.")
    else:
     print("Flight has been cancelled")
else:
    print("Access Denied. Please ensure you have a valid ticket before boarding.")
