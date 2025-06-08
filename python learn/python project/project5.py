def chat_box():
    print("welcome to my chatbox")

    while True:

        msg=input("enter the msg:")

        if(msg=="hello"):
            print("BOT : HELLO RASIK")

        elif(msg=="how are your"):
            print("BOT : I AM FINE ")
        
        elif(msg=="tell about python"):
            print("BOT:Python is a versatile, high-level programming language renowned for its readability and simplicity. It is widely used in various fields, including web development, data science, machine learning, and automation. Python's design philosophy emphasizes code readability, making it an accessible language for both beginners and experienced developers")

        elif(msg=="bye"):
            print("BOT: EXIT IN CHATBOX")
          
            break

        else:
           print(" invalid msg")

           break

    
chat_box()       




    













 
