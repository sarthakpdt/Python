marks=1
while marks !=0:
    phy=int(input("enter the physics number:"))
    chem=int(input("enter the chemistry number:"))
    maths=int(input("enter the maths number:"))
    avg=(phy+chem+maths)/3
    if avg>90:
        print("grade: A","scholarship: 100%")
    elif avg>80:
        print("grade B","scholarship: 50%")
    elif avg>70:
        print("grade C","scholarship: 25%")
    else:
        print("grade D","no scholarship")
