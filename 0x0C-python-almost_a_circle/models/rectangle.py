#!/usr/bin/python3
"""Rectangle class module."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The constructor."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """gets height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of the rectangle."""
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """gets x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x-coordinate of the rectangle."""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """gets y-coordinate  of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y-coodinate of the rectangle."""
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """validates if the value is an integer"""
        """if type(value) != int:"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        if not eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
