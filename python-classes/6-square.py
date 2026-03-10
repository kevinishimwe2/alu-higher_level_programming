#!/usr/bin/python3
"""Module that defines a Square class with position functionality."""


class Square:
    """A class that defines a square by its size and position.
    
    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The position of the square (private).
    """
    
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.
        
        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position
    
    @property
    def size(self):
        """Get the size of the square.
        
        Returns:
            int: The size of the square.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """Set the size of the square with validation.
        
        Args:
            value (int): The new size of the square.
            
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @property
    def position(self):
        """Get the position of the square.
        
        Returns:
            tuple: The position of the square.
        """
        return self.__position
    
    @position.setter
    def position(self, value):
        """Set the position of the square with validation.
        
        Args:
            value (tuple): The new position of the square.
            
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        """Calculate and return the area of the square.
        
        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
    
    def my_print(self):
        """Print the square using the # character with position offset.
        
        If size is 0, prints an empty line.
        Position[0] adds horizontal spaces before each row.
        Position[1] adds vertical newlines before the square.
        """
        if self.__size == 0:
            print()
        else:
            # Print vertical offset (position[1] empty lines)
            for i in range(self.__position[1]):
                print()
            # Print each row of the square with horizontal offset
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
