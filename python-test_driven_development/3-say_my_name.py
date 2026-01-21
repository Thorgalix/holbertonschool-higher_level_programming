#!/usr/bin/python3
"""
Module 3-say_my_name: Contient une fonction qui affiche
le nom complet d'une personne.
"""


def say_my_name(first_name, last_name=""):
    """Affiche le nom complet d'une personne.
    Args:
        first_name (str): le prénom de la personne
        last_name (str, optional): le nom de famille de la personne.
        Par défaut, une chaîne vide.
    Raises:
        TypeError: si first_name n'est pas une chaîne
        TypeError: si last_name n'est pas une chaîne
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    name = first_name + (" " + last_name if last_name else "")
    print(f"My name is {name}", end="\n")
