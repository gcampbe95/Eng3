# test

import board
import time
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
from rainbowio import colorwheel
import neopixel
from adafruit_simplemath import map_range
from adafruit_simplemath import map_unconstrained_range # I opted for unconstrained for this because I'm sometimes mapping color values backwards

r = 0 # these will change with distance
g = 0
b = 0 

red = (255, 0, 0) # 5
magenta = (255, 0, 255) # 12.5
blue = (0, 0, 255) # 20
cyan = (0, 255, 255) # 27.5
green = (0, 255, 0) # 35

num_pixels = 1  # only 1 because I'm using my neopixel
BRIGHTNESS = 0.4  # between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.

pixels = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=BRIGHTNESS, auto_write=False)

while True:
    try:
        print((sonar.distance,))
        if sonar.distance <= 5: #--------------------------------------------------------------------------------------------------------
            pixels.fill(red) # set color to red for values less than or equal to 5 
            pixels.show() # display color
        if sonar.distance >= 35: #-------------------------------------------------------------------------------------------------------
            pixels.fill(green)
            pixels.show()
        if (5 < sonar.distance) and (sonar.distance <= 12.5): #--------------------------------------------------------------------------
            # color = (red)
            r = 255 #setting initial rgb values
            g = 0
            # b = 0
            b = map_unconstrained_range(sonar.distance, 5, 12.5, 0, 255) # b icreases with distance
            color = (r, g, b)
            pixels.fill((color))
            pixels.show()
        if (12.5 < sonar.distance) and (sonar.distance <= 20): #-------------------------------------------------------------------------
            # color = (magenta)
            # r = 255
            g = 0
            b = 255
            r = map_unconstrained_range(sonar.distance, 12.5, 20, 255, 0)
            color = (r, g, b)
            pixels.fill((color))
            pixels.show()
        if (20 < sonar.distance) and (sonar.distance <= 27.5): #-------------------------------------------------------------------------
            # color = (blue)
            r = 0
            # g = 0
            b = 255
            g = map_unconstrained_range(sonar.distance, 20, 27.5, 0, 255)
            color = (r, g, b)
            pixels.fill((color))
            pixels.show()
        if (27.5 < sonar.distance) and (sonar.distance < 35): #--------------------------------------------------------------------------
            # color = (cyan)
            r = 0
            g = 255
            # b = 255
            b = map_unconstrained_range(sonar.distance, 27.5, 35, 255, 0)
            color = (r, g, b)
            pixels.fill((color))
            pixels.show()
    except RuntimeError: #---------------------------------------------------------------------------------------------------------------
        print("Retrying!")
    time.sleep(0.1)
