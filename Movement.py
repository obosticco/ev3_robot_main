#!/usr/bin/env python3
from math import pi
from Position import *
from pick_up import *
from ev3dev2.motor import MoveTank, MoveSteering, LargeMotor, SpeedPercent
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor

correction_drive = MoveSteering(left_motor_port="A", right_motor_port="D")
correction_drive.gyro = GyroSensor(address="1")

ultra = UltrasonicSensor(address="3")


def drive(rotations):
    target = correction_drive.gyro.angle
    correction_drive.right_motor.position = 0
    error = 0
    last_error = 0
    integral = 0
    derivative = 0
    kp = 0.20
    kd = 0.05
    ki = 0.22
    while ((correction_drive.right_motor.position / 360) < rotations):
        while (ultra.distance_inches < 6):
            correction_drive.off()

        currDegree = correction_drive.gyro.angle
        error = target - currDegree
        if (error == 0):  # prevent the integral term from 'overshooting'
            integral = 0
        else:
            integral = integral + error
        derivative = error - last_error

        steer = (error * kp) + (integral * ki) + + (derivative * kd)
        print(steer)
        correction_drive.on(steer, 35)
        last_error = error
    correction_drive.off()


def turn_right():
    iAngle = correction_drive.gyro.angle
    while (abs(correction_drive.gyro.angle - iAngle) < 90):
        correction_drive.on(100, 10)
    correction_drive.off()


def turn_left():
    iAngle = correction_drive.gyro.angle
    while (abs(correction_drive.gyro.angle - iAngle) < 82):
        correction_drive.on(-100, 10)
    correction_drive.off()


def turn_around():
    iAngle = correction_drive.gyro.angle
    while (abs(correction_drive.gyro.angle - iAngle) < 180):
        correction_drive.on(-100, 10)
    correction_drive.off()
    time.sleep(0.25)


def back_up():
    rotation = 6 / (2.16 * pi)
    correction_drive.on_for_rotations(0, -20, rotation)


def driveTo(posX, posY, iPosX, iPosY):
    # correction_drive.gyro.calibrate()

    rotationX = abs(posX - iPosX) / (2.16 * pi)
    rotationY = abs(posY - iPosY) / (2.16 * pi)

    # Drive to Location
    drive(rotationY)
    if (posX > iPosX):
        if (posY > iPosY):
            turn_right()
        else:
            turn_left()
    else:
        if (posY < iPosY):
            turn_right()
        else:
            turn_left()
    drive(rotationX)
    ###################


def driveFrom(posX, posY, iPosX, iPosY):
    # correction_drive.gyro.calibrate()

    rotationX = abs(posX - iPosX) / (2.16 * pi)
    rotationY = abs(posY - iPosY) / (2.16 * pi)

    # Drive to Location
    drive(rotationX)
    if (posX > iPosX):
        if (posY < iPosY):
            turn_right()
        else:
            turn_left()
    else:
        if (posY > iPosY):
            turn_right()
        else:
            turn_left()
    drive(rotationY)
    ###################


def DriveToOtherHome(iPosX, iPosY, fPosX, fPosY):
    turn_around()
    # When traveling between Home A and C or Home B and D
    if iPosX == fPosX:
        rotation = abs(fPosY - iPosY) / (2.16 * pi)
        drive(rotation)

    # When traveling between Home A and B or Home C and D
    elif iPosY == fPosY:
        rotation = 6 / (2.16 * pi)
        rotationX = abs(fPosX - iPosX) / (2.16 * pi)
        drive(rotation)

        if (fPosX < iPosX):
            turn_right()
            drive(rotationX)
            turn_right()

        else:
            turn_left()
            drive(rotationX)
            turn_left()

        drive(rotation)

    # When traveling between Home A and D or Home B and C
    else:
        rotation = 6 / (2.16 * pi)
        rotationX = abs(fPosX - iPosX) / (2.16 * pi)
        rotationY = (abs(fPosY - iPosY) - 6) / (2.16 * pi)
        correction_drive.on_for_rotations(35, 35, rotationY)

        if (fPosX < iPosX):
            turn_right()
            drive(rotationX)
            turn_right()

        else:
            turn_left()
            drive(rotationX)
            turn_left()

        drive(rotation)


def getBox():
    while (ultra.distance_inches > 1.2):
        correction_drive.on(0, 5)
    correction_drive.off()
