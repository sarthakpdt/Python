lst=eval(input("enter the list:"))
pos=0
neg=0
for i in lst:
    if i>0:
        pos+=1
    else:
        neg+=1

print("the positive number in the list are:",pos)
print("the negative number in the list are:",neg)
