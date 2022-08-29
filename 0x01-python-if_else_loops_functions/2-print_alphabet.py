#!/usr/bin/python3
string = "{}"
for c in range(97, 123):
    print(string.format(chr(c), end=""))