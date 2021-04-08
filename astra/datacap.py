import utime
from machine import I2C, Pin
import _thread
from MPL3115A2 import MPL3115A2 as mpl
import MPU6050
import serialisation
from ring_buffer import RingBuffer
from math import sqrt
from copy import deepcopy

capture_time = 300
capture_rate = 10
delay = int(1000/capture_rate)

# hard limit to avoid overflowing storage
limit = capture_rate*capture_time
samples = 0

led = Pin(25, Pin.OUT)
check = Pin(22, Pin.IN, Pin.PULL_UP)

# create data array
data = [float()]*10

while check.value():
    print("Waiting")
    utime.sleep(1)

# initialise barometer
baro_i2c = I2C(0, scl=Pin(17), sda=Pin(16))
baro = mpl(baro_i2c, mode=mpl.PRESSURE)

# initialise MPU6050
mpu = MPU6050.MPU6050(bus = 1, scl = Pin(19), sda = Pin(18))
mpu.setGResolution(16)
mpu.setGyroResolution(500)

# create lock to prevent both threads accessing data together
lock = _thread.allocate_lock()

start = utime.ticks_ms()

def get(rest=50):
    global led
    global data
    global start

    pressure = baro.pressure()
    temperature = baro.temperature()
    motion = mpu.readData()
    dt = utime.ticks_diff(utime.ticks_ms(), start)

    # lock data while updating
    lock.acquire()
    data[0] = dt
    data[1] = pressure
    data[2] = temperature
    data[3] = motion.Gx
    data[4] = motion.Gy
    data[5] = motion.Gz
    data[6] = motion.Gyrox
    data[7] = motion.Gyroy
    data[8] = motion.Gyroz

    lock.release()    

    led.toggle()
    utime.sleep_ms(rest)

_thread.start_new_thread(get, ())

buffer_size = 5 * capture_rate
rb = RingBuffer(buffer_size)
# initialise log file with 256 bit buffer
log = serialisation.storage(256, "log")

utime.sleep(2) # let modules settle, ignore initial invalid readings

magnitude = 0
# launch accel is ~ 110 m/s^2
while magnitude < 50:
    lock.acquire()
    reading = deepcopy(data)
    lock.release()
    magnitude = sqrt(reading[2]**2 + reading[3]**2 + reading[4]**2)
    rb.add(reading)
    

log.write(rb)

while samples < limit:
    lock.acquire()
    reading = deepcopy(data)
    lock.release()
    log.write(data)
    samples = samples + 1
    utime.sleep_ms(delay)