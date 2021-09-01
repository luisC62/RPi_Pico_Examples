from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

# Configuring onboard_led
onboard_led = Pin(25, Pin.OUT)
# Create the i2c object
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
# Create the display  object
oled = SSD1306_I2C(128, 64, i2c)

texto1="Hola?"
texto2="Hay alguien?"

onboard_led.high()

while True:
    oled.fill(0)
    oled.text(texto1, 0, 30)
    oled.show()
    utime.sleep(2)
    oled.fill(0)
    oled.text(texto2, 0, 30)
    oled.show()
    utime.sleep(2)

