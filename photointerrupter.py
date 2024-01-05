import board
import time
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
counter = 0
lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x27), num_rows=2, num_cols=16)

photoint = digitalio.DigitalInOut(board.D6)
photoint.direction = digitalio.Direction.INPUT
photoint.pull = digitalio.Pull.UP
photoint_state = None

lcd.set_cursor_pos(0,0)
lcd.print("interrupts:")

while True:
    lcd.set_cursor_pos(0,0)
    lcd.print("interrupts:  ")
    if not photoint.value and photoint_state is None:
        photoint_state = None 
        lcd.set_cursor_pos(1,0)
        lcd.print("                 ")
    if photoint.value and photoint_state is None:
        photoint_state = "interrupted"  
        photoint_state = None
        counter = counter + 1
        print(counter)
        lcd.set_cursor_pos(1,0)
        lcd.print(counter)
    

