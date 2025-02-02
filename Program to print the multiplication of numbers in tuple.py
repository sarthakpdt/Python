tup=eval(input("enter the tuple:"))
mul=[]
for i in range(len(tup)-1):
    mul.append(tup[i]*tup[i+1])

mul=tuple(mul)    
print(mul)
    
    
