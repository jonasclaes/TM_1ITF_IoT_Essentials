import RPi.GPIO as GPIO
import time

INPUT_PIN = 17
LED_PIN = 24


def blink(pin):
    GPIO.output(pin, 1)
    time.sleep(0.5)
    GPIO.output(pin, 0)
    time.sleep(0.5)


GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
while True:
    if GPIO.input(INPUT_PIN) == 0:
        print("LED flashing")
        blink(LED_PIN)
    else:
        print("LED not flashing")
