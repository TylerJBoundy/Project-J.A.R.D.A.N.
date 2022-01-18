# armControl.py>

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color

brick = EV3Brick()

lifter = Motor(Port.A)

readyToLift = True

liftSpeed = 1000
liftAngle = 15



def Lift():
    global readyToLift
    if readyToLift is True:
        readyToLift = False
        brick.screen.draw_text(0, 20, "Lifting")
        lifter.run_angle(liftSpeed, -liftAngle, Stop.HOLD, False)

def Unlift():
    global readyToLift
    if readyToLift is False:
        readyToLift = True
        brick.screen.draw_text(0, 40, "Un-lifting")
        lifter.run_angle(liftSpeed * 2, liftAngle, Stop.HOLD, False)