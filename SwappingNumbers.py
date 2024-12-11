# Q1. Write a Python program to swap two numbers without using a third variable
a = int(input("a"))
b = int(input("b"))
a = a + b
b = a - b
a = a - b
print("a =", a)
print("b =", b)