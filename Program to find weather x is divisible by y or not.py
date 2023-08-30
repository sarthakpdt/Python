x=int(input("enter a number:"))
y=int(input("enter a number:"))
if x<0 and y<0:
    print("invalid input")

else:
    if y%x==0:
        print(y,"is divisible by",x)
    else:
        print(y,"is not divisible by",x)
