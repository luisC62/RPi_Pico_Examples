from machine import Pin
import utime
from ssd1306 import SSD1306_I2C

#I/O Configuration
led = Pin(28, Pin.OUT)
onboard_led = Pin(25, Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

#Set Initial Conditions
led.low()
onboard_led.high()
fast_blink = False

# attach the interrupt to the buttonPin

def alert(pin):
    global fast_blink
    #avoid rebounds
    utime.sleep(0.25)
    if button.value() == 1:
        if fast_blink:
            fast_blink = False
        else:
            fast_blink = True
        print("Se ha pulsado el botón")
    
button.irq(trigger = Pin.IRQ_RISING , handler = alert)

# Main Loop
while True:
    led.toggle()
    onboard_led.toggle()
    if fast_blink:
        utime.sleep(0.25)
    else:
        utime.sleep(1)