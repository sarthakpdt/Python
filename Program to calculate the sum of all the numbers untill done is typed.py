total=0
num="yes"
while num=="yes":
    num=int(input("enter a number:"))
    total+=num
    num=input("do you want to continue?:")
print("the sum of the numbers entered by user is:",total)
