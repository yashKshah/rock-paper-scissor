#'''Rock Paper Scissors
#Rock > Scissor
#Paper > Rock
#Scissor > Paper
#'''
import random
import keyboard
import sys

def game():
    user = input("Enter R for Rock\nEnter P for Paper\nEnter S for Scissor\n")

    a = random.randint(1,3)
    if(a == 1):
        comp = "R"
    elif(a == 2):
        comp = "P"
    elif(a == 3):
        comp = "S"

    print(f"You choose {user}")
    print(f"Computer choose {comp}")

    if (comp == user):
        return None
    if(comp == "R"):
        if(user == "P"):
            return True
        elif(user == "S"):
            return False
    if(comp == "P"):
        if(user == "S"):
            return True
        elif(user == "R"):
            return False
    if(comp == "S"):
        if(user == "R"):
            return True
        elif(user == "P"):
            return False
    pass



while True:
    result = game()
    if(result == None):
        print("DRAW")
    elif(result == True):
        print("You WON")
    else:
        print("You LOSE")      
    