#!/usr/bin/python3
def square(x):
    return x**2


def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        new += [list(map(square, i))]
    return new
