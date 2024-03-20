#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import math


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
lm = Motor(Port.D)
rm = Motor(Port.A)
robot = DriveBase(lm,rm, 55, 141)
gabelstapler = Motor(Port.B)
greifarm = Motor(Port.C)
gyro = GyroSensor(Port.S2)

# Write your program here.
#gabelstapler.reset_angle(0)
#gabelstapler.run(-80)
#while gabelstapler.angle() >= -250:
#    print(gabelstapler.angle())

def greifarm_f(grad):
    greifarm.reset_angle(0)
    greifarm.run((grad/abs(grad))*150)
    while abs(greifarm.angle()) <= abs(grad):
        pass
    greifarm.hold()

def gabelstapler_f(grad):
    gabelstapler.reset_angle(0)
    gabelstapler.run(80)
    while gabelstapler.angle() <= grad:
        print(gabelstapler.angle())
    gabelstapler.hold()


def perfekte_kurve_rechts(grad):
    gyro.reset_angle(0)
    while gyro.angle() <= grad:
        x = gyro.angle()
        y = -20 * math.log(grad+x) + 2
        robot.drive(0, y)
        print(gyro.angle())
     
    robot.stop()
    lm.stop()
    rm.stop()

def perfekte_kurve_links(grad):
    gyro.reset_angle(0)
    while gyro.angle() >= -grad:
        x = gyro.angle()
        y = 20 * math.log(grad-x) + 2
        robot.drive(0, y)
        print(y)
     
    robot.stop()
    lm.stop()
    rm.stop()



perfekte_kurve_links(55)
greifarm_f(-90)


robot.straight(350)
perfekte_kurve_rechts(110)

robot.straight(280)
greifarm_f(100)

robot.straight(100)
perfekte_kurve_rechts(30)

robot.straight(900)

perfekte_kurve_links(45)

robot.straight(600)
