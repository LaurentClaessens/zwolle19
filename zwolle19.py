#!venv/bin/python3

"""Try a brute force solution for Zwolle 19."""

from card import Card
from package import Package

c1 = Card("ident1", "a", "b", "c", "d")
c2 = Card("ident2", "1", "2", "3", "4")
c3 = Card("ident3", "N", "S", "E", "W")

package = Package([c1, c2, c3])
for card in package:
    print(card)

print("Les lignes")
for line in package.subsets_three():
    n+=1
    print(line[0].ident, line[1].ident, line[2].ident)
