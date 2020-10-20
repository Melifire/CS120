""" File: prob2.py
    Author: Ben Kruse
    Purpose: Has a color class that takes in rgb values and allows 
    modifications to be made to them
"""

def bound_color(*values):  # the * means not limited to any number of inputs
    return ((min(max(value, 0), 255)) for value in values)

class Color():

    def __init__(self, r, g, b):
        self._r, self._g, self._b = bound_color(r, g, b)

    def __str__(self):
        return ("rgb({},{},{})"
            .format(self._r, self._g, self._b))

    def html_hex_color(self):
        # {:02X} gives the number as a 2 digit hex
        return ("#{:02X}{:02X}{:02X}"
            .format(self._r, self._g, self._b))

    def get_rgb(self):
        return (self._r, self._g, self._b)

    def set_color_by_tuple(self, tuple):
        # this function is used to each value doesnt have to be changed indv.
        self._r, self._g, self._b = tuple

    def set_standard_color(self, name):
        name = name.lower()
        if name == 'red':
            self.set_color_by_tuple((255, 0, 0))
        elif name == 'yellow':
            self.set_color_by_tuple((255, 255, 0))
        elif name == 'white':
            self.set_color_by_tuple((255, 255, 255))
        elif name == 'black':
            self.set_color_by_tuple((0, 0, 0))
        else:
            # if none of the names match, throw an error
            assert True

    def remove_red(self):
        self._r = 0
