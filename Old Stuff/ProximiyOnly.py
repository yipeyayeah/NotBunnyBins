import time, socket, pickle
from gpiozero import MCP3008
import sys


divider = MCP3008(0)


while True:
    print(divider[0].value)       
    time.sleep(1)


