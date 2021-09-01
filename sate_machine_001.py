from machine import Pin, I2C
import utime

# Configure button hardware
onboard_led = Pin(25, Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Set initial conditions
onboard_led.high()
state = 0
print("Estado: ", state)

# attach the interrupt to the buttonPin
def alert(pin):
    #avoid rebounds
    global state
    utime.sleep(0.25)
    if button.value() == 1:
        if state == 0:
            state = 1
            print("Estado: ", state)
        elif state == 1:
            state = 2
            print("Estado: ", state)
        elif state == 2:
            state = 3
            print("Estado: ", state)
        elif state == 3:
            state = 0
            print("Estado: ", state)
            
button.irq(trigger = Pin.IRQ_RISING , handler = alert)

while True:
    if state==0:
        onboard_led.high()
    else:
        onboard_led.low()