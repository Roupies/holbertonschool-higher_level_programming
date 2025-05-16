#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    i = counter = 0
    try:
        if x <= 0:
            return 0
        for i in my_list:
            counter += 1
            print(i, end='')
            if i == x:
                print()
                return counter
        print()
        return counter
    except TypeError or ValueError:
        print("Please choose a positive integer for x")
