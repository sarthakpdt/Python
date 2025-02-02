num=int(input("enter the number:"))
a=0
b=1
while num!=0:
    a=num%10
    b=b*a
    num=num//10
print("the multiplication of digit is:",b)
