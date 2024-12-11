# Q10. Write a Python program to calculate the factorial of a number
factorial = 1
N = int(input("Enter a number: "))
for i in range(1,N+1):
    factorial *= i
print(factorial)