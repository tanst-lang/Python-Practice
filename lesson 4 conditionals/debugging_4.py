print("--- Daily Step Tracker ---")
#how many steps user took
steps = input("How many steps did you walk today? ")
steps = int(steps)
#conditionals
#over 1000 steps
if steps >= 10000 :
    print("Amazing! You walked over 10,000 steps! You are a Pro Athlete.")
#uner 5000 steps
if steps < 5000:
    print("Good start, but try to walk a bit more tomorrow!")
#daily goal
DAILY_GOAL = 5000
#goal reached
if steps==DAILY_GOAL:
    print("Bullseye! You hit your goal exactly!")
#0 steps
if steps==0:
    print("Did you forget your phone today? You have 0 steps!")
#close tracker
print("Tracker closing...")