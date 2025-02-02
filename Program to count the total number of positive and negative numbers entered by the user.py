pcount=0
ncount=0
ch="yes"
while ch=="yes":
    num=int(input("enter the number:"))
    if num>0:
        pcount+=1
    else:
        ncount+=1
    ch=input("do you want to continue:")
print("total number of positive number are:",pcount)
print("total number of negative number are:",ncount)
