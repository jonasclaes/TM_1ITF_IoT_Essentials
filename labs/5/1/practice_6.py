import RPi.GPIO as GPIO
import time

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
GPIO.setup(LED_PIN, GPIO.OUT)
while True:
    sos(LED_PIN)
