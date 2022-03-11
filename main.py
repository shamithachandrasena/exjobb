import steppers
import time

steppers.calibrate_X()
steppers.calibrate_Y()

while(steppers.arm):
    steppers.move_to(100, 100, steppers.SINGLE)
    time.sleep(1)
    steppers.move_to(50, 50, steppers.SINGLE)
    time.sleep(1)
    steppers.move_to(0, 0, steppers.SINGLE)
    time.sleep(1)

