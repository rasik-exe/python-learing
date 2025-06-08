f=open("file.txt","r") 
content=f.read()

if("rasik" in content):
    print("this is present")

else:
    print("this is not present")

f.close()
