#!/usr/bin/env python3
class Position:
    def __init__(self, posX, posY, identity):
        self.posX = posX
        self.posY = posY
        self.idenity = identity

################################################


# Decode box location
def decode(input):
    if (input[0] + input[1] == 'A1'):
        y = 1
        x = 0
    elif (input[0] + input[1] == 'A2'):
        y = 2
        x = 0
    elif (input[0] + input[1] == 'C1'):
        y = 3
        x = 0
    elif (input[0] + input[1] == 'C2'):
        y = 4
        x = 0
    elif (input[0] + input[1] == 'B1'):
        y = 1
        x = 7
    elif (input[0] + input[1] == 'B2'):
        y = 2
        x = 7
    elif (input[0] + input[1] == 'D1'):
        y = 3
        x = 7
    elif (input[0] + input[1] == 'D2'):
        y = 4
        x = 7

    if (int(input[3] + input[4]) >= 1 and int(input[3] + input[4]) <= 6):
        x += int(input[3] + input[4])
    else:
        y += 1
        x += (int(input[3] + input[4]) - 6)

    return x, y

##################################################################


# Get Position Data from txt file and put into Array
def createPositionsArray():
    PositionData = open("PositionData.txt", "r")
    rows, cols = (15, 7)
    positions = [[Position(0, 0, "") for i in range(cols)]
                 for i in range(rows)]

    for i in PositionData:
        r = i.split()
        tPos = Position(int(r[2]), int(r[3]), r[4])
        positions[int(r[0])][int(r[1])] = tPos

    PositionData.close
    return positions

################################################
