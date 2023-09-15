import board
import time
import pwmio
from adafruit_motor import servo 
from digitalio import DigitalInOut, Direction, Pull 
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50) #sets up pwm
my_servo = servo.Servo(pwm)
curangle = 90 #the while True asks the servo to move right or left of this angle

btn1 = DigitalInOut(board.D6) #b1 pin
btn1.direction = Direction.INPUT 
btn1.pull = Pull.DOWN #sets up pulldown for buttons

btn2 = DigitalInOut(board.D5) #same as b1
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN

while True:
    if btn1.value: # while the button is pressed
        if curangle <= 174: # prevents the angle from getting above 180 
            curangle = curangle + 5 
            my_servo.angle = curangle
            time.sleep(0.05)
    elif btn2.value:
        if curangle >= 6: # prevents the angle from getting below 0 
            curangle = curangle - 5
            my_servo.angle = curangle
            time.sleep(0.05)
    else:
        print("BTN is up")
        pass
