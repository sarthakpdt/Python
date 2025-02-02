url=input("enter the url:")
x=url.split()
y=[]
for i in x:
    if i.startswith("https:") or i .startswith("http:"):
        y.append(i)

print(y)
