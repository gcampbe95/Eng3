import board
import time
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

photoint = digitalio.DigitalInOut(board.D6)
photoint.direction = digitalio.Direction.INPUT
photoint.pull = digitalio.Pull.UP
photoint_state = None

while True:
    
