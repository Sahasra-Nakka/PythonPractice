# Q14. Write a Python program to check if a number is prime
import math
N = int(input("Enter a number: "))
if N < 2:
    print("N is Not Prime.")
else:
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            print("N is Not Prime.")
            break
    else:
        print("N is Prime.")
