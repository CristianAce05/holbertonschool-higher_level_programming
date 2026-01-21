#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of elements present in only one of the two sets.
    """
    return set_1 ^ set_2
