#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

led_pin_1 = 12
led_pin_2 = 16
button_pin = 18

def blink(channel):
    t = time.time()
    print(t)
    with open("data.csv", 'a+') as outFile:
        outFile.write(str(t) + "\n")

    GPIO.output(led_pin_2, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(led_pin_2, GPIO.LOW)

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup([led_pin_1, led_pin_2], GPIO.OUT)
    GPIO.setup(button_pin, GPIO.IN)

    GPIO.output(led_pin_1, GPIO.LOW)
    GPIO.output(led_pin_2, GPIO.LOW)

    GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=blink, bouncetime=2000)

    try:
        while True:
            GPIO.output(led_pin_1, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(led_pin_1, GPIO.LOW)
            time.sleep(0.5)
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
