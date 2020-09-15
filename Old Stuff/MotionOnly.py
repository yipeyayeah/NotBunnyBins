from gpiozero import MotionSensor
pir = MotionSensor(13)
import time

while True:
    if pir.motion_detected:
        print("Movement")
        time.sleep(0.5)        
##    pir.wait_for_motion()
##    print("Motion detected!")
##    pir.wait_for_no_motion()
##    print("No Motion detected!")
