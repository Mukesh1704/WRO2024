#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


def Follow_Line_Distance(distance):
    BLACK = 9
    WHITE = 85
    threshold = (BLACK + WHITE) / 2
    DRIVE_SPEED = 100
    PROPORTIONAL_GAIN = 1.2

    while robot.distance >= distance:
        deviation = line_sensor.reflection() - threshold
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)
        wait(10)




# Create your objects here.
ev3 = EV3Brick()
Motor_left = Motor(Port.A,positive_direction=Direction.CLOCKWISE, gears=None)
Motor_right = Motor(Port.D,positive_direction=Direction.CLOCKWISE, gears=None)
Motor_y = Motor(Port.B,positive_direction=Direction.CLOCKWISE, gears=[24]) #Werte nur Beispiel
Motor_x = Motor(Port.C,positive_direction=Direction.CLOCKWISE, gears=[24]) #Werte nur Beispiel
Robot = DriveBase(Motor_left,Motor_right,90,120) # Werte nur beispiel
color1 = ColorSensor(Port.S1)
color2 = ColorSensor(Port.S2)
gyro = GyroSensor(Port.S3)
distance = UltrasonicSensor(Port.S4)


# Write your program here.
while color1.reflection() >= 15:
    Robot.drive(50,16)
