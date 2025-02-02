dic={}
num=int(input("enter how many key vale pairs do you want to enter:"))
for i in range(num):
    a=input("enter the key:")
    b=int(input("enter the value:"))
    dic[a]=b
print("the dictionary formed is:",dic)
value=list(dic.values())
total=0
for i in value:
    total+=i
print("the sum of all the values in a dictionary is:",int(total))
    
