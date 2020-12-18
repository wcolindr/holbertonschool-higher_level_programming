#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, idx in list(a_dictionary.items()):
        if value == idx:
            del a_dictionary[key]
    return a_dictionary
