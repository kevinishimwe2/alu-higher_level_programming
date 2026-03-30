#!/usr/bin/python3
"""Module that defines BaseGeometry with area and integer_validator methods."""


class BaseGeometry:
    """A base class for geometry objects with validation and area interface."""

    def area(self):
        """Raise an exception since area is not implemented in the base class."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): The name of the parameter (assumed to always be a string).
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
