tup=eval(input("enter the tuple:"))
res=True
for i in range(len(tup)):
    if tup[i] in tup[i+1:]:
        res=False
    break
print(res)
