#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


class WRO:
    def __init__():     #setzt alle Sensoren und Aktoren auf
        ev3 = EV3Brick()
        lm = Motor(Port.A)
        rm = Motor(Port.D)
        robot = DriveBase(lm,rm, 55, 141)
        gabelstapler = Motor(Port.B)
        greifarm = Motor(Port.C)
        pass

    def zugreifen():    #schließt die Kralle
        greifarm.reset_angle(0)
        greifarm.run(-150)
        while greifarm.angle() >= -230:
            pass
        greifarm.hold()
        

    def aufmachen():    #oeffnet die Kralle
        greifarm.reset_angle(0) 
        greifarm.run(150)
        while greifarm.angle() <= -230:
            pass
        greifarm.hold()
        

    def hochfahren():   #fährt Gabelstapler hoch
        
        gabelstapler.reset_angle(0)
        abelstapler.run(-80)
        while gabelstapler.angle() >= -250:
            pass
        gabelstapler.hold()

    def runterfahren(): #fährt Gabelstapler runter
    
        gabelstapler.reset_angle(0)
        gabelstapler.run(80)
        while gabelstapler.angle() <= 250:
            pass
        gabelstapler.hold()

    def Position():     #gibt Position #und Rotation des Roboters #zurück(berechnet durch die bisherigen #Fahrten)
        

        return (x,y,r)

    def fahre_zu(currentx,currenty, currentr,x,y,r):     #fährt zu den angegebenen Koordinaten und rotation
        	
        pass