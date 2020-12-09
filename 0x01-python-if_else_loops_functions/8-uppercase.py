#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96:
            char = ord(i)
            if char > 96:
                char -= 32
                print("{:c}".format(char), end="")
                print()
