# Q3. Write a Python program to find the largest of three numbers
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if a>b and a>c:
    print("a is the largest number.")
elif b>a and b>c:
    print("b is the largest number.")
else:
    print("c is the largest number")
