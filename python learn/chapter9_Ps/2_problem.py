///  
import random

def game():
    print("you are playing game")
    score=random.randint(1,50)

    with open("hiscore.txt") as f:
        hiscore=f.read()


///

    