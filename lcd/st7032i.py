import time
from pyb import I2C
from pyb import Pin

p_out=Pin('X12',Pin.OUT_PP) # Reset Pin

class ST7032I(object):

    def __init__(self):
        self.reset()
        self.init_lcd()
    
    def reset(self):
        p_out.low()
        time.sleep(0.1)
        p_out.high()
        time.sleep(0.1)
    
    def send_command(self, command):
        data = bytearray(2)
        data[0]=0x00
        data[1]=command
        self.i2c.send(data, addr=0x3e)

    def send_character(self, character):
        data = bytearray(2)
        data[0]=0x40
        data[1]=character
        self.i2c.send(data, addr=0x3e)

    def init_lcd(self):
        self.i2c = I2C(1, I2C.MASTER)
        self.i2c.init(I2C.MASTER, baudrate=400000) # 400kHz
        self.send_command(0x38)
        self.send_command(0x39)
        self.send_command(0x14)
        self.send_command(0x70) # Voltage 3.3v
        self.send_command(0x56) # Voltage 3.3v
        self.send_command(0x6C)
        time.sleep(0.2)
        self.send_command(0x38)
        self.send_command(0x0C)
        self.send_command(0x01)
        time.sleep(1.2)
