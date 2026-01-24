#!/usr/bin/python3
def safe_print_integer(value):
    """
    Safely print an integer
    Args:
        value: Value to print (can be any type)
    Returns:
        True if value is integer and printed successfully
        False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
