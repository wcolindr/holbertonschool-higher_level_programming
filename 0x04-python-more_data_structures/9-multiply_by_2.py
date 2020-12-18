#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newMe = dict(a_dictionary)
    for key in a_dictionary:
        newMe[key] *= 2
    return newMe
