import time
from machine import SoftI2C, Pin
from esp32_i2c_1602lcd import I2cLcd
#from datetime import datetime

#now = datetime.now()

DEFAULT_I2C_ADDR = 0x27
i2c = SoftI2C(sda=Pin(15),scl=Pin(2),freq=100000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

for i in range(1, 100):
    lcd.clear()
    #current_time = now.strftime("%H:%M:%S")
    #lcd.putstr("当前时间 =", current_time)
    lcd.putstr("loading...{}\n".format(i))
    lcd.putstr("u10k")
    time.sleep(1)

# SDA GPIO15
# SCL GPIO2
# Vcc 5V （3V显示不清楚）
# GND GND

