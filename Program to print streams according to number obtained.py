eng=int(input("enter your english numbers:"))
math=int(input("enter your math number:"))
sci=int(input("enter your science numbers:"))
sst=int(input("enter your social number:"))
if eng>80 and math>80 and sci>80 and sst>80:
    print("Science stream!!! == Marwao ab apni")
elif eng>80 and math>50 and sci>50:
    print("Commerce stream!!! == Saste me chor diya tumko")
elif eng>80 and sst>80:
    print("Humanities!!! == Ye ky hota h??")
