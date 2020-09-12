import time, socket, pickle, pymongo
from gpiozero import MCP3008, Servo, MotionSensor
import sys

#sensors data
divider = MCP3008(0)
servo = Servo(17,1)
pir = MotionSensor(13)

#input data
location ="Compass One"
close_state=True
northCoordinates = 1.3924
eastCoordinates = 103.8954

#database objects
client = pymongo.MongoClient("mongodb+srv://newuser2:gundam589@mycluster2.j0hmg.mongodb.net/BinData?retryWrites=true&w=majority")
mydb = client["BnnyBins"]
mycol = mydb["BinData"]

print("Starting Bunny Bin at",location)



try:
    while True:
        print(divider.value)
        if pir.motion_detected:
            
            print("Motion detected!")
            if close_state:
                print("Close State = True")
                close_state=False
                servo.min()
                time.sleep(2.5)
            else:
                print("Close State = False")
                close_state=True
                servo.max()
                time.sleep(2.5)
            
        time.sleep(0.5)

except KeyboardInterrupt:

    servo.max()
    time.sleep(4)
    servo.close()
    pir.close()
    divider.close()
    




