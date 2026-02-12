#!/usr/bin/env python3
import sys

params = sys.argv[1:]

if len(params) != 2:
    print("none")
else:
    keyword = params[0]
    sentence = params[1]
    
    count = sentence.count(keyword)
    
    if count == 0:
        print("none")
    else:
        print(count)