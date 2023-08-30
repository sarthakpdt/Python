num=int(input("enter the number:"))
temp=num
reverse_num=0
while num!=0:
    digit=num%10
    reverse_num=digit+(reverse_num*10)
    num=num//10
print("the reversed number is:",reverse_num)

if temp==reverse_num:
    print("the number is palindrome")
else:
    print("the number is not palindrome")
