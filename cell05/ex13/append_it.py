#!/usr/bin/env python3
import sys

params = sys.argv[1:]

if not params:
    print("none")
else:
    for p in params:
        if not p.endswith("ism"):
            print(p + "ism")