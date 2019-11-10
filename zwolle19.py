#!venv/bin/python3

"""Try a brute force solution for Zwolle 19."""

from card import Card
from package import Package
from tools import show_triple

dprint = print  #pylint: disable=invalid-name, unused-variable


def do_work():
    """Do the brute force work."""
    package = Package(
        [
            Card(1, "A", "E", "B", "D"),
            Card(2, "A", "F", "H", "G"),
            Card(3, "B", "H", "F", "G"),
            Card(4, "E", "B", "H", "C"),
            Card(5, "G", "E", "H", "C"),
            Card(6, "E", "G", "D", "A"),
            Card(7, "B", "E", "E", "G"),
            Card(8, "B", "F", "C", "D"),
            Card(9, "A", "E", "A", "F")
        ]
    )

    possible_three = package.possible_three_lines()

    print("Liste des résultats")
    for line1, line2, line3 in possible_three:
        show_triple(line1, line2, line3)

do_work()
