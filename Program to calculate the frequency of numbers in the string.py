stng=input("enter the string:")
count=0
for i in stng:
    if i.isdigit():
        count+=1

print("the frequency of number in the string is:",count)
