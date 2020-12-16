#!/usr/bin/python3
def multiple_returns(sentence):
    blank = None
    length = len(sentence)
    char = sentence[0]
    if length > 0:
        blank = char
    return length, char
