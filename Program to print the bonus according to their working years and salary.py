sal=int(input("enter the salary:"))
year=int(input("enter the year:"))
if year<6:
    total=sal*(5/100)
    print("your bonus is:",total)
elif year<10:
    total2=sal*(8/100)
    print("your bonus is:",total2)
else:
    total3=sal*(10/100)
    print("your bonus is:",total3)
