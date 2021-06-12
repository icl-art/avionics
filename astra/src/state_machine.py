from serialisation import NORMAL, storage
from sensors import sensors

from os import listdir
from external import utime, Pin, buzzer, Timer

class state:
    def run(self):
        pass


CAPTURE_RATE = 20
MILLIS = 1000

DATA_SIZE = 9 * 4
STORAGE_BUFFER_SIZE = 50 * CAPTURE_RATE #50 seconds

FLIGHT_TIME = 60 * CAPTURE_RATE

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
        buffer = storage(STORAGE_BUFFER_SIZE*DATA_SIZE,0, open("log{}.bin".format(n_logs), "wb"))
        buzzer.playsong("nokia.txt")
        return flight(buffer, sensor)
    
class flight(state):
    DELAY = MILLIS // CAPTURE_RATE

    def __init__(self, buffer, sensors):
        self.buffer = buffer
        self.sensors = sensors

    def run(self) -> state:
        self.buffer.set_mode(NORMAL)
        timer = Timer()
        i = 0
        def tick(timer):
            nonlocal i
            if i < FLIGHT_TIME:
                indicate(i)
                data = self.sensors.get()
                self.buffer.write(data)
                i += 1
            else:
                timer.callback(None)
                timer.deinit()
        
        timer.init(freq=CAPTURE_RATE, mode=Timer.PERIODIC, callback=tick)
        while i < FLIGHT_TIME:
            pass
        indicate("Flight done")
        self.buffer.close()
        buzzer.playsong("mario.txt")
        return postflight()

class postflight(state):
    def run(self) -> int:
        while True:
            indicate("Awaiting recovery")
            utime.sleep(1)