lst=eval(input("enter the list:"))
even=0
odd=0
for i in lst:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("the number of even numbers in the list are:",even)
print("the number of odd numbers in the list are:",odd)    
