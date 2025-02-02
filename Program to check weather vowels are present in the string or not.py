stng=input("enter the string:")
vowels="aeiou"
if all((vowel or vowel.upper()) in stng for vowel in vowels):
    print("all vowels are present in the string")
else:
    print("all vowels are not present in the string")
