num=int(input("enter a number:"))
fact=1
n=1
if num<0:
    print("invalid number")
elif num==0 and num==1:
    print("1")
else:
    while n<=num:
        fact=fact*n
        n+=1
print("the factorial of",num,"is:",fact)
