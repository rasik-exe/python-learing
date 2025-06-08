name="rasik"

with open("name.txt","r") as f:
    content=f.read()

newcontent=content.replace(name,"@@@@")

with open("name.txt","w") as f:
    f.write(newcontent)
