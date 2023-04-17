#!/usr/bin/env python3
from Position import *
from Movement import *

positions = createPositionsArray()
currHome, Home = positions[0][0], positions[14][0]
DriveToOtherHome(currHome.posX, currHome.posY, Home.posX, Home.posY)
