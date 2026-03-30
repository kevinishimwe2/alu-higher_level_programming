#!/usr/bin/python3
"""Module for writing a string to a text file."""


def write_file(filename="", text=""):
    """Write text to a UTF8 file and return number of chars written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
