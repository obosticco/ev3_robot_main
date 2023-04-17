#!/usr/bin/env python3
from Position import *
from Movement import *

positions = createPositionsArray()
code = "A1_12"
row, col = decode(code)

rotation = positions[row][col].posX / (2.16 * pi)
drive(rotation)
turn_right()
getBox()
scan("B3")
