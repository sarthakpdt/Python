lst=eval(input("enter the tuple:"))
for i in lst:
    if not(i.count(None)==len(i)):
        lst.remove(i)
        
print(tuple(lst))
        
