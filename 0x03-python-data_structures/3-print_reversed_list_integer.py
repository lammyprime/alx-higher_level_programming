#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rangelist = len(my_list) + 1
    for i in range(-1, -rangelist, -1):
        print('{}'.format(i))
