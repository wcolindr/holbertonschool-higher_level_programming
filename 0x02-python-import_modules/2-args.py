#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)

    if length == 1:
        print("0 arguments.")

    elif length == 2:
        print("1 argument:")
        print("{}: {}".format(length - 1, argv[1]))

    else:
        print("{} arguments:".format(length - 1))
        for count in range(1, length):
            print("{}: {}".format(count, argv[count]))
