#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lastInteger = number % -10
else:
    lastInteger = number % 10

if lastInteger > 5:
    print("Last digit of {} is {} and\
 is greater than 5".format(number, lastInteger))

elif number % 10 == 0:
    print("Last digit of {} is {} and is 0".format(number, lastInteger))

elif lastInteger < 6 and number != 0:
    print("Last digit of {} is {} and\
 is less than 6 and not 0".format(number, lastInteger))
