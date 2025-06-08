number1=int(input("enter the first number:"))
number2=int(input("enter the second number:"))
operation=input("enter the operation(+,-,*,/):")

if(operation=="+"):
    c=number1+number2
    print(f"{number1} + {number2}={c}")

elif(operation=="-"):
    c=number1-number2
    print(f"{number1} - {number2}={c}")


elif(operation=="*"):
      c=number1*number2
      print(f"{number1} * {number2}={c}")


elif(operation=="/"):
      c=number1/number2
      print(f"{number1} / {number2}={c}")

print("result",c)    