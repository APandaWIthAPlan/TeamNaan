import RPi.GPIO as GPIO
from time import sleep


def SnipSnip():
    pins = [4,6,13,17]
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    while True:
        for i in pins:
            if GPIO.input(i) == 0:
                sleep(1)
                if GPIO.input(i) == 0:
                    if i == 17:
                        return "win"
                    else:
                        return "bad"

