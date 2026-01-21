#!/usr/bin/python3
"""
Module 2-matrix_divided:
Contient une fonction qui divise tous les éléments d'une matrice par un diviseur.
"""


def matrix_divided(matrix, div):
    """Divise tous les éléments d'une matrice par div et retourne une nouvelle matrice.

    Args:
        matrix (list of lists of int/float): la matrice à diviser
        div (int/float): le diviseur

    Returns:
        list: nouvelle matrice avec tous les éléments divisés et arrondis à 2 décimales

    Raises:
        TypeError: si matrix n'est pas une liste de listes de nombres
        TypeError: si les lignes de matrix n'ont pas la même taille
        TypeError: si div n'est pas un nombre
        ZeroDivisionError: si div est égal à 0
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
