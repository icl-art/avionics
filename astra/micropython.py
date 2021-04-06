from machine import Pin, freq
from utime import sleep

led = Pin(25, Pin.OUT)

def blink(freq):
    t = 1/freq
    led.on()
    sleep(t)
    led.off()
    sleep(t)


while True:
    blink(9)