#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    val_max= my_list[0]
    for num in my_list[1:]:
        if num > val_max:
            val_max = num
    return val_max
