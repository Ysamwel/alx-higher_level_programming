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
        """width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        """"value of width."""
        self.__width = value

    @property
    def height(self):
        """height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """"value of height."""
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """x of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """"value of x."""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """y of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """"value of y."""
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """validation method for value"""
        """if type(value) != int:"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be >= 0".format(name))
