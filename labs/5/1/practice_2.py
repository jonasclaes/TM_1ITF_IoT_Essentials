import RPi.GPIO as GPIO
import time

LED_PIN_1 = 18
LED_PIN_2 = 23
LED_PIN_3 = 24
LED_PIN_4 = 25


def blink(pins):
    for pin in pins:
        GPIO.output(pin, 1)

    time.sleep(0.1)

    for pin in pins:
        GPIO.output(pin, 0)

    time.sleep(0.1)


GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)
GPIO.setup(LED_PIN_3, GPIO.OUT)
GPIO.setup(LED_PIN_4, GPIO.OUT)
while True:
    blink((LED_PIN_1, LED_PIN_2, LED_PIN_3, LED_PIN_4))
