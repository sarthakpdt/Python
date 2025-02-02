num=int(input("enter the number:"))
for i in range(0,num):
    for j in range(0,num-i):
        print("*",end=" ")
    print("\r")
