tup=eval(input("enter the tuple:"))
num=int(input("enter the length of tuple to be removed:"))
a=list(tup)
for i in a:
    if len(i)==num:
        a.remove(i)
    else:
        break
    
print(tuple(a))
