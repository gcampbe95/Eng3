# test

import board
import time
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
from rainbowio import colorwheel
import neopixel
from adafruit_simplemath import map_range
from adafruit_simplemath import map_unconstrained_range

r = 255
g = 0
b = 0

red = (255, 0, 0) # 5
magenta = (255, 0, 255) # 12.5
blue = (0, 0, 255) # 20
cyan = (0, 255, 255) # 27.5
green = (0, 255, 0) # 35

num_pixels = 1  # Update this to match the number of LEDs.
BRIGHTNESS = 0.4  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.

pixels = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=BRIGHTNESS, auto_write=False)

while True:
    try:
        print((sonar.distance,))
        if sonar.distance <= 5:
            pixels.fill(red)
            pixels.show()
        if sonar.distance >= 35:
            pixels.fill(green)
            pixels.show()
        if (5 < sonar.distance) and (sonar.distance <= 12.5):
            map_unconstrained_range(b, 0, 255, sonar.distance, 5, 12.5)
            color = (r, g, b)
            pixels.fill((color))
            pixels.show()
        if (12.5 < sonar.distance) and (sonar.distance <= 20):
            map_unconstrained_range(r, 255, 0, sonar.distance, 12.5, 20)
            color = (r, g, b)
            pixels.fill((color))
            pixels.show()
        if (20 < sonar.distance) and (sonar.distance <= 27.5):
            map_unconstrained_range(g, 0, 255, sonar.distance, 20, 27.5)
            color = (r, g, b)
            pixels.fill((color))
            pixels.show()
        if (27.5 < sonar.distance) and (sonar.distance < 35):
            map_unconstrained_range(b, 255, 0, sonar.distance, 27.7, 35)
            color = (r, g, b)
            pixels.fill((color))
            pixels.show()
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
