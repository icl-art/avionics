import utime
from machine import Pin

from .serialisation import storage, RING, NORMAL
from .state_machine import state, state_machine
from .sensors import sensors

CAPTURE_RATE = 20
MILLIS = 1000
STORAGE_BUFFER_SIZE = 256

led = Pin(25, Pin.OUT)
def indicate(msg):
    if msg:
        print(msg)
    led.toggle()

class idle(state):
    NEXT_STATE = 1

    def run(self) -> int:
        check = Pin(22, Pin.IN, Pin.PULL_UP)

        while check.value():
            utime.sleep(1)
            indicate("Waiting")
        return self.NEXT_STATE
    
class preflight(state):
    NEXT_STATE = 1
    ACCEL_THRESH = 4*4
    DELAY = MILLIS // (2 * CAPTURE_RATE)

    #TODO: Add a ring buffer mode to storage
    def __init__(self, buffer: storage, sensors: sensors):
        self.buffer = buffer
        self.sensors = sensors

    def run(self) -> int:
        self.log.set_mode(RING)
        magnitude = 0
        while magnitude < self.ACCEL_THRESH:
            indicate(None)
            data = self.sensors.get()
            x, y, z = data[3], data[4], data[5]
            magnitude = x*x + y*y + z*z
            self.buffer._write_normal(data)
            utime.sleep_ms(self.DELAY)
        return self.NEXT_STATE

class flight(state):
    NEXT_STATE = 1
    DELAY = MILLIS // CAPTURE_RATE

    def __init__(self, buffer: storage, sensors: sensors):
        self.buffer = buffer
        self.sensors = sensors

    def run(self) -> int:
        self.log.set_mode(NORMAL)
        #TODO: Work out when to stop recording
        while True:
            try:
                indicate()
                data = self.sensors.get()
                self.buffer._write_normal()
                utime.sleep_ms(self.DELAY)
            except:
                break
        indicate("Flight done")
        return self.NEXT_STATE

class postflight(state):
    def run(self) -> int:
        while True:
            indicate("Awaiting recovery")
            utime.sleep(1)

sens = sensors(indicate=indicate)
log = storage(STORAGE_BUFFER_SIZE, "log.bin")

machine = state_machine([
    idle(),
    preflight(log, sens),
    flight(log, sens),
    postflight()
])

utime.sleep(2)

machine.run()