price=int(input("enter the price:"))
if price<=7000:
    print("you will get this product at",price*(10/100),"price")
elif price<=10000:
    print("you will get this product at",price*(15/100),"price")
else:
    print("you will get this product at",price*(20/100),"price")
