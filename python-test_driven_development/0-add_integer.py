#!/usr/bin/python3
"""
Module 0-add_integer:
Contient une fonction qui additionne 2 entiers.
"""


def add_integer(a, b=98):
    """
    Additionne deux entiers et retourne le résultat.

    a et b doivent être des entiers ou des flottants ; les flottants
    sont convertis en int.
    Lève TypeError si a ou b ne sont pas des entiers ou flottants.

    Retourne :
        int : la somme de a et b
    """
    if not isinstance(a, (int, float)) or a != a:  # a != a vérifie NaN
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b != b:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
