tup=eval(input("enter a tuple:"))
res=0
for i in tup:
    res=tup.count(i)
    print("the number",i,"is repeated",res,"number of times")
