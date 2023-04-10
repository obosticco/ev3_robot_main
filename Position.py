#!/usr/bin/env python3
class Position:
    def __init__(self, posX, posY, identity):
        self.posX = posX
        self.posY = posY
        self.idenity = identity

################################################


# Decode box location
def decode(input):
    match(input[0] + input[1]):
        case 'A1':
            row = 1
            col = 0
        case 'A2':
            row = 2
            col = 0
        case 'C1':
            row = 3
            col = 0
        case 'C2':
            row = 4
            col = 0
        case 'B1':
            row = 1
            col = 7
        case 'B2':
            row = 2
            col = 7
        case 'D1':
            row = 3
            col = 7
        case 'D2':
            row = 4
            col = 7

    if (int(input[3] + input[4]) >= 1 and int(input[3] + input[4]) <= 6):
        col += int(input[3] + input[4])
    else:
        row += 1
        col += (int(input[3] + input[4]) - 6)

    return row, col

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
