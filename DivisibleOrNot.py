# Q7. Write a Python program to check if a number is divisible by both 3 and 5
N = int(input("Enter a number: "))
if N % 3 == 0 and N % 5 == 0:
    print("N is divisible by both 3 and 5.")
elif N % 5 == 0:
    print("N is divisible by 5 but not by 3.")
else:
    print("N is divisible by 3 but not by 5.")