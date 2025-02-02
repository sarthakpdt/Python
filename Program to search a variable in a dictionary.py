dic={}
num=int(input("how many data do u want to enter?:"))
for i in range(num):
    a=input("enter the key:")
    b=int(input("enter the value:"))
    dic[a]=b
print("dictionary formed is:",dic)
rf=input("enter the variable to be searched:")
if rf in dic:
    print("the variable",rf,"is present in the dictionary")
else:
    print("the variable",rf,"is not presentin the dictionary")
