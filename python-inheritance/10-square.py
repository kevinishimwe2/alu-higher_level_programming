#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square defined by a single private size, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize Square with a validated private size.

        Args:
            size (int): The side length of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
