dic={}
num=int(input("how many data do you want to enter:"))
for i in range(num):
    key=input("enter the name:")
    value=int(input("enter the age:"))
    dic[key]=value
print("your dictionary formed is:",dic)
a=list(dic.values())
a.sort()
for j in a:
    sorted_dic={j:dic[j]}
print(sorted_dic)
