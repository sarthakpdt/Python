num=int(input("enter the number:"))
sp=num-1
for i in range(0,num):
    for j in range(0,sp):
        print(end=" ")
    sp-=1
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
