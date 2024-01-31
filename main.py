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


# Create your objects here.
ev3 = EV3Brick()
lm = Motor(Port.A)
rm = Motor(Port.D)
robot = DriveBase(lm,rm, 55, 141)
gabelstapler = Motor(Port.B)
greifarm = Motor(Port.C)

# Write your program here.
#gabelstapler.reset_angle(0)
#gabelstapler.run(-80)
#while gabelstapler.angle() >= -250:
#    print(gabelstapler.angle())
greifarm.reset_angle(0)
greifarm.run(-150)
while greifarm.angle() >= -230:
    pass
greifarm.hold()

gabelstapler.reset_angle(0)
gabelstapler.run(80)
while gabelstapler.angle() <= 250:
    print(gabelstapler.angle())
gabelstapler.hold()