from serialisation import RING, NORMAL, storage
from sensors import sensors

from os import listdir
from external import utime, Pin, buzzer

class state:
    def run(self):
        pass


CAPTURE_RATE = 20
MILLIS = 1000

DATA_SIZE = 9 * 4
STORAGE_BUFFER_SIZE = 50 * CAPTURE_RATE #50 seconds
PREFLIGHT_DELAY = 15 * 60 # 15 minutes

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
        
        n_logs = len(list(filter(lambda s: "log" in s, listdir())))
        if n_logs != 0:
            buzzer.playsong("miichannel.txt")
        buffer = storage(STORAGE_BUFFER_SIZE*DATA_SIZE, 0, open("log{}.bin".format(n_logs), "wb"))
        buzzer.playsong("nokia.txt")
        utime.sleep(PREFLIGHT_DELAY)
        return flight(buffer, sensor)
class flight(state):
    DELAY = MILLIS // CAPTURE_RATE

    def __init__(self, buffer, sensors):
        self.buffer = buffer
        self.sensors = sensors

    def run(self) -> state:
        self.buffer.set_mode(NORMAL)
        buzzer.playsong("nokia.txt")
        #TODO: Work out when to stop recording
        i = 0
        while i < FLIGHT_TIME:
            try:
                indicate(None)
                data = self.sensors.get()
                self.buffer.write(data)
                utime.sleep_ms(self.DELAY)
            except Exception as e:
                print(e)
                break
            i += 1
        indicate("Flight done")
        self.buffer.close()
        return postflight()

class postflight(state):
    def run(self) -> int:
        while True:
            buzzer.playsong("mario.txt")