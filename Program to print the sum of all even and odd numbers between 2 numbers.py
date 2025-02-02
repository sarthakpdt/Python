osum=0
esum=0
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
if num1>num2:
    while num1>=num2:
        if num2%2==0:
            esum+=num2
            num2+=1
        else:
            osum+=num2
            num2+=1
else:
    while num1<=num2:
        if num1%2==0:
            esum+=num1
            num1+=1
        else:
            osum+=num1
            num1+=1
print("the sum of all odd number is:",osum)
print("the sum of all even number is:",esum)

