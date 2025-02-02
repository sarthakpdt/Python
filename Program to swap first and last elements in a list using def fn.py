def swaplist(list):
    first=list.pop(0)
    last=list.pop(-1)

    list.insert(0,last)
    list.append(first)
    
    return (list)

list=eval(input("enter the list:"))
print(swaplist(list))
    
