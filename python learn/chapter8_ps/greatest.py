a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))

def greater(a,b,c):
    if(a>b and a>c):
        return a

    elif(b>a and b>c):
       return b

    elif(c>a and c>b):
       return c
print(greater(a,b,c))              