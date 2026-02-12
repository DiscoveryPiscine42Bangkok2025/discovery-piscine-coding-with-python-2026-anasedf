#!/usr/bin/env python3

print("Enter a number less than 25")
user_input = int(input())

if user_input > 25:
    print("Error")
else:
    for i in range(user_input, 26):
        print(f"Inside the loop, my variable is {i}")
