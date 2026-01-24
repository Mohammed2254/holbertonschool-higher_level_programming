#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divide two integers and print result with debug info
    Args:
        a: Numerator
        b: Denominator
    Returns:
        Result of division or None if division by zero
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
