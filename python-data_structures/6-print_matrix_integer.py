#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lignes in matrix:
        for elements in lignes:
            print("{:d}".format(elements), end=" ")
        print()
