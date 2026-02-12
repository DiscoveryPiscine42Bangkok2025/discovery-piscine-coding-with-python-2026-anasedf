#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    word = sys.argv[1]
    answer = input("What was the parameter? ")
    
    if answer == word:
        print("Good job!")
    else:
        print("Nope, sorry...")