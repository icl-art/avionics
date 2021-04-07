import utime
from machine import I2C, Pin, Timer
import _thread
from MPL3115A2 import MPL3115A2 as mpl
import MPU6050

led = Pin(25, Pin.OUT)
check = Pin(22, Pin.IN, Pin.PULL_UP)
cap = Timer()
data = []

baro_i2c = I2C(0, scl=Pin(17), sda=Pin(16))
baro = mpl(baro_i2c, mode=mpl.PRESSURE)

mpu = MPU6050.MPU6050(bus = 1, scl = Pin(19), sda = Pin(18))
mpu.setGResolution(16)
mpu.setGyroResolution(500)



def get(timer):
    global led
    global data
    pressure = baro.pressure()
    temperature = baro.temperature()
    motion = mpu.readData()
    data = [pressure, temperature, 
    motion.Gx, motion.Gy, motion.Gz,
    motion.Gyrox, motion.Gyroy, motion.Gyroz]
    
    led.toggle()


while check.value():
    print("Waiting")
    utime.sleep(1)

cap.init(freq = 10, mode=Timer.PERIODIC, callback = get)

while True:
    if check.value():
        print("Waiting")
    else:
        print(data)
    utime.sleep(1)
    