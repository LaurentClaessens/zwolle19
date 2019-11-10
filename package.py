"""Define the card package."""

from tools import is_ok_line
from tools import is_ok_two_lines
from tools import is_ok_three_lines
from tools import show_double

dprint = print  #pylint: disable=invalid-name, unused-variable


class Package:
    """Represent the full list of cards."""

    def __init__(self, base_list):
        """
        Initiate with a list of cards.

        The given list is the list of cards given by Zwolle. Here
        we variate the orientations to create the full card package.
        """
        self.base_list = base_list
        self.full_list = []
        for card in self.base_list:
            self.full_list.extend(card.variations())
        self.index = 0

    def subsets_three(self):
        """
        Yield all the possibilities of subsets of 3 cards.

        No repetitions.
        """
        package0 = self
        for card1 in package0:
            package1 = package0.remove_ident(card1.ident)
            for card2 in package1:
                package2 = package1.remove_ident(card2.ident)
                for card3 in package2:
                    yield([card1, card2, card3])

    def possible_lines(self):
        """Return the list of possible lines."""
        lines = []
        for line in self.subsets_three():
            if is_ok_line(line):
                lines.append(line)
        return lines

    def possible_two_lines(self):
        """
        Return the possible blocks of two lines.

        Each element is a tuple of 2 list of cards.
        """
        doubles = []
        for line1 in self.possible_lines():
            for line2 in self.possible_lines():
                if is_ok_two_lines(line1, line2):
                    show_double(line1, line2)
                    doubles.append((line1, line2))
        return doubles

    def possible_three_lines(self):
        """Return the list of possible 3 lines."""
        triples = []
        for line1, line2 in self.possible_two_lines():
            show_double(line1, line2)
            for line3 in self.possible_lines():
                if is_ok_three_lines(line1, line2, line3):
                    print("Une de trouvé")
                    triples.append((line1, line2, line3))
        return triples

    def remove_ident(self, ident):
        """Return a new package, with the given ident removed."""
        new_base_list = [card for card in self.base_list
                         if card.ident != ident]
        return Package(new_base_list)

    def length(self):
        """Return the number of cards in self."""
        return len(self.full_list)

    def __iter__(self):
        """Make the card package itarable."""
        return self

    def __next__(self):
        """Iterate over self's full card list."""
        self.index += 1
        try:
            return self.full_list[self.index-1]
        except IndexError:
            self.index = 0
            raise StopIteration  # Done iterating.
