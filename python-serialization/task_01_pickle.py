#!/usr/bin/python3
"""CustomObject class with pickle serialization and deserialization."""

import pickle


class CustomObject:
    """A custom Python object with name, age, and is_student attributes."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Whether the object is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the specified format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to a file using pickle.

        Args:
            filename (str): The file to save the object to.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a pickle file.

        Args:
            filename (str): The file to load the object from.

        Returns:
            CustomObject or None: Returns the loaded instance or None if error.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except (OSError, pickle.UnpicklingError):
            return None
