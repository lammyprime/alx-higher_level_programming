#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
       return my_list
    list_len = len(my_list)
    if idx > list_len:
        return my_list
    del my_list[idx]
    return my_list
