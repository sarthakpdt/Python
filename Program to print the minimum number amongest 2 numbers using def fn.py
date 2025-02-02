def minimum(num1,num2):
    if num1>num2:
        return num2

    else:
        return num1

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("the smallest number amongest the  number is:",minimum(num1,num2))
