#!/usr/bin/env python3
import sys

def downcase_it(s):
    return s.lower()

params = sys.argv[1:]

if not params:
    print("none")
else:
    for p in params:
        result = downcase_it(p)
        print(result)