def table(num,length):
    for i in range(1,length+1):
        result=num*i
        print(num,"*",i,"=",num*i)


num=int(input("Enter a number: "))
length=int(input("Enter the table length: "))
table(num,length)
