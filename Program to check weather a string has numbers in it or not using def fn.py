def stn(stng):
    for i in stng:
        if i.isalpha():
            return "true"
        else:
            return "false"

stng=input("enter the string:")
print(stn(stng))
