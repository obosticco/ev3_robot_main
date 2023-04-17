#!/usr/bin/env python3
from Position import *
from Movement import *

positions = createPositionsArray()
code = "A1_12"
row, col = decode(code)

rotations = abs(96 - positions[row][col].posX) / (2.16 * pi)
lift(-100)
back_up()
turn_left()
time.sleep(0.1)
drive(rotations)
drop(700)
back_up()
