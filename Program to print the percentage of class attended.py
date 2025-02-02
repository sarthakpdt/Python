total=int(input("enter the total number of days:"))
absent=int(input("enter the number of days you were absent:"))
per=(total-absent)/total*100
if per>75:
    print("you can sit in the exam")
else:
    print("you cannot sit in the exam")
