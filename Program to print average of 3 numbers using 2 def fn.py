def calc(x,y,z):
    sum=x+y+z
    return sum
def avg(x,y,z):
    avg=calc(x,y,z)/3
    return avg
x=int(input("enter the number:"))
y=int(input("enter the number:"))
z=int(input("enter the number:"))
print("average of the number is:",avg(x,y,z))
