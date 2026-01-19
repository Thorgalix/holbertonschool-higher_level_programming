#!/usr/bin/python3
fruits1 = {'pomme' : 1.50, 'ananas' : 2.20}
fruits2 = {'orange' : 2.00, 'kiwi' : 5.20}
print (fruits1.get("pomme"), "avant")
print (fruits1.get("ananas"), "avant")

fruits1["pomme"] = 2.10
fruits1["ananas"] = 3.50

print (fruits1.get("pomme"), "après")
print (fruits1.get("ananas"), "après")


