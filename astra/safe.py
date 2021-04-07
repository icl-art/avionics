import utime
from machine import I2C, Pin, Timer
import _thread

led = Pin(25, Pin.OUT)
tim = Timer()

def tick(timer):
    global led
    led.toggle()

def blink(hz):
    global tim

    tim.init(freq = hz, mode=Timer.PERIODIC, callback=tick)

print("Intialising Pin")
check = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    if check.value():
        print("Pin On")
        blink(10)
    else:
        # short pin 15 to ground to write file, otherwise it'll keep it for reading
        print("Pin Off")
        blink(1)
    utime.sleep(2)