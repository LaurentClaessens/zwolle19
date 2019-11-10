#!venv/bin/python3

"""Try a brute force solution for Zwolle 19."""

from card import Card
from package import Package


def do_work():
    """Do the brute force work."""
    package = Package(
        [
            Card(1, "S jaune", "L blanche", "S orange", "L mauve"),
            Card(2, "S jaune", "L bleue", "L verte", "S rouge"),
            Card(3, "S orange", "L verte", "L bleue", "S rouge"),
            Card(4, "L verte", "S noir", "S orange", "L blanche"),
            Card(5, "L verte", "S noir", "L blanche", "S rouge"),
            Card(6, "S jaune", "L blanche", "S jaune", "L bleue"),
            Card(7, "S orange", "L blanche", "L blanche", "S rouge"),
            Card(8, "S orange", "L bleue", "S noir", "L mauve"),
            Card(9, "L bleue", "S rouge", "L mauve", "S jaune")
        ]
    )

    print("Les lignes")
    for line in package.possible_lines():
        print(line[0].ident, line[1].ident, line[2].ident)

do_work()
