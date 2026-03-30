#!/usr/bin/python3
"""Module that defines BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """A base class for geometry objects with an area interface."""

    def area(self):
        """Raise an exception since area is not implemented in the base class."""
        raise Exception("area() is not implemented")
