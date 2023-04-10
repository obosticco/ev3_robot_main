#!/usr/bin/env python3
from math import pi
from ev3dev2.motor import MoveTank, LargeMotor, Motor
from ev3dev2.sensor.lego import GyroSensor

liftDrive = Motor("C")
#tank_drive = MoveTank(left_motor_port="A", right_motor_port="D")

laps = 1   # int(input("Enter the number of laps: "))
length = 30.48  # float(input("Enter the length: "))

# distance required to go divided by wheels circumference
rotations = length / (5.3975 * pi)

#tank_drive.on_for_rotations(25, 25, rotations)
liftDrive.on_for_rotations(-100, 4)

#tank_drive.on_for_rotations(-25, -25, rotations)
#liftDrive.on_for_rotations(10, 1.5)
