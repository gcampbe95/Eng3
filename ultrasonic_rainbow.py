# test

import board
import time
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
from rainbowio import colorwheel
import neopixel 
r = 255
g = 0
b = 0

color = (r, g, b)
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
            b = (b + 1) % 256
            pixels.fill(colorwheel(color))
            pixels.show()
        if (12.5 < sonar.distance) and (sonar.distance <= 20):
            r = (r - 1) % 256
            pixels.fill(colorwheel(color))
            pixels.show()
        if (20 < sonar.distance) and (sonar.distance <= 27.5):
            g = (g + 1) % 256
            pixels.fill(colorwheel(color))
            pixels.show()
        if (27.5 < sonar.distance) and (sonar.distance < 35):
            b = (b - 1) % 256
            pixels.fill(colorwheel(color))
            pixels.show()
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
