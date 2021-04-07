import utime
from machine import I2C, Pin, Timer
import _thread
from MPL3115A2 import MPL3115A2 as mpl
import MPU6050

led = Pin(25, Pin.OUT)
cap = Timer()
data = []

baro_i2c = I2C(0, scl=Pin(17), sda=Pin(16))
baro = mpl(baro_i2c, mode=mpl.PRESSURE)

def get(timer):
    global led
    global data
    pressure = baro.pressure()
    temperature = baro.temperature()
    data = [pressure, temperature]
    led.toggle()

cap.init(freq = 10, mode=Timer.PERIODIC, callback = get)

while True:
    utime.sleep(1)
    print(data)