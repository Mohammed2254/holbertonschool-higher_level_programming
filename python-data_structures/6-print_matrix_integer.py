#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for row in matrix:
        for j in range(len(row)):
            if j == len(row) - 1:
                print("{:d}".format(row[j]), end="")
            else:
                print("{:d}".format(row[j]), end=" ")
        print()
