# test

import board
import time
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
from rainbowio import colorwheel
import neopixel 

num_pixels = 1  # Update this to match the number of LEDs.
BRIGHTNESS = 0.2  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.

pixels = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=BRIGHTNESS, auto_write=False)

while True:
    try:
        print((sonar.distance,))
        if sonar.distance <= 5:
            pixels.fill((255, 0, 0))
            pixels.show()
        if sonar.distance >= 35:
            pixels.fill((0, 255, 0))
            pixels.show()
        if sonar.distance == 20:
            pixels.fill((0, 0, 255))
            pixels.show()
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
