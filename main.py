#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random
import time

from movement import TurnRight, TurnLeft, GoForward, GoBackward
from headControl import SlamHead, RaiseHead, HelpMe, painCount, beak, isDown
from armControl import Lift, Unlift, readyToLift
from AI import Speak, helpStrings, helpedStrings, painStrings


# 0 - movement
# 1 - head
# 2 - arm
mode = 0

brick = EV3Brick()



# Button Behaviour
def LeftButton():
    global mode
    if mode == 0:
        TurnRight(45)
    elif mode == 1:
        SlamHead()
    elif mode == 2:
        Lift()
def RightButton():
    global mode
    if mode == 0:
        TurnLeft(45)
    elif mode == 1:
        HelpMe()
    elif mode == 2:
        Unlift()
def UpButton():
    global mode
    if mode == 0:
        GoBackward(10)
    elif mode == 1:
        RaiseHead()
    elif mode == 2:
        brick.screen.clear()
        mode = 0
def DownButton():
    global mode
    if mode == 0:
        GoForward(10)
    elif mode == 1:
        brick.screen.clear()
        mode = 2



while True:
    if mode == 0:
        brick.screen.draw_text(0, 0, "Mode: Movement")
    elif mode == 1:
        brick.screen.draw_text(0, 0, "Mode: Head controls")
    elif mode == 2:
        brick.screen.draw_text(0, 0, "Mode: Arm controls")

    #define buttons
    buttons = brick.buttons.pressed()

    # check button press
    if Button.LEFT in buttons:
        LeftButton()
    elif Button.RIGHT in buttons:
        RightButton()
    elif Button.UP in buttons:
        UpButton()
    elif Button.DOWN in buttons:
        DownButton()

    if beak.pressed():
        if mode == 0:
            brick.screen.clear()
            mode = 1
        elif mode == 1:
            painCount += 1

            # clear old message.
            brick.screen.clear()

            # send message.
            brick.screen.draw_text(0, 50, 'pain counter = ' + str(painCount))

            # say message.
            brick.speaker.say(painStrings[random.randint(0, len(painStrings) - 1)])
    elif isDown:
        if mode == 1:
            Speak(helpStrings[random.randint(0, len(helpStrings) - 1)])