num=int(input("enter a number:"))
num1=num
a=0
b=0
length=len(str(num))
i=1
if num<0:
    print("invalid number")
else:
    while i<=length:
        a=num%10
        b=b*10+a
        num=num//10
        i+=1
if num1==b:
    print("the number is a palindrome number")
else:
    print("the number is not palindrome")
