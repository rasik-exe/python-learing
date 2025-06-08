words=["hey","sam","one"]

with open("list.txt","r") as f:
    content=f.read()

for word in words:
    content=content.replace(word,"$"*len(word))    

with open("list.txt","w") as f:
    f.write(content)   