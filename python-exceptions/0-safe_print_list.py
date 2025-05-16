#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    i = 0
    try:
        for i in my_list:
            print(i, end='')
            if i == x:
                print()
                return i
        print()
        return i
    except TypeError or ValueError:
        print("Please choose a positive integer for x")
