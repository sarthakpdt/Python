num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
while num1!=num2:
    if num1>num2:
        num1-=num2
    else:
        num2-=num1
print(num1)
