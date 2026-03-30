#!/usr/bin/python3
"""Module for converting a class instance to a JSON-safe dictionary."""


def class_to_json(obj):
    """Return a dictionary of an object's attributes for JSON serialization."""
    return obj.__dict__
