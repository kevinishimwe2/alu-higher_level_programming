#!/usr/bin/python3
"""Module that defines a Rectangle class with square factory method"""


class Rectangle:
    """Rectangle class with private width and height attributes

    Attributes:
        number_of_instances (int): number of Rectangle instances
        print_symbol: symbol used for string representation (default #)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance

        Args:
            width (int): width of the rectangle (default 0)
            height (int): height of the rectangle (default 0)
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute with validation

        Args:
            value (int): width value

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute with validation

        Args:
            value (int): height value

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the rectangle perimeter

        Returns 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of the rectangle

        Uses print_symbol for the representation.
        Returns empty string if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)
        rectangle = []
        for i in range(self.__height):
            rectangle.append(symbol * self.__width)
        return "\n".join(rectangle)

    def __repr__(self):
        """Return official string representation to recreate the instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print message when instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on area

        Args:
            rect_1: first Rectangle instance
            rect_2: second Rectangle instance

        Returns:
            The rectangle with the bigger area, or rect_1 if equal

        Raises:
            TypeError: if rect_1 or rect_2 is not a Rectangle instance
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a new Rectangle instance with width == height == size

        Args:
            size (int): size of the square (default 0)

        Returns:
            A new Rectangle instance with width == height == size
        """
        return cls(size, size)
