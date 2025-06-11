class calculator():

    def __init__(self,n):
        self.n=n

    def square(self):
        print(f" square is: {self.n*self.n}")

    def cube(self):
        print(f"cube is:{self.n *self.n *self.n}")  

    def squareroot(self):
        print(f"squareroot is:{self.n*1/2}")  

    @staticmethod
    def hello():
        print("hello everyone")        

c=calculator(5)
c.square()
c.cube()
c.squareroot()
c.hello()