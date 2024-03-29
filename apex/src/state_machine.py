# The state machine has 5 states:
# 1. Diagnostic - all peripherals are initialised
# 2. Calibration - the accelerometer is calibrated
# 3. Preflight - calibrates all sensors, and waits for a text message containing the message "launch".
# 4. Flight - takes readings from sensors for FLIGHT_TIME minutes.
# 5. Postflight - takes gps readings and sends them to GROUND_CONTROL_PHONE, until a "Received" is received.
#                 It also plays sounds over the speakers, in case the earlier method failed

import struct
from time import sleep, monotonic_ns
import board
from busio import I2C

from sensors import sensors, millis
from gps import gps
from sms import sms
from led import LED
from speaker import Speaker

led = LED()
led.colour(255, 255, 255)
led.on()

speaker = Speaker()


def sleep_ms(ms):
    sleep(ms//1000)


i2c = I2C(scl=board.GP27, sda=board.GP26, timeout=10000000, frequency=400_000)

class state:
    def __init__(self, sms, sensors, gps):
        self._sms = sms
        self._sensors = sensors
        self._gps = gps

    def run(self):
        raise NotImplementedError("Not implemented")

class diagnostic(state):
    def __init__(self):
        pass
    
    def run(self):
        sms_ = sms(rx=board.GP5, tx=board.GP4)
        sensors_ = sensors(i2c)
        gps_ = gps(i2c, 1000)
        sms_.send_msg("gps+sensors ok")
        sleep_ms(50)
        sms_.report()
        print("Done")
        return calibration(sms_, sensors_, gps_)

class calibration(state):
    def run(self):
        led.colour(0, 255, 0)
        led.on()
        self._sms.send_msg("Calibrating")
        self._sensors.calibrate()
        led.colour(255, 0, 255)
        self._sms.send_msg("Calibrated")
        while self._sms.recv_msg(led) != "ok":
            pass
        return preflight(self._sms, self._sensors, self._gps)

class preflight(state):
    def run(self):
        led.colour(0, 0, 255)
        self._sms.send_msg("Send 'la'")
        while self._sms.recv_msg(led) != "la":
            pass
        self._sms.send_msg("launching")
        return flight(self._sms, self._sensors, self._gps)

class flight(state):
    _capture_rate = 20
    _delay = 1000//_capture_rate
    _flight_time = 30 * _capture_rate  # 5 minutes of flight

    def __init__(self, sms, sensors, gps):
        super(flight, self).__init__(sms, sensors, gps)
        self._sensor_storage = open("log.bin", "wb")

    def run(self):
        i = 0
        led.colour(255, 0, 0)

        #Problem:
        #Sim module will need long (50ms+) waits to work
        #But we can't afford that in a single threaded environment
        #Solution:
        #Use pkt_wait to provide the sleeps
        # pkt_wait = 1
        # pkt = bytearray(32 * 4)
        # self._sms.connect()

        while i < self._flight_time:
            # pkt_wait -= 1
            i += 1
            start = millis()
            data = self._sensors.get()
            for reading in data:
                self._sensor_storage.write(struct.pack("f", reading))

            # if pkt_wait == 0:
            #     pkt[0:4] = struct.pack("f", data[0]) #time
            #     for j in range(4):
            #         pkt[4*j:4*(j+1)] = struct.pack("f", data[j+4])
                
            #     pkt[20:24] = struct.pack("f", data[10]) #altitude
                
            #     lat, lon, _ = self._gps.get_loc()
            #     pkt[20:24] = struct.pack("f", lat)
            #     pkt[24:28] = struct.pack("f", lon)
                # pkt_wait = self._sms.send_pkt(pkt)
            end = millis()
            sleep_ms(max(0, self._delay - (end - start)))

        self._sensor_storage.flush()
        self._sensor_storage.close()
        # self._sms.disconnect()
        return postflight(self._sms, self._gps)


class postflight(state):
    def __init__(self, sms, gps):
        super(postflight, self).__init__(sms, None, gps)

    def run(self):
        led.colour(0, 255, 255)
        for _ in range(2):
            self._sms.send_msg_all("Landed")
            sleep(10)
        sleep(2)
        for _ in range(5):
            self._sms.send_msg_all(self._gps.create_msg())
            sleep(60)
           
        sleep(60)

        while True:
            speaker.siren()
            sleep(45)
            speaker.shutup()
            speaker.noise()
            sleep(45)
            speaker.shutup()
        