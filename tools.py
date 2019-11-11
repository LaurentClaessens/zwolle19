"""Some tools for Zwolle19."""

dprint = print  #pylint: disable=invalid-name, unused-variable


def is_coupled(label1, label2):
    """Say if the given two labels are coupled."""
    #couples = [{"G", "H"}, {"C", "E"}, {"A", "D"}, {"B", "F"}]
    couples = [{"G", "H"}, {"C", "D"}, {"A", "E"}, {"B", "F"}]

    for couple in couples:
        if {label1, label2} in couples:
            return True
    return False

def is_ok_line(line):
    """
    Say if the given line is ok.

    @param {list of Card} `line`
    """
    card1 = line[0]
    card2 = line[1]
    card3 = line[2]

    if not is_coupled(card1.east, card2.west):
        return False
    if not is_coupled(card2.east, card3.west):
        return False
    return True


def is_ok_two_lines(line1, line2):
    """
    Say if `line2` can be bellow `line1`

    - check that the two lines do not contain the same identifiers
    - check that the labels match
    """
    card1 = line1[0]
    card2 = line1[1]
    card3 = line1[2]
    card4 = line2[0]
    card5 = line2[1]
    card6 = line2[2]
    idents1 = [card.ident for card in line1]
    idents2 = [card.ident for card in line2]
    intersection = list(set(idents1) & set(idents2))
    if intersection:
        return False
    if not is_coupled(card1.south, card4.north):
        return False
    if not is_coupled(card2.south, card5.north):
        return False
    if not is_coupled(card3.south, card6.north):
        return False
    return True


def is_ok_three_lines(line1, line2, line3):
    """
    Say if `line2` can be bellow `line1` and `line3` bellow `line2`  

    - check that the two lines do not contain the same identifiers
    - check that the labels match
    """
    card1 = line1[0]
    card2 = line1[1]
    card3 = line1[2]
    card4 = line2[0]
    card5 = line2[1]
    card6 = line2[2]

    card7 = line3[0]
    card8 = line3[1]
    card9 = line3[2]
    idents1 = [card.ident for card in line1]
    idents2 = [card.ident for card in line2]
    idents3 = [card.ident for card in line3]

    intersection = list(set(idents1) & set(idents2))
    if intersection:
        dprint("intersection 12")
        return False

    intersection = list(set(idents1) & set(idents3))
    if intersection:
        return False

    intersection = list(set(idents2) & set(idents3))
    if intersection:
        return False

    print("??????????????")
    show_triple(line1, line2, line3)
    print("??????????????")

    if not is_ok_two_lines(line1, line2):
        return False
    if not is_ok_two_lines(line2, line3):
        return False

    return True


def show_double(line1, line2):
    """Show the two lines."""
    card1 = line1[0]
    card2 = line1[1]
    card3 = line1[2]
    card4 = line2[0]
    card5 = line2[1]
    card6 = line2[2]
    print("---")
    print(card1, card2, card3)
    print(card4, card5, card6)


def show_triple(line1, line2, line3):
    """Show the three lines."""
    card1 = line1[0]
    card2 = line1[1]
    card3 = line1[2]
    card4 = line2[0]
    card5 = line2[1]
    card6 = line2[2]
    card7 = line3[0]
    card8 = line3[1]
    card9 = line3[2]
    print(card1.ident, card2.ident, card3.ident)
    print(card4.ident, card5.ident, card6.ident)
    print(card7.ident, card8.ident, card9.ident)
    print(card1, card2, card3)
    print(card4, card5, card6)
    print(card7, card8, card9)
