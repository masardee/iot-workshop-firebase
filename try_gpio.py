
#!/usr/bin/python

import os
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# setup our input pin

PUSH_BTN = 2
LED = 17

GPIO.setup(PUSH_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)
while True:
    if ( GPIO.input(PUSH_BTN) == False ):
        os.system('clear')
        print("Button Pressed")
        os.system('date') # print the systems date and time
        print GPIO.input(PUSH_BTN)
        GPIO.output(LED,GPIO.HIGH)
        sleep(5)
        GPIO.output(LED,GPIO.LOW)
    else:
        os.system('clear') # clear the screens text
        print ("Waiting for you to press a button")
        sleep(0.1)

