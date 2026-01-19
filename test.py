#!/usr/bin/python3
L = int(input("Veuillez saisir le nombre de lignes : "))
c = int(input("Veuillez saisir le nombre de colonnes : "))

for i in range(L):
    for j in range(c):
        print("*", end=" ")
    print()

