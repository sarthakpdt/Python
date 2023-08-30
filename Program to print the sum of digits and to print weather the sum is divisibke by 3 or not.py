digit=int(input("enter a 3 digit number:"))
total=0
if digit==0:
    print("the sum is: 0")
else:
    total=int(digit%10)+(digit//100)
print("the sum of the digits is:",total)
if total%3==0:
    print("yes the sum is divisible by 3")

else:
    print("no the sum is not divisible by 3")
    
