#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dictt = sorted(a_dictionary)
    for key in dictt:
        print("{}: {}".format(key, a_dictionary[key]))
