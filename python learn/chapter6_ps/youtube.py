a="make a lot of money"
b="buy now"
c="subcribe pls"
d="click this"

msg=input("enter the massage:")

if((a in msg) or (b in msg) or (c in msg) or (d in msg)):
    print("massage is spam")

else:
    print("massage is not spam")    