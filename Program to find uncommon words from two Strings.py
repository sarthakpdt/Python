stng1=input("enter the first string:")
stng2=input("enter the second string:")
a=stng1.split()
b=stng2.split()
x=[]
for i in a:
    if i not in b:
        x.append(i)

for i in b:
    if i not in a:
        x.append(i)

print(x)
