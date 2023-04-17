#!/usr/bin/env python3
from Position import *
from Movement import *
import time


def Subtask1(position, iPosX, iPosY, fPosX, fPosY):
    driveTo(position.posX, position.posY, iPosX, iPosY)
    time.sleep(5)
    driveFrom(fPosX, fPosY, position.posX, position.posY)


positions = createPositionsArray()

code = "A1_12"  # input("Please enter box location code (Ex. A#_##): ")
row, col = decode(code)
Subtask1(positions[row][col], 0, 0, 96, 0)
