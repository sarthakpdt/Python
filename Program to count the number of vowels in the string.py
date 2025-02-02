stng=input("enter the string:")
count=0
vowels=set("aeiouAEIOU")
for i in stng:
    if i in vowels:
        count+=1
        
print("the number of vowels in the string are:",count)
