#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divide element by element from two lists
    Args:
        my_list_1: First list
        my_list_2: Second list
        list_length: Number of elements to divide
    Returns:
        New list with division results
    """
    result_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result_list.append(result)
    return result_list
