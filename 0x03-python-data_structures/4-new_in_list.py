#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        copy = my_list[:]
        if idx < 0:
            return copy
        elif idx >= len(my_list):
            return copy
        else:
            copy[idx] = element
            return copy