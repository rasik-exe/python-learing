items=[]
n=int(input("how many items you want :"))
for i in range(n):
    item=input("enter the items:")
    items.append(item)

print("list is")

for choice in items: 
    print("*",choice)


