"""Define a card."""


class Card:
    """
    Represent a small square.

    A square has a fixes orientation. In order to 'simulate'
    the possible orientations, we will just duplicate the squares.
    """

    def __init__(self, ident, north, south, east, west):
        """
        Initiate the square by giving its 'labels'.

        The identifier is needed to identify the cards which are, 
        in fact, the same after orientation variation. See the method
        `Package.subset_three`.

        """
        self.ident = ident
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def variations(self):
        """Return the list of 4 square with different orientations"""
        return [Card(self.ident, self.north, self.south,
                     self.east, self.west),
                Card(self.ident, self.east, self.west,
                     self.south, self.north),
                Card(self.ident, self.south, self.north,
                     self.west, self.east),
                Card(self.ident, self.west, self.east,
                     self.north, self.south)
                ]
