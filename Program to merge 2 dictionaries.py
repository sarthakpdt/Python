num1=int(input("enter how many key value pairs do you want in 1 dic:"))
dic1={}
dic2={}
for i in range(num1):
    key1=input("enter the name:")
    value1=int(input("enter the age:"))
    dic1[key1]=value1
num2=int(input("enter how many key value pair do you want in 2 dic:"))
for j in range(num2):
    key2=input("enter the name:")
    value2=int(input("enter the age:"))
    dic2[key2]=value2
print("before merging first dictionary is:",dic1)
print("before merging second dictionary is:",dic2)
res=dic2.update(dic1)
print("after merging the dictionary formed is:",res)
