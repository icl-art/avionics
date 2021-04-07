import utime
from machine import I2C, Pin, Timer
import _thread
#import MPL3115A2
#import MPU6050

#--------------------------
       
led = Pin(25, Pin.OUT)
tim = Timer()

def tick(timer):
    global led
    led.toggle()

def blink(hz):
    global tim

    tim.init(freq = hz, mode=Timer.PERIODIC, callback=tick)


def write():
    f = open("out.csv", "w")
    f.write("T,i\n")
    start = utime.ticks_ms()
    i = 0
    while i < 10:    
        dt = utime.ticks_diff(utime.ticks_ms(), start)
        line = "%d,%d\n" % (dt, i)
        print(line)
        f.write(line)
        i = i + 1
        utime.sleep(1)

    f.close()

print("Starting thread")
_thread.start_new_thread(write, ())

print("Normal Code")

j = 1

while j < 20:
    print(j)
    blink(j)
    utime.sleep(5)
    j = j + 1