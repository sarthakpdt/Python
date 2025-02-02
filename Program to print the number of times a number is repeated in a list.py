def count(lst,num):
    time=lst.count(num)
    return time

lst=eval(input("enter the list:"))
num=int(input("enter the number to be searched:"))
print(count(lst,num))
