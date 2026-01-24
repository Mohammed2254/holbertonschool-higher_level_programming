#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Print first x integers from a list
    Args:
        my_list: List containing mixed types
        x: Number of elements to access
    Returns:
        Real number of integers printed
    """
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue

    return count
