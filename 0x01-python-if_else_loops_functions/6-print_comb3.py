#!/usr/bin/python3
for firstInt in range(0, 10):
    for secInt in range(0, 10):
        if firstInt == secInt or firstInt > secInt:
            pass
        elif firstInt == 8 and secInt == 9:
            print("{}{}".format(firstInt, secInt))
        else:
            print("{}{}".format(firstInt, secInt), end=", ")
