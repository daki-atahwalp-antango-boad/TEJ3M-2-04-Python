# This program turns the RGB on the breadboard on and cycles through all the colours
#
# Created by: Daki A.B
# Created on: Mar 2025

import time
import board
import digitalio

# variables
blink_time = 1

# setting RGB pins to output
pin_3 = digitalio.DigitalInOut(board.GP3)
pin_4 = digitalio.DigitalInOut(board.GP4)
pin_5 = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT

# running loop turning RGB on and cycling through colours
while True:
    pin_3.value = True
    pin_4.value = False
    pin_5.value = False
    time.sleep(blink_time)
    pin_3.value = False
    pin_4.value = True
    pin_5.value = False
    time.sleep(blink_time)
    pin_3.value = False
    pin_4.value = False
    pin_5.value = True
    time.sleep(blink_time)
    pin_3.value = True
    pin_4.value = True
    pin_5.value = False
    time.sleep(blink_time)
    pin_3.value = True
    pin_4.value = False
    pin_5.value = True
    time.sleep(blink_time)
    pin_3.value = False
    pin_4.value = True
    pin_5.value = True
    time.sleep(blink_time)
    pin_3.value = True
    pin_4.value = True
    pin_5.value = True
    time.sleep(blink_time)
