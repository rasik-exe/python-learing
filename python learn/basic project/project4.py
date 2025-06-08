def length():
   
    print("enter 1 to converter kilometer")
    print("enter 2 to convert meter")
    kl_cm=int(input("enter the number 1 or 2: "))

    if(kl_cm==1):
        print("M to kl  ")
        meter=int(input("enter the number: "))
        kilometer=meter/1000
        print(f"{kilometer}km")
      
    elif(kl_cm==2):
        print("kl to M")
        kilometer=int(input("enter the number: "))
        meter=kilometer*1000
        print(f"{meter}m")

    else:
        print("invalid number")

  

def weight():

    print("enter 1 to convert kg to pound:")
    print("enter 2 to convert pound to kg:")
    WEIGHT=int(input("enter the number 1 or 2:"))

    if(WEIGHT==1):
        print("kg to pound")
        kg=int(input("enter the number:"))
        pound=kg*2.2
        print(f"{pound}lb")

    elif(WEIGHT==2):
        print("pound to kg")
        pound=int(input("enter the number:"))
        kg=pound/2.2
        print(f"{kg}kg")    

    else:
        print("invalid number")    


print("Enter 1 to convert the length:")
print("enter 2 to convert the weight:")        

choice=int(input("enter the number:"))
if(choice==1):
    length()
elif(choice==2):
    weight()    

