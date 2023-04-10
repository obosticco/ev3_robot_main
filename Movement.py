#!/usr/bin/env python3
from math import pi
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
