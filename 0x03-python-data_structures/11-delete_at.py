#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        if idx < 0:
            return
        elif idx >= len(my_list):
            return
        else:
            my_list.remove(idx+1)
            return my_list
