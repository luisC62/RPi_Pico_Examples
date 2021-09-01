import machine
from machine import Pin
# Configuring onboard_led
onboard_led = Pin(25, Pin.OUT)
# Configuring pins for i2c bus
sda=machine.Pin(0)
scl=machine.Pin(1)
# Creating i2c object
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)
# Executing scan. Store results in array devices
print('Scan i2c bus...')
devices=i2c.scan()
# Printing out the results
if len(devices)==0:
    print('No i2c devices found!')
else:
    print('Found ', len(devices), 'devices')

for device in devices:
    print("Decimal address: ", device, " | Hexa address: ", hex(device))
# Onboard led is on when the i2c bus is already scanned    
onboard_led.high()
