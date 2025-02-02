km=int(input("enter the kilometer:"))
if km<=10:
    print("your bill is:",km*11)
elif km<=100:
    print("your bill is:",110+((km-10)*10))
else:
    print("your bill is:",1010+((km-100)*9))
