from machine import Pin, PWM, Timer
import time 

mode = 1  
brightness = 0
fade_direction = 1  # 1 inc, -1 dec

led = PWM(Pin(15))
led.freq(1000)  

button = Pin(14, Pin.IN, Pin.PULL_DOWN)

def button_handler(pin):
    global mode
    time.sleep_ms(50)
    if pin.value() == 0:  # Button released
        if mode ==1:
            mode =2
        elif mode ==2:
            mode=3
        elif mode ==3:
            mode =1

button.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

# --- Timer callback: runs every 10 ms ---
def update_led(timer):
    global brightness, fade_direction, mode
    
    if mode == 2:  # Fade mode
        step = int(65535 / (200))  # 200 steps = 2 sec at 10 ms/step
        brightness += fade_direction * step
        
        if brightness >= 65535:
            brightness = 65535
            fade_direction = -1
        elif brightness <= 0:
            brightness = 0
            fade_direction = 1
        
        led.duty_u16(brightness)
    
    elif mode == 1:  #On
        led.duty_u16(70000)
        
    elif mode ==3: #off
        led.duty_u16(0)

timer = Timer()
timer.init(freq=100, mode=Timer.PERIODIC, callback=update_led)

while True:
    time.sleep(1)
#chatgpt helped with cleaning up the code and fixed some issues i had with the timer and button
#especially the timer
