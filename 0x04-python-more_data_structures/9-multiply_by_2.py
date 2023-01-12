#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdictionary = a_dictionary.copy()
    for i in newdictionary:
        newdictionary[i] *= 2
    return newdictionary
