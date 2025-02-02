def split(stng):
    lst1=stng.split()
    return lst1

def join(stng):
    lst2="-".join(stng)
    return lst2

stng=input("enter the string:")
print(split(stng))
print(join(stng))


