#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (each integer counted only once).
    """
    unique = set(my_list)
    return sum(unique)
