import utime
from machine import I2C, Pin, Timer
from MPL3115A2 import MPL3115A2 as mpl
import MPU6050
import serialisation
from ring_buffer import RingBuffer
from math import sqrt

capture_time = 30
capture_rate = 10
delay = 1000//capture_rate


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
    led.toggle()

print("Initialising Sensors")

datastream = Timer()
# initialise barometer
#baro_i2c = I2C(0, scl=Pin(17), sda=Pin(16))
#baro = mpl(baro_i2c, mode=mpl.PRESSURE)

# initialise MPU6050
mpu = MPU6050.MPU6050(bus = 1, scl = Pin(19), sda = Pin(18))
mpu.setGResolution(16)
mpu.setGyroResolution(500)

start = utime.ticks_ms()

def get(timer):
    global led
    global data
    global start
    
    #pressure = baro.pressure()
    #temperature = baro.temperature()
    motion = mpu.readData()
    dt = utime.ticks_diff(utime.ticks_ms(), start)

    data[0] = dt
    #data[1] = pressure
    #data[2] = temperature
    data[3] = motion.Gx
    data[4] = motion.Gy
    data[5] = motion.Gz
    data[6] = motion.Gyrox
    data[7] = motion.Gyroy
    data[8] = motion.Gyroz       

    #print("Data updated")
    

print("Starting acquisition")

datastream.init(freq = capture_rate, mode=Timer.PERIODIC, callback = get)

print("Starting data recording")
# faster data checking during trigger phase
buffer_size = 4 * capture_rate * 2
rb = RingBuffer(buffer_size)

# initialise log file with 256 bit buffer
log = serialisation.storage(256, "log.bin")

utime.sleep(2) # let modules settle, ignore initial invalid readings

magnitude = 0
print("Waiting for launch trigger")
# launch accel is ~ 110 m/s^2

while magnitude < 30:
    led.toggle()

    magnitude = sqrt(data[3]**2 + data[4]**2 + data[5]**2)
    rb.add(data)    

    utime.sleep_ms(delay//2)
    print(magnitude)

print("Launch detected")
log.write(rb)

while samples < limit:
    led.toggle()
    log.write(data)
    samples = samples + 1
    utime.sleep_ms(delay)

# post flight cleanup
log.close()

del log, rb

while True:
    led.toggle()
    utime.sleep(2)

