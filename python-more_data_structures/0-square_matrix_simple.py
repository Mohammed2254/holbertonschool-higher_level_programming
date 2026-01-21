#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        new_row = []
        for n in row:
            new_row.append(n * n)
        new.append(new_row)
    return new
