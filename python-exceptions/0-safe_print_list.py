#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    counter = 0
    try:
        if x <= 0:
            return 0
        if isinstance(my_list, str):
            my_list = list(my_list)
        for i in my_list:
            counter += 1
            print(i, end='')
            if counter == x:
                break
    except (TypeError, ValueError):
        print("Please choose a positive integer for x")
        return 0
    print()
    return counter
