# Q13. Write a Python program to find the sum of digits of a number
sumOfDigits = 0
N = input("Enter a number: ")
for i in N:
    sumOfDigits += int(i)
print(sumOfDigits)