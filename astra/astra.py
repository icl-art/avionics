import utime
from machine import I2C, Pin, Timer
import MPL3115A2
import MPU6050

#--------------------------
       
led = Pin(25, Pin.OUT)
tim = Timer()

def tick(timer):
    global led
    led.toggle()

tim.init(freq = 5, mode=Timer.PERIODIC, callback=tick)
utime.sleep(5)

i = 0
#tim.init(freq = 10)

f = open("out.csv", "w")
f.write("T,i\n")
start = utime.ticks_ms()
print(start)

while i < 20:
    
    dt = utime.ticks_diff(utime.ticks_ms(), start)
    line = "%d,%d\n" % (dt, i)
    print(line)
    f.write(line)
    i = i + 1
    utime.sleep(1)

#tim.init(freq = 5)
#utime.sleep(5)

f.close()
