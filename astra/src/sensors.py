import utime
from machine import I2C, Pin
from MPL3115A2 import MPL3115A2 as mpl
import MPU6050

class sensors:

    _data = [float()] * 9
    _start = utime.ticks_ms()

    def __init__(self, indicate=(lambda: ...)):
        self._indicate = indicate

        #initialise MPL3115A2
        baro_i2c = I2C(1, scl=Pin(19), sda=Pin(18))
        self._baro = mpl(baro_i2c, mode=mpl.PRESSURE)

        # initialise MPU6050
        self._mpu = MPU6050.MPU6050(bus = 0, scl = Pin(17), sda = Pin(16))
        self._mpu.set_accel_range(16)
        self._mpu.set_gyro_range(500)

        #self calibrate hardware
        for _ in range(200):
            self._indicate()
            self.get()
            utime.sleep(3)
    

    def get(self) -> list[float]:
        pressure = self._baro.pressure()
        temperature = self._baro.temperature()
        motion = self._mpu.read()
        dt = utime.ticks_diff(utime.ticks_ms(), self._start)

        try:
            self._data[0] = dt
            self._data[1] = pressure
            self._data[2] = temperature
            self._data[3] = motion.Gx
            self._data[4] = motion.Gy
            self._data[5] = motion.Gz
            self._data[6] = motion.Gyrox
            self._data[7] = motion.Gyroy
            self._data[8] = motion.Gyroz       
        except:
            self._data = [float('nan')]*9
            print("Failed to get data")
        finally:
            return self._data