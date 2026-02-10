#!/usr/bin/python3
"""Module to serialize a Python dictionary to XML and deserialize back."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The Python dictionary to serialize.
        filename (str): The file name to save the XML data.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, "item", key=str(key))
        # Store type to help during deserialization
        if isinstance(value, bool):
            item.set("type", "bool")
            item.text = str(value)
        elif isinstance(value, int):
            item.set("type", "int")
            item.text = str(value)
        elif isinstance(value, float):
            item.set("type", "float")
            item.text = str(value)
        else:
            item.set("type", "str")
            item.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file to a Python dictionary.

    Args:
        filename (str): The XML file to read.

    Returns:
        dict: The reconstructed Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        dictionary = {}

        for item in root.findall("item"):
            key = item.get("key")
            typ = item.get("type", "str")
            text = item.text

            # Convert text back to original type
            if typ == "bool":
                value = text == "True"
            elif typ == "int":
                value = int(text)
            elif typ == "float":
                value = float(text)
            else:
                value = text

            dictionary[key] = value

        return dictionary

    except (ET.ParseError, FileNotFoundError):
        return {}
