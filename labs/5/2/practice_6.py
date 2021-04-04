import RPi.GPIO as GPIO

INPUT_PIN_1 = 17
INPUT_PIN_2 = 23
RELAY_PIN_1 = 18
RELAY_PIN_2 = 24


GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_PIN_1, GPIO.IN)
GPIO.setup(INPUT_PIN_2, GPIO.IN)
GPIO.setup(RELAY_PIN_1, GPIO.OUT)
GPIO.setup(RELAY_PIN_2, GPIO.OUT)
while True:
    if GPIO.input(INPUT_PIN_1) == 1:
        GPIO.output(RELAY_PIN_1, 0)
    else:
        GPIO.output(RELAY_PIN_1, 1)

    if GPIO.input(INPUT_PIN_2) == 1:
        GPIO.output(RELAY_PIN_2, 0)
    else:
        GPIO.output(RELAY_PIN_2, 1)
