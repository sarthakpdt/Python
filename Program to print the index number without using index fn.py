tup=("a","b","c","d")
ch=input("enter the element to be searched:")
if ch in tup:
    count=0
    for i in tup:
        if i!=ch:
            count+=1
        else:
            break
    print(count)
