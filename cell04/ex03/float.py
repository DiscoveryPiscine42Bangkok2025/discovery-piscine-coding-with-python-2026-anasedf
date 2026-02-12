#!/usr/bin/env python3

value = float(input("Give me a number: "))

if value.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")