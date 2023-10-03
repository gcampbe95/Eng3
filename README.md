# CircuitPython
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [Ultrasonic_Rainbow](#Ultrasonic_Rainbow)
* [Motor_Control](#Motor_Control)
---

## Hello_CircuitPython

### Description & Code Snippets
Write a couple sentences here, describing this assignment, and make sure that you hit these two points:
* What was the goal of the assignment?
* How did you accomplish that goal?
  How you accomplished the goal is NOT a reflection, it is you telling the reader how to do this assignment, in broad strokes.

  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
Code goes here

```

**Lastly, please end this section with a link to your code or file.**  

### Evidence
Pictures / Gifs of your finished work should go here.  You need to communicate what your thing does.
For making a GIF, I recommend [ezgif.com](https://www.ezgif.com) Remember you can insert pictures using Markdown or HTML to insert an image.

![spinningMetro_Optimized](https://user-images.githubusercontent.com/54641488/192549584-18285130-2e3b-4631-8005-0792c2942f73.gif)


And here is how you should give image credit to someone if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
Make an account with your Google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**

## Ultrasonic_Rainbow

### Description & Code Snippets
This assignment was to use what we recently learned about neopixels to fade one's color from red to blue to green as an object got farther away from an ultrasonic sensor. This required a lot of familiar skills like mapping to be adapted for circuitpython. My strategy was to break distances that required fades into chunks of red-magenta, magenta-blue, blue-cyan, and cyan-green, which meant I only had to tackle one rgb value at a time. For this task, the best solution turned out to be the simplest one, and though I'm not usually one for writing pseudocode, I would definitely recommend it to anyone attempting this assignment. 

The code for one of the afformentioned color sections looks like this:

``` 
if (5 < sonar.distance) and (sonar.distance <= 12.5): #names distance range
      r = 255 #setting initial rgb values
      g = 0
      # b = 0 // I commented this out because the b value is what will be changing, but it's good to have as a reminder
      b = map_unconstrained_range(sonar.distance, 5, 12.5, 0, 255) # b icreases with distance
      color = (r, g, b)
      pixels.fill((color))
      pixels.show()
```
Before beginning, it was important that I understood all the components, so I broke the task down into shorter, simpler code functions that only did one thing. This is an example of my ultrasonic sensor "simplecode:"

``` 
import board
    import time
    import adafruit_hcsr04
    sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
```
Once I had all these pieces, I combined them into my full code which can be found here:
**https://github.com/gcampbe95/Eng3/blob/main/ultrasonic_rainbow.py**  

### Evidence

![](https://im5.ezgif.com/tmp/ezgif-5-0dd6a09949.gif)

### Wiring
Wiring for this code can be found here: 

**https://www.tinkercad.com/things/8jPgL02bwfb?sharecode=Yq47arHhx7T9tyG5EsO7KpIhFaA4cjIe9BHEPfdqQR8**

![](../../Pictures/WIN_20230925_11_13_32_Pro%20-%20Trim.mp4)

### Reflection
The easiest way to approach this was to break it into more manageable parts, such as checking the function of my ultrasonic sensor, writing simpler pieces of neopixel code to make sure I understood it before moving on to more advanced functions like gradients, and mapping simple ranges and printing the result. I spent a lot of time on this because I was trying to come up with a solution using variables and adding/subtracting from rgb values incrementally instead of mapping. The solution that ended up working was naming colors and distances at the top to keep my values organized, like this...
```
red = (255, 0, 0) # 5
magenta = (255, 0, 255) # 12.5
blue = (0, 0, 255) # 20
cyan = (0, 255, 255) # 27.5
green = (0, 255, 0) # 35
```
... and then naming these as initial rgb values for each range individually. After that I mapped the changing value to distance to get a smooth color transition. That's it! It took a lot of time for me to realize that the best solution was actually the least complicated, but I could've probably avoided that if I had organized my tasks better and written some pseudocode beforehand. 

## Motor_Control

### Description & Code Snippets
This assignment was to control the speed of a motor using input from a potentiometer. It was a fairly simple piece of code (the whileTrue is only 2 lines) and the trickiest parts were was making sure my wiring was correct and realizing that all I needed was pwmio, and not a brand new library. 

I started with printing the potentiometer value like this:

``` 
import board
import time
from analogio import AnalogIn

potentiometer = AnalogIn(board.A0)

while True:
    print((potentiometer.value))
    time.sleep(0.25)
```
Once that was working, I added 2 lines to incorporate motor control and the finished code looked like this:

``` 
import board
import time
from analogio import AnalogIn
import pwmio

potentiometer = AnalogIn(board.A0)
pwm = pwmio.PWMOut(board.D6)

while True:
    print((potentiometer.value))
    pwm.duty_cycle = potentiometer.value
```

### Evidence

![](https://im5.ezgif.com/tmp/ezgif-5-0dd6a09949.gif)

### Wiring
Wiring for this code can be found here (procede with caution): 

**https://www.tinkercad.com/things/9N2J4e0QSd0-stunning-gaaris/editel?tenant=circuits**

![](../../Pictures/WIN_20230925_11_13_32_Pro%20-%20Trim.mp4)

### Reflection
The easiest way to approach this was to break it into more manageable parts, such as checking the function of my ultrasonic sensor, writing simpler pieces of neopixel code to make sure I understood it before moving on to more advanced functions like gradients, and mapping simple ranges and printing the result. I spent a lot of time on this because I was trying to come up with a solution using variables and adding/subtracting from rgb values incrementally instead of mapping. The solution that ended up working was naming colors and distances at the top to keep my values organized, like this...
```
red = (255, 0, 0) # 5
magenta = (255, 0, 255) # 12.5
blue = (0, 0, 255) # 20
cyan = (0, 255, 255) # 27.5
green = (0, 255, 0) # 35
```
... and then naming these as initial rgb values for each range individually. After that I mapped the changing value to distance to get a smooth color transition. That's it! It took a lot of time for me to realize that the best solution was actually the least complicated, but I could've probably avoided that if I had organized my tasks better and written some pseudocode beforehand. 
