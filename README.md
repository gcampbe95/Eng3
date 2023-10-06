# ENG3_Documentation

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Ultrasonic_Rainbow](#Ultrasonic_Rainbow)
* [Motor_Control](#Motor_Control)
* [Onshape_Hanger](#Onshape_Hanger)
* [Swing_Arm](#Swing_Arm)
---

## Ultrasonic_Rainbow

### Description & Code Snippets
This assignment was to use what we recently learned about neopixels to fade one's color from red to blue to green as an object got farther away from an ultrasonic sensor. This required a lot of familiar skills like mapping to be adapted for circuitpython. My strategy was to break distances that required fades into chunks of red-magenta, magenta-blue, blue-cyan, and cyan-green, which meant I only had to tackle one rgb value at a time. For this task, the best solution turned out to be the simplest one, and though I'm not usually one for writing pseudocode, I would definitely recommend it to anyone attempting this assignment. 

The code for one of the afformentioned color sections looks like this:

```Python 
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

```Python 
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

**[Ultrasonic_Rainbow](https://github.com/gcampbe95/Eng3/blob/main/ultrasonic_rainbow.py)**

### Evidence

![](https://github.com/gcampbe95/Eng3/blob/main/ultrasonic.gif)

### Wiring
Wiring for this code can be found here: 

**[Ultrasonic Sensor Wiring](https://www.tinkercad.com/things/8jPgL02bwfb?sharecode=Yq47arHhx7T9tyG5EsO7KpIhFaA4cjIe9BHEPfdqQR8)**
![](https://github.com/gcampbe95/Eng3/blob/main/ultrasonic.png)

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
This assignment was to control the speed of a motor using input from a potentiometer. It was a fairly simple piece of code (the whileTrue is only 2 lines) and the trickiest parts were making sure my wiring was correct and realizing that all I needed was pwmio, and not a brand new library. 

I started with printing the potentiometer value like this:

```Python
import board
import time
from analogio import AnalogIn

potentiometer = AnalogIn(board.A0)

while True:
    print((potentiometer.value))
    time.sleep(0.25)
```
Once that was working, I added 2 lines to incorporate motor control and the finished code looked like this:

```Python
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

![](https://github.com/gcampbe95/Eng3/blob/main/motor.gif)

### Wiring
Wiring for this code can be found here (proceed with caution): 
**[Motor Control Wiring](https://www.tinkercad.com/things/9N2J4e0QSd0-stunning-gaaris/editel?tenant=circuits)**

![](https://github.com/gcampbe95/Eng3/blob/main/motorcontrol.png)

### Reflection
The most important parts of this assignment were wiring carefully and not overcomplicating it. In my initial iteration of this code, I included a map function that ended up being unnecessary. The more concise and effective solution was a simple "pwm.duty_cycle = potentiometer.value." As a general principle, it's better to start with the easiest plausible solution and complicate as needed, an idea that I will try to stick to more as we continue with circuitpython. 

## Onshape_Hanger 

### Description 
In this assignment we modelled a "block hanger" and got more practice modelling parts just from drawings, which will be a necessary skill for the Onshape certification. It was also a needed reminder of best practices for efficient modelling, because speed and accuracy will also be assets on the exam. Ultimately I think the most important thing to remember on this assignment is that taking the time to form good modelling habits now will definitely pay off later: a good foundation can be sped up, but practices that lead to inaccuracies will be much harder to fix. 

### Evidence

![](https://im5.ezgif.com/tmp/ezgif-5-0dd6a09949.gif)

### Part Link
The finished part can be found here: 

**https://cvilleschools.onshape.com/documents/f4db0690df87f7004a8dc5cf/w/95766ec79d0166b3b0bb6b30/e/cfd029d9d43e634cbc7a784f**

### Reflection
I approached this part by extruding a rectangular prism of the correct dimensions, then carving out the necessary arcs and holes. While this assignment didn't give me much trouble, I definitely learned some strategies for modelling **faster**. For example, this part is symetrical about the center line. I prefer to model parts all at once (accomplishing as much as possible with one sketch) so I used that approach modelling the hanger as well. I did mirror most of the symetrical features, but it would've been quicker and easier to just model one half and mirror that at the end. I also used a 3 point arc and then constrained it to be tangent instead of just using a ...tangent... arc. 

## Swing_Arm 

### Description 
In this assignment we modelled a part based on 3 drawings, using variables for some dimensions. This is definitely the most difficult CAD part I've been assigned, and it was a fun challenge to practice with. As I mentioned in the henger documentation, my sketches are busy and few, so I started by extruding this:
![](https://github.com/gcampbe95/Eng3/blob/main/swingarmsketch.png)
...then adding the holes on the ends and cutting out/expanding components to the right width and changing some of my variables to make sure the model was adaptable in the right ways. 
![](https://github.com/gcampbe95/Eng3/blob/main/swingarmholes.png)
![](https://github.com/gcampbe95/Eng3/blob/main/swingarmconfig2.png)
### Evidence

![](https://github.com/gcampbe95/Eng3/blob/main/swingarmv1.png)
![](https://github.com/gcampbe95/Eng3/blob/main/swingarmv2.png)

### Part Link
The finished part can be found here: 

**https://cvilleschools.onshape.com/documents/e16d436a118fe77fed8a7da4/w/a16e9ab0950106cb18ac6077/e/61485a0378d7a82e6cc495f2**

### Reflection
My approach to this part was mostly sound, though I did make a couple mistakes that I ended up needing to go back and fix. The first was assuming that the overhangs on the bottom and side were based on the 7.5mm fillet radius. I realized later that their height was not given because their tops needed to be tangent to the ring at the part's... axis of rotation(?) and also needed to be parallel to the sections they protruded from. My biggest challenge in modelling this part, however, was interpreting the sketch. I didn't have a reference model that could clarify my questions, so I had to do a little more deduction than I'm used to. For example, I initially didn't include the tangent panel on the bottom, which threw my mass off. 
