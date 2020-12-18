#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key:
        result = a_dictionary.pop(key, None)
        return result
