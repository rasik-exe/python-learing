import random

random_number=random.randint(1,100)

choice_number=int(input("enter the number between 1-10:"))

if(random_number==choice_number):
    print("YES , YOU ARE SELECT RIGHT NUMBER")

else:
    print("NO, YOU ARE SELECT WRONG NUMBER,BETTER LUCK NEXT TIME")


