import random
def calc(n):
    min=10**(n-1)
    max=(10**n)-1
    res=random.randint(min,max)
    return res
n=int(input("enter the number:"))
print(calc(n))
