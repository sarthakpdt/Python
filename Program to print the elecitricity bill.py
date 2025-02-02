num=int(input("enter the number:"))
if num<100:
    print("0")
elif num<200:
    print(num-100)*5
else:
    print(((num-200)*10)+500)
