#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if not my_list:
        print("Empty list!")
    else:  
        print('{0}\n{1}\n{2}\n{3}\n{4}'.format(*my_list))
