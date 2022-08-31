#!/usr/bin/python3
def summ(num1, *args):
    total = num1
    for num in args:
        total = total + num
    return total