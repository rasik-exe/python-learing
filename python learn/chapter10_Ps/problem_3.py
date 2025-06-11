import random

class train():
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"train is book {self.trainNo} from {fro} to {to}")


    def getstatus(self):
        print(f" train number {self.trainNo} is running")  

    def price(self,fro,to):
        fare=random.randint(555,1000)
        print(f"train is book {self.trainNo} from {fro} to {to} {fare}")  


t=train(1555) 
t.book("mumbai","raigad")
t.getstatus()
t.price("mumbai","raigad")

