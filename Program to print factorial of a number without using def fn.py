num=int(input("enter the number:"))
i=1
fact=1
if num<0:
    print("wrong number entered")
else:
    while i<=num:
        fact=fact*i
        i+=1
    print(fact)
