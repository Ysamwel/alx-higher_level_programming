#!/usr/bin/python3
"""The module of Base class for the rest of classes."""

class Base:
    """Representation of the Base class of hierarchy."""

    __nb_objects = 0
    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
