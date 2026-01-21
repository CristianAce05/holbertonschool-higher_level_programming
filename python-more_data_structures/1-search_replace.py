#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Returns a new list where all occurrences of `search` are replaced
    with `replace`.
    """
    new_list = [replace if x == search else x for x in my_list]
    return new_list
