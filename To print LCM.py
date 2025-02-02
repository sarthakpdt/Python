num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
if num1>num2:
    large=num1
else:
    large=num2
while True:
    if(large%num1==0 and large%num2==0):   
        print(large)
        break
    large+=1
