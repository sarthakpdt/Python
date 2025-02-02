lst=eval(input("enter the list:"))
for i in lst:
    time= lst.count(i)
    if time>1:
        print(i,end=' ')
