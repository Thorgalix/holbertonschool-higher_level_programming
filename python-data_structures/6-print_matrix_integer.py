#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lignes in matrix:
        print(" ".join("{:d}".format(elements) for elements in lignes))
