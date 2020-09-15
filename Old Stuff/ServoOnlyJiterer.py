from gpiozero import Servo
from time import sleep

myGPIO=17
servo = Servo(myGPIO)

while True:
    servo.value = -1
    sleep(3)
    servo.value = 1
    sleep(3)
##    servo.min()
##    sleep(3)
##    servo.max()
##    sleep(3)