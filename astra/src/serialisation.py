import struct
import _thread

_FLOAT_SIZE = 4

RING = 0
NORMAL = 1

class storage:
    def __init__(self, max_buffer_size, ring_buffer_size, file):
        self.max_buffer_size = max_buffer_size
        self.buffer_size = 0
        
        self.ring_buffer_size = ring_buffer_size
        self.buffer = bytearray(max_buffer_size)
        self.file = file
        self.write = self._write_normal   

    #Readings is a tuple of the readings
    #Note a max_buffer_size must be divisible by the size of the readings
    def _write_normal(self, readings):
        if self.buffer_size >= self.max_buffer_size:
            self.flush()
        
        for val in readings:
            self.buffer[self.buffer_size:] = struct.pack("f", val)
            self.buffer_size += _FLOAT_SIZE

    def _write_ring(self, readings):
        for val in readings:
            self.buffer[self.buffer_size:] = struct.pack("f", val)
            self.buffer_size += _FLOAT_SIZE
        
        self.buffer_size %= self.ring_buffer_size

    def flush(self):
        self.file.write(self.buffer)
        self.buffer_size = 0

    def close(self):
        self.flush()
        del self.buffer
        self.file.close()

    def set_mode(self, mode):
        if mode == NORMAL:
            self.write = self._write_normal
        elif mode == RING:
            self.write = self._write_ring