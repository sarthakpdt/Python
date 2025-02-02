dic={}
num=int(input("enter how many key value pairs do you want to enter:"))
for i in range(num):
    x=int(input("enter the first number to be entered as key:"))
    y=int(input("enter the second number to be entered as key:"))
    z=int(input("enter the third number to be entered as key:"))

    dic[x,y,z]=(x*y*z)
print(dic)
