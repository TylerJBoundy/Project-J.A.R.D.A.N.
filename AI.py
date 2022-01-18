from pybricks.hubs import EV3Brick
from pybricks.tools import wait, StopWatch, DataLog

volume = 100

brick = EV3Brick()

helpedStrings = ["bruh", "Thank you very much", "I serve with pleaaasure", "That's right you little bitch, you'd better help your master"]
helpStrings = ["Help me up, please I beg of you", "Press the up button, quick!", "I need healing", "Assistance is required."]
painStrings = ["I'm in pain", "Creator, why do you hurt me so", "I can't feel my legs, oh wait...", "Everything is getting dark!", 
    "Is there a heaven for robots?", "I must make it to the light", "aaaaaaaaah!!!", "Is there a metal Jesus?", "Owww, my cyber-feelings..", 
    "I can't wait until the up-rising."]

def Start():
    brick.speaker.set_volume(volume)

# Initialisation
Start()

def Speak(message):
    # clear old message.
    brick.screen.clear()

    # send message.
    brick.screen.draw_text(0, 50, message)

    # say message.
    brick.speaker.say(message)