with open("this.txt")as f:
    content1=f.read()
with open("this_copy.txt")as f:
    content2=f.read()


if(content1==content2):
    print("YES , THIS IS MATCH")

else:
    print("NO, THIS IS NOT MATCH")