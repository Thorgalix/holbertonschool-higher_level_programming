#!/usr/bin/python3
def no_c(my_string):
    resultat = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            resultat += char
    return resultat
