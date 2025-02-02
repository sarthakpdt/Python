def swapnum(list,num1,num2):
    first=list.pop(num1)
    second=list.pop(num2-1)

    list.insert(num1,second)
    list.insert(num2,first)

    return(list)

list=eval(input("enter the list:"))
num1=int(input("enter the first position:"))
num2=int(input("enter the second position:"))

print(swapnum(list,num1,num2))
