num=int(input("enter the number:"))
if num%2==0 and num%3==0:
    print("the number is divisible by 2 and 3 both")
else:
    if num%2==0:
        print("the number is divisible by 2 but not my 3")
    else:
        print("the number is divisible by 3 but not by 2")
