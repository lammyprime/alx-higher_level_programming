#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lenlist = len(my_list)
    if lenlist != 0:
        newlist = []
    for i in my_list:
        if i % 2 == 0:
            newlist += [True]
        elif i % 2 != 0:
            newlist += [False]
    return newlist    
