#!/usr/bin/python3
"""Module that defines a Square class with its own string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square with its own [Square] w/h string representation."""

    def __init__(self, size):
        """Initialize Square with a validated private size.

        Args:
            size (int): The side length of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return a string description of the square in [Square] w/h format."""
        return "[Square] {}/{}".format(self.__size, self.__size)
