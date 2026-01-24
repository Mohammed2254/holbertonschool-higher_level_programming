#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Convert Roman numeral to integer
    Args:
        roman_string: Roman numeral string
    Returns:
        Integer value or 0 if invalid input
    """
    if not roman_string or not isinstance(roman_string, str):
        return 0
    romdict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev_value = 0
    for char in reversed(roman_string):
        current_value = romdict.get(char, 0)
        if current_value >= prev_value:
            total += current_value
        else:
            total -= current_value
        prev_value = current_value
    return total
