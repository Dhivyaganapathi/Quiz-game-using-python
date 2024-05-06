print("WELCOME !!")
player = input("Do You Want to Play ?")
if player.lower() != "yes":
    quit()
print("OK, Let's Play")
score = 0
question = input("Baby frog is known as ?")
if question.lower() == "Tadpole" :
    print("CORRECT")
    score+=1
else:
    print("INCORRRECT")
question = input("Name the National river of India?")
if question.lower() == "Ganga" :
    print("CORRECT")
    score+=1
else:
    print("INCORRRECT")
question = input("Name the National fruit of India?")
if question.lower() == "Mango" :
    print("CORRECT")
    score+=1
else:
    print("INCORRRECT")
question = input("How many continents are there in the world?")
if question.lower() == "Seven" :
    print("CORRECT")
    score+=1
else:
    print("INCORRRECT")
question = input("Name the biggest continent in the world?")
if question.lower() == "Asia" :
    print("CORRECT")
    score+=1
else:
    print("INCORRRECT")
question = input("Name the house made of ice?")
if question.lower() == "Igloo" :
    print("CORRECT")
    score+=1
else:
    print("INCORRRECT")
question = input("Name the largest mammal?")
if question.lower() == "Blue " :
    print("CORRECT")
    score+=1
else:
    print("INCORRRECT")
question = input("Name the largest planet of our Solar System?")
if question.lower() == "Jupiter" :
    print("CORRECT")
    score+=1
else:
    print("INCORRRECT")
question = input("Name the National Reptile of India?")
if question.lower() == "King Cobra" :
    print("CORRECT")
    score+=1
else:
    print("INCORRRECT")
question = input("How many seconds make one hour?")
if question.lower() == "3600 Seconds" :
    print("CORRECT")
    score+=1
else:
    print("INCORRRECT")
print("YOUR SCORE",score)
        
