#!/usr/bin/env python3

num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
res = num1 * num2

print(f"{num1} x {num2} = {res}")

if res > 0: 
    print("The result is positive.")
elif res < 0: 
    print("The result is negative.")
else: 
    print("The result is positive and negative.")