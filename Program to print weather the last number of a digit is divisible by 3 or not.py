num=int(input("enter a number:"))
res=num%10
print("the last number of the digit is:",res)
if res%3==0:
    print(res,"is divisible by 3")
else:
    print(res,"is not divisibe by 3")
