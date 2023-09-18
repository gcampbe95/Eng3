import board
import time
from rainbowio import colorwheel
import neopixel 

num_pixels = 1  # Update this to match the number of LEDs.
BRIGHTNESS = 0.2  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.

pixels = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=BRIGHTNESS, auto_write=False)

while True:
     pixels.fill((255, 0, 0))
     pixels.show()
     time.sleep(0.5)
     pixels.fill((0, 255, 0))
     pixels.show()
     time.sleep(0.5)
     pixels.fill((0, 0, 255))
     pixels.show()
     time.sleep(0.5)
     