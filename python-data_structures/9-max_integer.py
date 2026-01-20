#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max0 = my_list[0]
    for num in my_list:
        if num > max0:
            max0 = num
    return max0
