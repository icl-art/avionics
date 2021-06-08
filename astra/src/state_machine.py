from serialisation import RING, NORMAL, storage
from sensors import sensors

from external import utime, Pin, buzzer

class state:
    def run(self):
        pass


CAPTURE_RATE = 20
MILLIS = 1000

DATA_SIZE = 9 * 4
STORAGE_BUFFER_SIZE = 50 * CAPTURE_RATE #50 seconds
RING_BUFFER_SIZE = 20 * 2 * CAPTURE_RATE #20 seconds

FLIGHT_TIME = 5 * 60 * CAPTURE_RATE

led = Pin(25, Pin.OUT)
def indicate(msg):
    if msg:
        print(msg)
    led.toggle()

class idle(state):
    def run(self) -> state:
        check = Pin(4, Pin.IN, Pin.PULL_UP)

        while check.value():
            utime.sleep(1)
            indicate("Waiting")

        sensor = sensors()
        buffer = storage(STORAGE_BUFFER_SIZE*DATA_SIZE, 
                         RING_BUFFER_SIZE*DATA_SIZE, open("log.bin", "wb"))
        buzzer.playsong("nokia.txt")
        return preflight(buffer, sensor)
    
class preflight(state):
    NEXT_STATE = 1
    ACCEL_THRESH = 4*4
    DELAY = MILLIS // (2 * CAPTURE_RATE)

    def __init__(self, buffer, sensors):
        self.buffer = buffer
        self.sensors = sensors

    def run(self) -> state:
        self.buffer.set_mode(RING)
        magnitude = 0
        while magnitude < self.ACCEL_THRESH:
            data = self.sensors.get()
            x, y, z = data[3], data[4], data[5] #This isn't great - since preflight should not know the data format
            magnitude = x*x + y*y + z*z
            self.buffer.write(data)
            utime.sleep_ms(self.DELAY)
        return flight(self.buffer, self.sensors)

class flight(state):
    NEXT_STATE = 1
    DELAY = MILLIS // CAPTURE_RATE

    def __init__(self, buffer, sensors):
        self.buffer = buffer
        self.sensors = sensors

    def run(self) -> state:
        self.buffer.set_mode(NORMAL)
        #TODO: Work out when to stop recording
        i = 0
        while i < FLIGHT_TIME:
            try:
                indicate(None)
                data = self.sensors.get()
                print(i, data)
                self.buffer.write(data)
                utime.sleep_ms(self.DELAY)
            except Exception as e:
                print(e)
                break
            i += 1
        indicate("Flight done")
        self.buffer.close()
        buzzer.playsong("mario.txt")
        return postflight()

class postflight(state):
    def run(self) -> int:
        while True:
            indicate("Awaiting recovery")
            utime.sleep(1)