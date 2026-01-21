#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value in a dictionary.
    If the dictionary is empty or None, returns None.
    """
    if not a_dictionary:
        return None

    best_key = None
    best_value = float('-inf')  # smallest possible number

    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key

    return best_key
