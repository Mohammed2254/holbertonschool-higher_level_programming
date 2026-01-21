#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or a_dictionary == {}:
        return None
    best = ""
    val = 0
    for key, value in a_dictionary.items():
        if value > val:
            best = key
            val = value
    return best
