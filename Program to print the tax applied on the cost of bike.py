num=int(input("enter the price of bike:"))
if num<=50000:
    print("tax applied is:",(5/100)*num)
elif num<100000:
    print("tax applied is:",(10/100)*num)
else:
    print("tax applied is:",(15/100)*num)
    
