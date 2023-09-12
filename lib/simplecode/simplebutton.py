import board
import time
import pwmio
from digitalio import DigitalInOut, Direction, Pull 
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50) #sets up pwm

btn1 = DigitalInOut(board.D6) #b1 pin
btn1.direction = Direction.INPUT 
btn1.pull = Pull.DOWN #sets up pulldown for buttons

while True:
    if btn1.value: # while the button is pressed
        print ("BTN is down")
    else:
        print("BTN is up")
        pass
