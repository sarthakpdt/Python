num=int(input("enter the number:"))
for i in range(num):
    for j in range(1,num-i):
        print(" ",end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print("\r")
    
