stng=input("enter the string:")
spl=stng.split(" ")
for i in spl:
    if len(i)%2==0:
        print(i)
