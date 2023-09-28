from machine import Pin, PWM
import time

pwm2 = PWM(Pin(2))

pwm2.freq(1000)

while True:
    # 1.从不亮变亮
    for i in range(0, 1024, 1):
        pwm2.duty(i)
        time.sleep_ms(2)
    # 1.从不亮变亮
    for i in range(1023, -1, -1):
        pwm2.duty(i)
        time.sleep_ms(2)
