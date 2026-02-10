#!/usr/bin/python3
"""Return the dictionary description of a class instance for JSON serialization."""


def class_to_json(obj):
    """Return a dictionary of all serializable attributes of an object."""
    return obj.__dict__.copy()
