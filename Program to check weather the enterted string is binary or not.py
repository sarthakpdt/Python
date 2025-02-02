binary=input("enter the string:")
num=set(binary)
dic={"0","1"}
if num==dic or num=={"0"} or num=={"1"}:
    print("the string entered is binary")
else:
    print("the string is not binary")
