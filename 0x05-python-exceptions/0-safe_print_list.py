#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for x in (my_list):
            print (*my_list)
    except TypeError:
        print("this is a type Error")
    except: 
        print("unknown error")

