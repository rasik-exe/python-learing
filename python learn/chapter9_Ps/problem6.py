with open("log.txt") as f:
    content=f.read()

if("python" in content):
    print("YES , IT IS PRESENT")
else:
    print("NO , IT IS NOT PRESENT")    
