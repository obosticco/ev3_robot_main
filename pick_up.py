#!/usr/bin/env python3
from math import pi
from ev3dev2.motor import MoveTank, LargeMotor, Motor
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor, ColorSensor
from ev3dev2.display import *
import time

liftDrive = Motor("C")
color = ColorSensor(address="2")
display = Display()


def lift(degrees):
    liftDrive.on_for_degrees(20, degrees)


def drop(degrees):
    liftDrive.on_for_degrees(15, degrees)


def scan(box):
    lift(-100)
    if (color.ambient_light_intensity == 0):
        c1 = True
    else:
        c1 = False
    lift(-100)
    time.sleep(1)
    if (color.ambient_light_intensity == 0):
        c2 = True
    else:
        c2 = False
    lift(-100)
    time.sleep(1)
    if (color.ambient_light_intensity == 0):
        c3 = True
    else:
        c3 = False
    lift(-100)
    time.sleep(1)
    if (color.ambient_light_intensity == 0):
        c4 = True
    else:
        c4 = False
    drop(500)

    if (c1 and (not c2) and (not c3) and (not c4)):
        if box == "B1":
            display.text_pixels("Box 1: Correct Box")
        else:
            display.text_pixels("Box 1: Incorrect Box")
    elif (c1 and (not c2) and c3 and (not c4)):
        if box == "B2":
            display.text_pixels("Box 2: Correct Box")
        else:
            display.text_pixels("Box 2: Incorrect Box")
    elif (c1 and c2 and c3 and (not c4)):
        if box == "B3":
            display.text_pixels("Box 3: Correct Box")
        else:
            display.text_pixels("Box 3: Incorrect Box")
    elif (c1 and (not c2) and (not c3) and c4):
        if box == "B4":
            display.text_pixels("Box 4: Correct Box")
        else:
            display.text_pixels("Box 4: Incorrect Box")
    else:
        display.text_pixels("Invalid")
    display.update()


# scan("B1")
