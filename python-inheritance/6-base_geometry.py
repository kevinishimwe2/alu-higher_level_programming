#!/usr/bin/python3
"""Module that defines BaseGeometry with an area method."""


class BaseGeometry:
    """A base class for geometry objects."""

    def area(self):
        """Raise an exception: area is not implemented."""
        raise Exception("area() is not implemented")
