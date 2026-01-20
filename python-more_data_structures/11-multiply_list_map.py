#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    y = lambda x: x*number
    newlist = list(map(y, my_list))
    return newlist
