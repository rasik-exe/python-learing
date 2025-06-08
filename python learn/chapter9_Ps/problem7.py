
with open("log.txt") as f:
    lines=f.readline()

lineno=1
for line in lines:  
    if("PYTHON" in lines):
      print(f"YES , IT IS PRESENT IN LINE NO :{lineno}")
      break
    lineno +=1

else:
    print("NO, IT IS NOT PRESENT")