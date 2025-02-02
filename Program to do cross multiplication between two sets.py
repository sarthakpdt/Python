tup1=eval(input("enter the first tuple:"))
tup2=eval(input("enter the second tuple:"))
tup=[]
for i in tup1:
    for j in tup2:
        tup.append((i,j))
        tup.append((j,i))
print(tup)
