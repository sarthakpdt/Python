string=input("enter the string:")
half=int(len(string)/2)

first=string[:half]
second=string[half:]

if first==second:
    print("the string entered is palindrome")
else:
    print("the string is not palindrome")
