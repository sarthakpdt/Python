num=int(input("enter the year:"))
if num%100==0:
    if num%400:
        print("the number is a leap year")
    else:
        print("the number is not a leap year")
else:
    if num%4==0:
        print("the number is a leap year")
    else:
        print("the number is not a leap year")
