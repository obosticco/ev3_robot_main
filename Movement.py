#!/usr/bin/env python3
from math import pi
from Position import *
from ev3dev2.motor import MoveTank, LargeMotor
from ev3dev2.sensor.lego import GyroSensor, ColorSensor, UltrasonicSensor

tank_drive = MoveTank(left_motor_port="A", right_motor_port="D")
gyro = GyroSensor(address="1")
color = ColorSensor(address="2")
ultra = UltrasonicSensor(address="3")


def driveTo(posX, posY, iPosX, iPosY):
    gyro.calibrate

    rotationX = abs(posX - iPosX) / (1.602362 * pi)
    rotationY = abs(posY - iPosX) / (1.602362 * pi)
    iAngle = gyro.angle

    # Drive to Location
    tank_drive.on_for_rotations(35, 35, rotationY, rotationY)

    if (posX > iPosX):
        tank_drive.on(35, -35)
        gyro.wait_until_angle_changed_by(-90, True)
    else:
        tank_drive.on(-35, 35)
        gyro.wait_until_angle_changed_by(90, True)

    tank_drive.on_for_rotations(35, 35, rotationX, rotationX)
    ###################


def DriveToOtherHome(currHome, finalHome):
    tank_drive.on(35, -35)
    gyro.wait_until_angle_changed_by(180)

    # When traveling between Home A and C or Home B and D
    if currHome.posX == finalHome.posX:
        rotation = abs(finalHome.posY - currHome.posY) / (1.602362 * pi)
        tank_drive.on_for_rotations(35, 35, rotation, rotation)

    # When traveling between Home A and B or Home C and D
    elif currHome.posY == finalHome.posY:
        rotation = 6 / (1.602362 * pi)
        rotationX = abs(finalHome.posX - currHome.posX) / (1.602362 * pi)
        tank_drive.on_for_rotations(35, 35, rotation, rotation)

        if (finalHome.posX > currHome.posX):
            tank_drive.on(35, -35)
            gyro.wait_until_angle_changed_by(-90, True)
            tank_drive.on_for_rotations(35, 35, rotationX, rotationX)
            tank_drive.on(35, -35)
            gyro.wait_until_angle_changed_by(-90, True)

        else:
            tank_drive.on(-35, 35)
            gyro.wait_until_angle_changed_by(90, True)
            tank_drive.on_for_rotations(35, 35, rotationX, rotationX)
            tank_drive.on(-35, 35)
            gyro.wait_until_angle_changed_by(90, True)

        tank_drive.on_for_rotations(35, 35, rotation, rotation)

    # When traveling between Home A and D or Home B and C
    else:
        rotation = 6 / (1.602362 * pi)
        rotationX = abs(finalHome.posX - currHome.posX) / (1.602362 * pi)
        rotationY = (abs(finalHome.posY - currHome.posY) - 6) / (1.602362 * pi)
        tank_drive.on_for_rotations(35, 35, rotationY, rotationY)

        if (finalHome.posX > currHome.posX):
            tank_drive.on(35, -35)
            gyro.wait_until_angle_changed_by(-90, True)
            tank_drive.on_for_rotations(35, 35, rotationX, rotationX)
            tank_drive.on(-35, 35)
            gyro.wait_until_angle_changed_by(90, True)

        else:
            tank_drive.on(-35, 35)
            gyro.wait_until_angle_changed_by(90, True)
            tank_drive.on_for_rotations(35, 35, rotationX, rotationX)
            tank_drive.on(-35, 35)
            gyro.wait_until_angle_changed_by(90, True)

        tank_drive.on_for_rotations(35, 35, rotation, rotation)
