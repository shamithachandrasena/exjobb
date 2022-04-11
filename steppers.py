import board
import signal
import sys
import time
import RPi.GPIO as IO
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())

arm_input = 24
arm_light = 25

arm = False

rotaryA_X = 17
rotaryB_X = 18

rotaryA_Y = 27
rotaryB_Y = 22

val_X = 0
val_Y = 0

coord_X = 0
coord_Y = 0

endstop_X = 20
endstop_Y = 21

speed = 0.02

def signal_handler(sig, frame): 
    kit.stepper1.release()
    kit.stepper2.release()
    IO.cleanup()
    sys.exit(0)

# Rotary encoder callback function for X axis
def rotary_callback_X(channel): 
    global val_X
    val_X = val_X + 1

# Rotary encoder callback function for Y axis
def rotary_callback_Y(channel): 
    global val_Y
    val_Y = val_Y + 1

# Arm callback function
def arm_callback(channel): 
    global arm
    arm = not arm
    if arm:
        IO.output(arm_light, IO.HIGH)
    else:
        IO.output(arm_light, IO.LOW)

#if __name__ == '__main__':
IO.setmode(IO.BCM)

IO.setup(arm_input, IO.IN, pull_up_down=IO.PUD_UP)
IO.setup(arm_light, IO.OUT)
IO.add_event_detect(arm_input, IO.FALLING, callback=arm_callback, bouncetime=600)

IO.setup(rotaryA_X, IO.IN, pull_up_down=IO.PUD_DOWN)
IO.setup(rotaryB_X, IO.IN, pull_up_down=IO.PUD_DOWN)

IO.add_event_detect(rotaryA_X, IO.BOTH, callback=rotary_callback_X, bouncetime=1)
IO.add_event_detect(rotaryB_X, IO.BOTH, callback=rotary_callback_X, bouncetime=1)

IO.setup(rotaryA_Y, IO.IN, pull_up_down=IO.PUD_DOWN)
IO.setup(rotaryB_Y, IO.IN, pull_up_down=IO.PUD_DOWN)

IO.add_event_detect(rotaryA_Y, IO.BOTH, callback=rotary_callback_Y, bouncetime=1)
IO.add_event_detect(rotaryB_Y, IO.BOTH, callback=rotary_callback_Y, bouncetime=1)

IO.setup(endstop_X, IO.IN, pull_up_down=IO.PUD_UP)
IO.setup(endstop_Y, IO.IN, pull_up_down=IO.PUD_UP)

signal.signal(signal.SIGINT, signal_handler)
IO.output(arm_light, IO.LOW)

# function to move stepper motor for X axis
def move_X(direction, style):
    global arm
    global coord_X
    if arm and coord_X < 800:
        kit.stepper2.onestep(direction=direction, style=style)
        time.sleep(speed)

# function to move stepper motor for Y axis
def move_Y(direction, style):
    global arm
    global coord_Y
    if arm and coord_Y < 400:
        kit.stepper1.onestep(direction=direction, style=style)
        time.sleep(speed)

# function to calibrate X axis stepper motor
def calibrate_X():
    global val_X
    global coord_X
    while IO.input(endstop_X) == IO.HIGH:
        move_X(stepper.FORWARD, stepper.SINGLE)
    val_X = 0
    coord_X = 0

# function to calibrate Y axis stepper motor
def calibrate_Y():
    global val_Y
    global coord_Y
    while IO.input(endstop_Y) == IO.HIGH:
        move_Y(stepper.BACKWARD, stepper.SINGLE)
    val_Y = 0
    coord_Y = 0

# function to move stepper motor for X axis to a specific coordinate x
def move_to_X(x, style):
    global val_X
    global coord_X

    val_X = 0

    length = abs(x - coord_X)

    if x > coord_X:
        while val_X < length:
            move_X(stepper.FORWARD, style)
            print(val_X)
    elif x < coord_X:
        while val_X < length:
            move_X(stepper.BACKWARD, style)
            print(val_X)
    
    coord_X = x

# function to move stepper motor for Y axis to a specific coordinate y
def move_to_Y(y, style):
    global val_Y
    global coord_Y

    val_Y = 0

    length = abs(y - coord_Y)

    if y > coord_Y:
        while val_Y < length:
            move_Y(stepper.FORWARD, style)
            print(val_Y)
    elif y < coord_Y:
        while val_Y < length:
            move_Y(stepper.BACKWARD, style)
            print(val_Y)
    
    coord_Y = y

# function to move to a specific coordinate (x, y)
def move_to(x, y, style):
    move_to_X(x, style)
    move_to_Y(y, style)


