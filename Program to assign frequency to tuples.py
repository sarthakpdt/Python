tup=eval(input("enter the tuple:"))
res=[]
for i in tup:
    if i not in res:
        res.append(i)
res1=[]
for i in res:
    x=list(i)
    x.append(tup.count(i))
    p=tuple(x)
    res1.append(p)

print(res1)
