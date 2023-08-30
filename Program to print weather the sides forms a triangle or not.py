side_1=int(input("enter the first side:"))
side_2=int(input("enter the second side:"))
side_3=int(input("enter the third side:"))
if (side_1+side_2)>side_3:
    print("it is a triangle")
elif (side_2+side_3)>side_1:
    print("it is a triangle")
elif (side_3+side_1)>side_2:
    print("it is a triangle")
else:
    print("it is not a triangle")
