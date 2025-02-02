num=int(input("enter how many terms u want in febonacci series:"))
if num==1:
    print("1")
elif num<0:
    print("please enter a valid number")
else:
    a=1
    b=1
    print(a,end=" ")
    print(b,end=" ")
    i=2
    while i<num:
        res=a+b
        print(res,end=" ")
        a=b
        b=res
        i=i+1

