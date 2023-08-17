#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique = 0
    for element in set(my_list):
        unique += element
    return unique
