#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    noice = []
    for i in my_list:
        if i % 2 == 0:
            noice.append(True)
        else:
            noice.append(False)
    return noice
