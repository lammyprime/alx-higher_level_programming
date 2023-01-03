#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of {} is {} and is {}"
if number < 0:
    lastdigit = number % -10
else:
    lastdigit = number % 10
if lastdigit > 5:
    print(str.format(number, lastdigit, ("greater than 5")))
elif lastdigit == 0:
    print(str.format(number, lastdigit, ("0")))
elif lastdigit < 6:
    print(str.format(number, lastdigit, ("less than 6 and not 0")))
