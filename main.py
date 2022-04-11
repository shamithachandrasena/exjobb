import steppers
import time
import light

while(not steppers.arm):
    time.sleep(0.1)

steppers.calibrate_X()
steppers.calibrate_Y()

while(steppers.arm):
    steppers.move_to(125, 35, steppers.stepper.SINGLE)
    time.sleep(1)
    light.set_light(True)
    time.sleep(3)
    light.set_light(False)
    time.sleep(1)
    steppers.move_to(200, 50, steppers.stepper.SINGLE)
    time.sleep(1)
    light.set_light(True)
    time.sleep(3)
    light.set_light(False)
    time.sleep(1)
    steppers.move_to(285, 35, steppers.stepper.SINGLE)
    time.sleep(1)
    light.set_light(True)
    time.sleep(3)
    light.set_light(False)
    time.sleep(1)
    

