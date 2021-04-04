import RPi.GPIO as GPIO
import time

INPUT_PIN = 17
LED_PIN_1 = 18
LED_PIN_2 = 23
LED_PIN_3 = 24
LED_PIN_4 = 25


def running_light(pins: list, direction: int = 0):
    if direction == 1:
        pins.reverse()
    for pin in pins:
        GPIO.output(pin, 1)
        time.sleep(0.1)
        GPIO.output(pin, 0)
        time.sleep(0.1)


GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_PIN, GPIO.IN)
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)
GPIO.setup(LED_PIN_3, GPIO.OUT)
GPIO.setup(LED_PIN_4, GPIO.OUT)
while True:
    if GPIO.input(INPUT_PIN) == 1:
        running_light([LED_PIN_1, LED_PIN_2, LED_PIN_3, LED_PIN_4])
    else:
        running_light([LED_PIN_1, LED_PIN_2, LED_PIN_3, LED_PIN_4], 1)
