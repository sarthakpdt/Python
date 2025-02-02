num=int(input("enter the number:"))
for i in range(1,num+1):
    for j in range(i):
        if j==0 or j==i-1:
            print("*",end=" ")
        else:
            if i!=num:
                print(" ",end=" ")
            else:
                print("*",end=" ")
    print("\r")
