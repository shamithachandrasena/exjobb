from typing import Counter
import steppers
import time
import light
import casat_interface
import sensor

while(not steppers.arm):
    time.sleep(0.1)

evo = sensor.initEvo()

last_item = ''
picked = False

debug = True

while(True):

    # Wait and update for new item
    while(last_item != casat_interface.get_item()):
        casat_interface.update_data()
    last_item = casat_interface.get_item()
    picked = False
    light.set_light(False)

    # Go to 0, 0
    steppers.calibrate_X()
    steppers.calibrate_Y()
    time.sleep(0.2)

    # Move to curren position and turn on light
    steppers.move_to(casat_interface.get_X(), casat_interface.get_Y(), steppers.stepper.SINGLE)
    time.sleep(0.2)
    light.set_light(True)

    # Measure the current height
    for i in range(20):
        sensor.get_height(evo) # Flush out the first measurements
    base_heigt = sensor.get_evo_range(evo)

    # DEBUG
    if debug:
        print('Base height: ' + str(base_heigt))

    # Look for variation bigger than the threshold
    height = sensor.get_evo_range(evo)
    threshold = 50 # mm
    trig_buffer = 20
    counter = 0
    while(True):
        if base_heigt - height > threshold:
            counter += 1
        elif counter > trig_buffer:
            picked = True
            break
        height = sensor.get_evo_range(evo)
    
    # DEBUG
    if debug:
        print('Triggered height: ' + str(height))
    
    if picked:
        casat_interface.write_to_file('picked', 1)

    # Flash light to indicate that the item has been picked
    light.set_light(False)
    time.sleep(0.5)
    light.set_light(True)



    

