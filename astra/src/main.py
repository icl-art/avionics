# from external import sleep

# from serialisation import storage
# from state_machine import state, idle
# from sensors import sensors

# STORAGE_BUFFER_SIZE = 256
# RING_BUFFER_SIZE = 80

# sens = sensors()
# log = storage(STORAGE_BUFFER_SIZE, RING_BUFFER_SIZE, "log.bin")

# sleep(2)

# state = idle(log, sens)
# while state:
#     state = state.run()

from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(5))

buzzer.duty_u16(1000)

def playtone(frequency):
    buzzer.freq(frequency)
    # buzzer.deinit()


while True:
    playtone(1000)
    sleep(1)
    playtone(2000)
    sleep(1)