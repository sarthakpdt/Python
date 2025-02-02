side1=int(input("enter the first side:"))
side2=int(input("enter the second side:"))
side3=int(input("enter the third side:"))
if side1==side2==side3:
    print("it is a equilateral triangle")
elif side1!=side2!=side3:
    print("it is a scalene triangle")
else:
    print("it is a isosceles triangle")
