age=int(input("enter your age:"))
sex=input("enter your sex:")
if age>=18 and age<30:
    if sex=="M":
        print("your wage is: 700/day")
    else:
        print("your age is: 750/day")
elif age>=30 and age<=40:
    if sex=="M":
        print("your wage is: 800/day")
    else:
        print("your wage is: 850/day")
else:
    print("your age is out of my range")
