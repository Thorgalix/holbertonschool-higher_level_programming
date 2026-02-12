#!/usr/bin/python3
"""
Module for serializing and deserializing Python dictionaries to and from XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Each key-value pair in the dictionary becomes a child element
    of the root <data> element. The key is used as the tag name,
    and the value is converted to a string and stored as the text
    of the element.

    Args:
        dictionary (dict): The dictionary to serialize. Keys should
                           be strings; values can be of any type.
        filename (str): The path to the output XML file.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ", level=0)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file back into a Python dictionary.

    Assumes that the XML file has a root <data> element, with
    child elements representing key-value pairs. The tag name
    of each child becomes the key in the dictionary, and the
    text of the child element becomes the value (as a string).

    Args:
        filename (str): The path to the XML file to read.

    Returns:
        dict: A dictionary containing the key-value pairs from
              the XML file, with all values as strings.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
