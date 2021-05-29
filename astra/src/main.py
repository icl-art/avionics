from .external import utime

from .serialisation import storage
from .state_machine import state, idle
from .sensors import sensors

STORAGE_BUFFER_SIZE = 256
RING_BUFFER_SIZE = 80

sens = sensors()
log = storage(STORAGE_BUFFER_SIZE, RING_BUFFER_SIZE, "log.bin")

utime.sleep(2)

state = idle()
while state:
    state = state.run()