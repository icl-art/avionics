import utime
from machine import I2C, Pin
import _thread
from MPL3115A2 import MPL3115A2 as mpl
import MPU6050
import serialisation

capture_time = 300
capture_rate = 10
delay = int(1000/capture_rate)
limit = capture_rate*capture_time
samples = 0

led = Pin(25, Pin.OUT)
check = Pin(22, Pin.IN, Pin.PULL_UP)

data = []

# initialise barometer
baro_i2c = I2C(0, scl=Pin(17), sda=Pin(16))
baro = mpl(baro_i2c, mode=mpl.PRESSURE)

# initialise MPU6050
mpu = MPU6050.MPU6050(bus = 1, scl = Pin(19), sda = Pin(18))
mpu.setGResolution(16)
mpu.setGyroResolution(500)

# create lock to prevent both threads accessing data together
lock = _thread.allocate_lock()

def get(rest=50):
    global led
    global data

    pressure = baro.pressure()
    temperature = baro.temperature()
    motion = mpu.readData()

    # lock data while updating
    lock.acquire()
    data = [pressure, temperature, 
    motion.Gx, motion.Gy, motion.Gz,
    motion.Gyrox, motion.Gyroy, motion.Gyroz]
    lock.release()    

    led.toggle()
    utime.sleep_ms(rest)



while check.value():
    print("Waiting")
    utime.sleep(1)

# initialise log file with 256 bit buffer
log = serialisation.storage(256, "log")

_thread.start_new_thread(get, ())

while samples < limit:
    lock.acquire()
    log.write(data)
    lock.release()
    samples = samples + 1
    utime.sleep_ms(delay)