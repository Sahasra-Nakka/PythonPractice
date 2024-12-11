# Q6. Write a Python program to count the number of vowels in a string
str = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for i in str:
    if i in vowels:
        count += 1
print(count)