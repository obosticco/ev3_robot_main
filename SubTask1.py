from Position import *
from Movement import *
import time


def Subtask1(position, iPosX, iPosY, fPosX, fPosY):
    driveTo(position.posx, position.posY, iPosX, iPosY)
    time.sleep(5)
    driveTo(fPosX, fPosY, position.posx, position.posY)


positions = createPositionsArray()

code = input("Please enter box location code (Ex. A#_##): ")
row, col = decode(code)
Subtask1(positions[row][col], 0, 0, 96, 0)
