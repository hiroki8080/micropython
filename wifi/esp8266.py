import time
from pyb import UART

class ESP8266(object):

    def __init__(self):
        self.uart = UART(6, 115200)
    
    def write(self, command):
        self.uart.write(command)
        count = 5
        while count >= 0:
            if self.uart.any():
                print(self.uart.readall().decode('utf-8'))
            time.sleep(0.1)
            count-=1
