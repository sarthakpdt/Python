num=int(input("enter the number:"))
i=0
while i<num:
    if i==0 or i==num-1:
        print("*"*num)
    else:
        print("*"+" "*(num-2)+"*")
    i+=1
    
