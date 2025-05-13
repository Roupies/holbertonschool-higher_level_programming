#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        print(" ".join(f"{x:3}" for x in row))
