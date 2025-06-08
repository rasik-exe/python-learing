dsa=int(input("enter the dsa marks:"))
java=int(input("enter the java marks:"))
python=int(input("enter the python marks:"))

total_percentage=(100*(dsa + java + python))/300

if(total_percentage>40 and dsa>30 and java>30 and python>30):
    print("student is pass:",total_percentage)

else:
    print("student is fail",total_percentage)