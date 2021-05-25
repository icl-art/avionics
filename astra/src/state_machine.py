from abc import abstractmethod
from .serialisation import RING, NORMAL

try:
    import utime
    from machine import Pin
except ImportError:
    class utime:
        def sleep_ms(self):
            pass
        def sleep(self):
            pass
    class Pin:
        IN = 0
        OUT = 0
        def __init__(self, *_):
            pass
        def toggle(self):
            pass

class state:
    @abstractmethod
    def run(self):
        pass


CAPTURE_RATE = 20
MILLIS = 1000

led = Pin(25, Pin.OUT)
def indicate(msg):
    if msg:
        print(msg)
    led.toggle()

class idle(state):
    def __init__(self, buffer, sensors):
        self.buffer = buffer
        self.sensors = sensors

    def run(self) -> int:
        check = Pin(22, Pin.IN, Pin.PULL_UP)

        while check.value():
            utime.sleep(1)
            indicate("Waiting")
        return preflight(self.buffer, self.sensors)
    
class preflight(state):
    NEXT_STATE = 1
    ACCEL_THRESH = 4*4
    DELAY = MILLIS // (2 * CAPTURE_RATE)

    def __init__(self, buffer, sensors):
        self.buffer = buffer
        self.sensors = sensors

    def run(self) -> int:
        self.buffer.set_mode(RING)
        magnitude = 0
        while magnitude < self.ACCEL_THRESH:
            indicate(None)
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

    def run(self) -> int:
        self.buffer.set_mode(NORMAL)
        #TODO: Work out when to stop recording
        while True:
            try:
                indicate()
                data = self.sensors.get()
                self.buffer.write(data)
                utime.sleep_ms(self.DELAY)
            except:
                break
        indicate("Flight done")
        return postflight()

class postflight(state):
    def run(self) -> int:
        while True:
            indicate("Awaiting recovery")
            utime.sleep(1)