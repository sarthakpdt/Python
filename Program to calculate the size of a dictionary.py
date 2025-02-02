dic={}
num=int(input("enter how many time you want to enter key value pair:"))
for i in range(num):
    a=input("enter the key:")
    b=int(input("enter the value:"))
    dic[a]=b
print("the dictionary formed is:",dic)
print("the size of this dicttionary is:",dic.__sizeof__(),"bytes")
