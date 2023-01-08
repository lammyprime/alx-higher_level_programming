#!/usr/bin/python3
def no_c(my_string):
     string = ''
     for char in my_string:
          if char != "C" and char != "c":
               string += char
     return string
