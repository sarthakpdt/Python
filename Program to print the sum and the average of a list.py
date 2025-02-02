lst=eval(input("enter the list:"))
sum=0
for i in lst:
    sum+=i
    avg=sum/len(lst)

print("the sum of the list is:",sum)
print("the average of the list is:",avg)
