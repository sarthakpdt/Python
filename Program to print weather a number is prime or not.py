num=int(input("enter a number:"))
var=0
for i in range(2,num):
    if num%i==0:
        var=1

if var==1:
    print("the number is not prime")
elif num==1:
    print("the number is neither prime nor composite")
else:
    print("the number is prime")
