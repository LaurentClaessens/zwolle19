"""Define a card."""


# pylint: disable=too-many-arguments
# pylint: disable=too-few-public-methods


class Card:
    """
    Represent a small square.

    A square has a fixes orientation. In order to 'simulate'
    the possible orientations, we will just duplicate the squares.
    """

    def __init__(self, ident, north, south, west, east):
        """
        Initiate the square by giving its 'labels'.

        The identifier is needed to identify the cards which are,
        in fact, the same after orientation variation. See the method
        `Package.subset_three`.
        """
        self.ident = ident
        self.north = north
        self.south = south
        self.west = west
        self.east = east

    def variations(self):
        """Return the list of 4 square with different orientations"""
        return [Card(self.ident, self.north, self.south,
                     self.west, self.east),
                Card(self.ident, self.west, self.east,
                     self.south, self.north),
                Card(self.ident, self.south, self.north,
                     self.east, self.west),
                Card(self.ident, self.east, self.west,
                     self.north, self.south)
                ]

    def __str__(self):
        return f"{self.ident}({self.north}, {self.south}, {self.west}, {self.east})"
