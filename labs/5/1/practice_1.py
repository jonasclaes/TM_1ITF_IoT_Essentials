import RPi.GPIO as GPIO
import time

LED_PIN = 24


def blink(pin):
    GPIO.output(pin, 1)
    time.sleep(0.5)
    GPIO.output(pin, 0)
    time.sleep(0.5)


GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
while True:
    blink(LED_PIN)
