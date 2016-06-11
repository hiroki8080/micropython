import pyb
import time
from st7032i import ST7032I

lcd = ST7032I()
lcd.send_command(0x80 | 0x00) # set cursor (0, 0)
lcd.send_character(0xCA) # write character
lcd.send_character(0xB0) # write character
lcd.send_character(0xB2) # write character
