import steppers
import time
import light
import casat_interface
import sensor

while(not steppers.arm):
    time.sleep(0.1)

steppers.calibrate_X()
steppers.calibrate_Y()
evo = sensor.initEvo()

last_item = ''

while(True):
    # # Get the current item
    # while(last_item != casat_interface.get_item()):
    #     casat_interface.update_data()
    # last_item = casat_interface.get_item()

    # # Move to curren position
    # steppers.move_to(casat_interface.get_X(), casat_interface.get_Y(), steppers.stepper.SINGLE)
    # time.sleep(1)
    # light.set_light(True)
    # base_heigt = sensor.get_evo_range(evo)



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
    

