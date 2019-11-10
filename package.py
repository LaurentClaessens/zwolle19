"""Define the card package."""


dprint = print


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
        dprint("package0", package0.length())
        for card1 in package0:
            package1 = package0.remove_ident(card1.ident)
            dprint("package1", package1.length())
            for card2 in package1:
                package2 = package1.remove_ident(card2.ident)
                dprint("package2", package2.length())
                for card3 in package2:
                    yield([card1, card2, card3])

    def possible_lines(self):
        """Return the list of possible lines."""
        for line in self.subset_three():
            if is_ok_line(line):
                yield line

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
