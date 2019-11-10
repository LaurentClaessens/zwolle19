"""Some tools for Zwolle19."""

def is_ok_line(line):
    """
    Say if the given line is ok.

    @param {list of Card} `line`
    """
    card1 = line[0]
    card2 = line[1]
    card3 = line[2]

    if card1.west != card2.east:
        return False
    if card2.west != card3.east:
        return False
    return True
