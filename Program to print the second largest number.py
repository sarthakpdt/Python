num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
if (num1>num2 and num1<num3) or (num1<num2 and num1>num3):
    print("second largest number is:",num1)
elif (num2>num1 and num2<num3) or (num2<num1 and num2>num3):
    print("second largest number is:",num2)
else:
    print("second largest number is:",num3)
    
    
