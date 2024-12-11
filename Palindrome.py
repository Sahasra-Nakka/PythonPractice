# Q11. Write a Python program to check if a string is a palindrome
str = input("Enter a string: ")
str = str.replace(" ", "").lower()
a = 0
b = len(str) - 1
while a < b:
    if str[a]!=str[b]:
        print("Given string is Not a Palindrome")
        break
    a += 1
    b -= 1
else:
    print("Given string is a Palindrome")