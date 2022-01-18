# headControl.py>

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from AI import Speak, helpedStrings
import random

painCount = 0

motorSpeed = 20000000
motorAngle = 165

isDown = False

brick = EV3Brick()

# define ports
head = Motor(Port.A)
beak = TouchSensor(Port.S4)

def Start():
    head.hold()

# Initialisation
Start()

# Head Behaviour
def SlamHead():
    global isDown
    if isDown is False:
        Speak("I'm a bird")
        head.run_angle(motorSpeed, motorAngle, Stop.HOLD, False)
        isDown = True
def HelpMe():
    global isDown
    if isDown is False:
        Speak('Press the left button!')
    else:
        Speak('Press the up button!')
def RaiseHead():
    global isDown
    if isDown:
        Speak(helpedStrings[random.randint(0, len(helpedStrings) - 1)])
        head.run_angle(motorSpeed * 2, -motorAngle, Stop.HOLD, True)
        head.hold()
        isDown = False