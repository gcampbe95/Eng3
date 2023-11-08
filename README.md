# ENG3_Documentation

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Ultrasonic_Rainbow](#Ultrasonic_Rainbow)
* [Motor_Control](#Motor_Control)
* [Onshape_Hanger](#Onshape_Hanger)
* [Swing_Arm](#Swing_Arm)
* [2Button_Servo](#2Button_Servo)
* [VBlock](#VBlock)
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

![](https://github.com/gcampbe95/Eng3/blob/main/Part%20Studio%201%20Copy%201%20(2).png)
![](https://github.com/gcampbe95/Eng3/blob/main/Part%20Studio%201%20Copy%201%20(3).png)

### Part Link
The finished part can be found here: 

**[Block Hanger](https://cvilleschools.onshape.com/documents/f4db0690df87f7004a8dc5cf/w/95766ec79d0166b3b0bb6b30/e/cfd029d9d43e634cbc7a784f)**

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

**[Swing Arm](https://cvilleschools.onshape.com/documents/e16d436a118fe77fed8a7da4/w/a16e9ab0950106cb18ac6077/e/61485a0378d7a82e6cc495f2)**

### Reflection
My approach to this part was mostly sound, though I did make a couple mistakes that I ended up needing to go back and fix. The first was assuming that the overhangs on the bottom and side were based on the 7.5mm fillet radius. I realized later that their height was not given because their tops needed to be tangent to the ring at the part's... axis of rotation(?) and also needed to be parallel to the sections they protruded from. My biggest challenge in modelling this part, however, was interpreting the sketch. I didn't have a reference model that could clarify my questions, so I had to do a little more deduction than I'm used to. For example, I initially didn't include the tangent panel on the bottom, which threw my mass off. 

## 2Button_Servo

### Description & Code Snippets
In this assignment the task was to control a servo with two buttons, where one moved the servo to the right and the other moved it to the left.  

I started with writing a simple function that recognizes when a button is pressed. It looks like this:

```Python
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
```
That part was honestly a little tricky, because it was a new way of doing pwm and I needed a refresher on pulldown, but I only needed to make a few adjustments to incorporate servo control. I started by declaring a variable, curangle, that would correspond to the servo's angle and be modified by the button. The first issue Ihad with this was that with lines that look like this...
```Python
curangle = curangle + 5
```
... angles can exceed 180 and get stuck. To avoid this, I added:
```Python
if curangle <= 174: # prevents the angle from getting above 180
```
... and the finished code looked like this:
```Python
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

```

### Evidence

![](https://github.com/gcampbe95/Eng3/blob/main/ezgif-1-db40b96bb7%20(1).gif)

### Wiring
Wiring for this code can be found here: 
**[2Button Wiring](https://www.tinkercad.com/things/5sdIopFZdMf)**

![](https://github.com/gcampbe95/Eng3/blob/main/Screenshot%202023-10-24%20123652.png)

### Reflection
Before this assignment, I was still pretty unfamiliar with pulldown and needed some practice with using pwm in CircuitPython. For this, it was helpful to break it down into just the button and just the servo. Where the button is concerned, Alexis helped me with pulldown and I now feel confident integrating it into other assignments, and I also know that having the isolated code will be useful in the future. On the servo side, my initial code had it getting stuck when the angle got above 180 or fell below 0, so I added "if" statements that prevented this. 

## VBlock 

### Description 
In this assignment we modelled a "V block" and then modified it based on a series of drawings. It was deceptively tricky, because I initially sacrificed a lot of accuracy for speed, which ended up costing me time. The most efficient way to approach this was to model 1/4 of the block and then use a part mirror to reflect it across the front and right planes. I usually use sketch mirrors, but apparently they're bad, so I avoided them for this model and it was definitely easier to make changes. The most important part here was paying close attention during the first question and taking the little bit of extra time to check each subsequent drawing to make sure every change was included.

### Evidence

![](https://github.com/gcampbe95/Eng3/blob/main/vblock.png)
![](https://github.com/gcampbe95/Eng3/blob/main/vblock2.png)
![](https://github.com/gcampbe95/Eng3/blob/main/vblock3.png)


### Part Link
The finished part can be found here: 

**[V Block](https://cvilleschools.onshape.com/documents/883d46fc4e0ec8cb44f43a23/w/65ace9810c27842f6c57f290/e/85d305785d1342d48913fa3d)**

### Reflection
There were a couple places in this assignment where I modelled one question, made it a version, moved on to the next question, and realized a bunch of updates later that I had something wrong in question 1 that I had missed because I didn't pay attention. Modelling the V Block could've been very simple if I had approached it as efficiently as possible. I did this in some ways (modelling 1/4 of the block and mirroring, using offset instead of dimensioning the outer lip edge by edge) but didn't in others (rushing through the first model instead of spending time getting a solid fundation so I could fly throught the modifications). Overall, I need to work on paying a little more attention in the instructions for a part's original version.   

## Multipart_Practice

### Description 
In this assignment we practiced using multi-part studios 

### Evidence

![](https://github.com/gcampbe95/Eng3/blob/main/strawberry.png)
![](https://github.com/gcampbe95/Eng3/blob/main/strawberry2.png)
![](https://github.com/gcampbe95/Eng3/blob/main/strawberry3.png)


### Part Link
The finished part can be found here: 

**[Multipart_Practice](https://cvilleschools.onshape.com/documents/9b86490b563a922655dea0dd/w/1956fef4e77daf394fecfe80/e/cf003c400780411b931a3afb)**

### Reflection
There were a couple places in this assignment where I modelled one question, made it a version, moved on to the next question, and realized a bunch of updates later that I had something wrong in question 1 that I had missed because I didn't pay attention. Modelling the V Block could've been very simple if I had approached it as efficiently as possible. I did this in some ways (modelling 1/4 of the block and mirroring, using offset instead of dimensioning the outer lip edge by edge) but didn't in others (rushing through the first model instead of spending time getting a solid fundation so I could fly throught the modifications). Overall, I need to work on paying a little more attention in the instructions for a part's original version.   