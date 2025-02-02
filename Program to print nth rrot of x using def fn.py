def calc(x,n=2):
    res=x**(1/n)
    return res
x=int(input("enter the number:"))
n=int(input("enter the value of n:"))
print(calc(x,n))
