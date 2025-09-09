from machine import Pin, PWM, Timer
from time import sleep

# SETUP
dimmer = PWM(Pin(15))
dimmer.freq(1000)

# 
while True:
    for duty in range(65536):
        dimmer.duty_u16(duty)
        sleep(.0001)
    for duty in range(65536,0,-1):
        dimmer.duty_u16(duty)
        sleep(.0001)

LOOP
