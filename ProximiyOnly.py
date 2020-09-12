import time, socket, pickle
from gpiozero import MCP3008
import sys


divider = MCP3008(0)


while True:
    print(divider.value)       
    time.sleep(1)


