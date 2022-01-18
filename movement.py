# movement.py>

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color

distanceConstant = 24
rotationConstant = 4.35

movementSpeed = 1000
rotationSpeed = 1000

# wheels
leftWheel = Motor(Port.D)
rightWheel = Motor(Port.B)

# Movement Behaviour
def GoForward(distance):
    leftWheel.run_angle(movementSpeed, -(distance * distanceConstant), Stop.HOLD, False)
    rightWheel.run_angle(movementSpeed, -(distance * distanceConstant), Stop.HOLD, False)
def GoBackward(distance):
    leftWheel.run_angle(movementSpeed, distance * 24, Stop.HOLD, False)
    rightWheel.run_angle(movementSpeed, distance * 24, Stop.HOLD, False)
def TurnRight(angle):
    leftWheel.run_angle(rotationSpeed, -(angle * rotationConstant), Stop.HOLD, False)
    rightWheel.run_angle(rotationSpeed, angle * rotationConstant, Stop.HOLD, False)
def TurnLeft(angle):
    leftWheel.run_angle(rotationSpeed, angle * rotationConstant, Stop.HOLD, False)
    rightWheel.run_angle(rotationSpeed, -(angle * rotationConstant), Stop.HOLD, False)