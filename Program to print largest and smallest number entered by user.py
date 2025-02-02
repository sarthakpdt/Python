lst=[]
i=1
while i<=10:
    num=int(input("enter the number:"))
    lst.append(num)
    lst.sort()
    i+=1
print("the largest number is:",lst[-1])
print("the smallest number is:",lst[0])
