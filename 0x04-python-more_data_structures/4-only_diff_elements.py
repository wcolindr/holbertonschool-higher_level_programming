#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    my_set = set(set_1) ^ set(set_2)
    return my_set
