def calc(b=1):
    for i in range(1,11):
        a=0
        for j in range(1,11):
            a=a+b
            b+=1
        print(a)
        
calc()
