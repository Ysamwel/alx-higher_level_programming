#!/usr/bin/python3
"""
This mode has one function "add_integer" 
"add_integer" checks if a and b are integers or float then
adds them up
"""


def add_integer(a, b=98):
    """Return the addition of two integers/float.
	    
    Arguments: a :b
	Result: addition of the arguments"""

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
