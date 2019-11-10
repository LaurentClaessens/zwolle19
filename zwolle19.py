#!/usr/bin/python3

"""Try a brute force solution for Zwolle 19."""


class Square:
    """
    Represent a small square.

    A square has a fixes orientation. In order to 'simulate'
    the possible orientations, we will just duplicate the squares.
    """

    def __init__(self, north, south, east, west):
        """Initiate the square by giving its 'labels'."""
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def variations(self):
        """Return the list of 4 square with different orientations"""
        return [Square(self.north, self.south, self.east, self.west),
                Square(self.east, self.west, self.south, self.north),
                Square(self.south, self.north, self.west, self.east),
                Square(self.west, self.east, self.north, self.south)
                ]
