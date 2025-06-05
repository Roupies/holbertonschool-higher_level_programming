#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a text file and prints it to the POSIX standard output.

    Keyword arguments:
    filename -- the name of the file to read (default is an empty string)
    """
    with open(filename, 'r') as file:
        print(file.read(), end="")