from machine import Pin, PWM, Timer
from time import sleep

# SETUP
dimmer = PWM(Pin(15))
dimmer.freq(1000)

# LOOP
while True:
    for duty in range(90000):
        dimmer.duty_u16(duty)
        sleep(.000009)
    for duty in range(65536,0,-1):
        dimmer.duty_u16(duty)
        sleep(.0009)

