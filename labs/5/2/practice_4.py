import RPi.GPIO as GPIO
import time

INPUT_PIN = 17
LED_PIN = 18


def pulse(pin: int, pulses: int, time_on: float, time_off: float):
    for num in range(3):
        GPIO.output(pin, 1)
        time.sleep(time_on)
        GPIO.output(pin, 0)
        time.sleep(time_off)


def sos(pin: int):
    pulse(pin, 3, 0.5, 0.5)
    pulse(pin, 3, 1.5, 0.5)
    pulse(pin, 3, 0.5, 0.5)


GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
while True:
    if GPIO.input(INPUT_PIN) == 1:
        sos(LED_PIN)
