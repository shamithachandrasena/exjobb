import steppers
import time
import light

steppers.calibrate_X()
steppers.calibrate_Y()

while(steppers.arm):
    steppers.move_to(100, 100, steppers.stepper.SINGLE)
    time.sleep(1)
    light.set_light(True)
    time.sleep(10)
    light.set_light(False)
    time.sleep(1)
    steppers.move_to(50, 50, steppers.stepper.SINGLE)
    time.sleep(1)
    light.set_light(True)
    time.sleep(10)
    light.set_light(False)
    time.sleep(1)
    steppers.move_to(0, 0, steppers.stepper.SINGLE)
    time.sleep(1)
    light.set_light(True)
    time.sleep(10)
    light.set_light(False)
    time.sleep(1)
    

