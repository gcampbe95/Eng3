import ansyncio
import board
import keypad
import time
import digitalio
from adafruit_motor import stepper

DELAY = 0.01
STEPS = 100

coils = (
    digitalio.DigitalInOut(board.D9), #A1
    digitalio.DigitalInOut(board.D10), #A2
    digitalio.DigitalInOut(board.D11), #B1
    digitalio.DigitalInOut(board.D12), #B2
)

for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT

motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)
