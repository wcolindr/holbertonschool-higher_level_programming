#!/usr/bin/python3
for decimal in range(0, 100):
    if decimal < 99:
        print("{:02d}".format(decimal), end=", ")
    else:
        print("{:02d}".format(decimal))
