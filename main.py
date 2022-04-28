from typing import Counter
import steppers
import time
import light
import casat_interface
import sensor


evo = sensor.initEvo()
casat_interface.update_data()

last_item = ''
picked = False

debug = True

while(not steppers.arm):
    time.sleep(0.1)

while(True):

    if debug:
        print(casat_interface.get_item())

    # Go to 0, 0
    steppers.calibrate_X()
    steppers.calibrate_Y()
    time.sleep(0.2)

    picked = False
    light.set_light(False)


    # Move to curren position and turn on light
    steppers.move_to(casat_interface.get_x_axis(), casat_interface.get_y_axis(), steppers.stepper.SINGLE)
    time.sleep(0.2)
    light.set_light(True)

    # Measure the current height
    for i in range(20):
        sensor.get_evo_range(evo) # Flush out the first measurements
    base_heigt = sensor.get_evo_range(evo)

    # DEBUG
    if debug:
        print('Base height: ' + str(base_heigt))

    # Look for variation bigger than the threshold
    height = sensor.get_evo_range(evo)
    threshold = 50 # mm
    trig_buffer = 100
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
    time.sleep(1)
    light.set_light(True)


    # Wait and update for new item
    while(last_item != casat_interface.get_item()):
        casat_interface.update_data()
    last_item = casat_interface.get_item()
    

    

