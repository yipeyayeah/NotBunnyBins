import time, socket, pickle
from gpiozero import MCP3008, Servo, MotionSensor
import sys


divider = MCP3008(0)
servo = Servo(17,1)
pir = MotionSensor(13)


close_state=True
print("done")

try:
    while True:
        print(divider.value)
        if pir.motion_detected:
            
            print("Motion detected!")
            if close_state:
                print("Close State = True")
                close_state=False
                servo.min()
                time.sleep(4.5)
            else:
                print("Close State = False")
                close_state=True
                servo.max()
                time.sleep(4.5)
            
        time.sleep(0.5)

except KeyboardInterrupt:

    servo.max()
    time.sleep(4)
    servo.close()
    pir.close()
    divider.close()
    



