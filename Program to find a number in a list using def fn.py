def find(lst,num):
    if num in lst:
        return "yes the number is there in list"

    else:
        return "no the number is not in the list"

lst=eval(input("enter the list:"))
num=int(input("enter the number to be searched:"))

print(find(lst,num))
    
