#scoring
score= 0
#question 1 
print("what is the fastest animal?\na: cheetah\nb: swordfish\nc: peregrine falcon ")
question_1= input("your answer:")
answer_1= "c"
if question_1==answer_1 :
    print("correct! peregrine falcons are the fastest animal in the world")
    print()
    score +=1
else :
    print("whoops that's incorrect")

#question 2
print("What is acrophobia a fear of?\na: spiders\nb: hieghts\nc: water")
question_2=input("your answer:")
answer_2="b"
if question_2==answer_2:
    print("correct!")
    score +=1
else:
    print("whoops that's incorrect")

#question 3
question_3 = input("what color is Aureolin a shade of?\nyour answer:")
answer_3 = "yellow"
if question_3==answer_3:
    print("correct!")
    score +=1
else:
    print("whoops that's incorrect")

#question 4
question_4= input("what year was the video game 'Minecraft' officially released?\nyour answer:")
answer_4= "2011"
if question_4==answer_4:
    print("correct!")
    score +=1
else:
    print("whoops that's incorrect")

#question 5
question_5= input("how many time zones are there in the world?\nyour answer:")
answer_5= "24"
if question_5==answer_5:
    print("correct!")
    score +=1
else:
    print("whoops that's incorrect")

#question 6
print("in the series 'The Amazing World Of Gumball' what kind of animal is Anais?\na: mouse\nb: hamster\nc: rabbit")
question_6= input("your answer:")
answer_6= "c"
if question_6==answer_6:
    print("correct!")
    score +=1
else:
    print("whoops that's incorrect")

#final score
if score>3:
    print("good job you got more than half right")
print("well done you got "+str(score)+" out of 6 questions correct")
