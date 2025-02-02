num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
if num1>num2:
    while num1>num2:
        if num2%2==0:
            print(num2)
            num2+=2
else:
    while num1<num2:
        if num1%2==0:
            print(num1)
            num1+=2
