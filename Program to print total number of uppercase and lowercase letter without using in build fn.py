sen=input("enter the sentence:")
lower=0
upper=0
for i in sen:
    if (i>="a" and i<="z"):
        lower+=1
    else:
        upper+=1
print("total number of lowercase letters are:",lower)
print("total number of uppercase letters are:",upper)
