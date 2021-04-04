import RPi.GPIO as GPIO
import time

PIN_A = 18
PIN_B = 23
PIN_C = 24
PIN_D = 25


def wave_step(pins: list, speed: float):
    for i in range(4):
        if i == 0:
            GPIO.output(pins[0], 1)
            GPIO.output(pins[1], 1)

        if i == 1:
            GPIO.output(pins[1], 1)
            GPIO.output(pins[2], 1)

        if i == 2:
            GPIO.output(pins[2], 1)
            GPIO.output(pins[3], 1)

        if i == 3:
            GPIO.output(pins[3], 1)
            GPIO.output(pins[0], 1)

        time.sleep(speed)
        for pin in pins:
            GPIO.output(pin, 0)


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_A, GPIO.OUT)
GPIO.setup(PIN_B, GPIO.OUT)
GPIO.setup(PIN_C, GPIO.OUT)
GPIO.setup(PIN_D, GPIO.OUT)
while True:
    wave_step([PIN_A, PIN_B, PIN_C, PIN_D], 0.01)
