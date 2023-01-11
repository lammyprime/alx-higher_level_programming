#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniquelist = list(set(my_list))
    sumof = 0
    for i in range(len(uniquelist)):
        sumof += uniquelist[i]
    return sumof
