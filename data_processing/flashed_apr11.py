import utime
from machine import I2C, Pin, PWM
from MPL3115A2 import MPL3115A2 as mpl
import MPU6050
import serialisation
from ring_buffer import RingBuffer

capture_time = 120
capture_rate = 20
delay = 1000//capture_rate
launch_del = delay//2


# hard limit to avoid overflowing storage
limit = capture_rate*capture_time
samples = 0

led = Pin(25, Pin.OUT)
check = Pin(22, Pin.IN, Pin.PULL_UP)

# create data array
data = [float()]*9

while check.value():
    print("Waiting")
    utime.sleep(1)
    led.toggle()

print("Initialising Sensors")

# initialise barometer
baro_i2c = I2C(1, scl=Pin(19), sda=Pin(18))
baro = mpl(baro_i2c, mode=mpl.PRESSURE)

# initialise MPU6050
mpu = MPU6050.MPU6050(bus = 0, scl = Pin(17), sda = Pin(16))
mpu.set_accel_range(16)
mpu.set_gyro_range(500)

start = utime.ticks_ms()

def get():
    global data
    global start
    
    try:
        pressure = baro.pressure()
        temperature = baro.temperature()
        motion = mpu.read()
        dt = utime.ticks_diff(utime.ticks_ms(), start)

        data[0] = dt
        data[1] = pressure
        data[2] = temperature
        data[3] = motion.Gx
        data[4] = motion.Gy
        data[5] = motion.Gz
        data[6] = motion.Gyrox
        data[7] = motion.Gyroy
        data[8] = motion.Gyroz       
    except:
        data = [float('nan')]*9
        print("Failed to get data")
    #print("Data updated")

# allow time to integrate hardware, self calibration    
print("Waiting for integration")
for _ in range(200):
    led.toggle()
    get()
    utime.sleep(3)

start = utime.ticks_ms()    

print("Starting acquisition")

print("Starting data recording")

 # create a 2 second ring buffer
 # launch detection is at 2x the frequency
buffer_size = 2 * capture_rate * 2
rb = RingBuffer(buffer_size, 9)

# initialise log file with 256 bit buffer
log = serialisation.storage(256, "log.bin")

utime.sleep(2) # let modules settle, ignore initial invalid readings

magnitude = 0
print("Waiting for launch trigger")
# launch accel is ~ 80 m/s^2

while magnitude < 16:
    led.toggle()
    get()
    #print(data)
    magnitude = data[3]**2 + data[4]**2 + data[5]**2
    rb.add(data)    

    utime.sleep_ms(launch_del)
    #print(magnitude)

print("Launch detected, dumping buffer")
log.dump(rb)
for val in rb:
    print(val)

del rb

print ("Buffer dumped, recording data")

while samples < limit:
    led.toggle()
    get()
    log.write(data)
    samples = samples + 1
    utime.sleep_ms(delay)

# post flight cleanup
print("Data capture complete, cleaning up")
log.close()

del log

print("Awaiting recovery")

while True:
    led.toggle()
    utime.sleep(1)
    

