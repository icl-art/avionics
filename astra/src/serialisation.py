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

        self.reserve_buffer = bytearray(max_buffer_size)
        self.buffer_lock = _thread.allocate_lock()
        self.flush_sema = _thread.allocate_lock()
        self.flush_sema.acquire()
        _thread.start_new_thread(self.thread_1, ())

    #Readings is a tuple of the readings
    #Note a max_buffer_size must be divisible by the size of the readings
    def _write_normal(self, readings):
        if self.buffer_size >= self.max_buffer_size:
            self.flush_async()
        
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
        
    def flush_async(self):
        with self.buffer_lock:
            self.buffer, self.reserve_buffer = self.reserve_buffer, self.buffer
            self.buffer_size = 0
        self.flush_sema.release()

    def thread_1(self):
        while True:
            self.flush_sema.acquire()
            with self.buffer_lock:
                self.file.write(self.reserve_buffer)


    def close(self):
        self.flush()
        del self.buffer
        self.file.close()

    def set_mode(self, mode):
        if mode == NORMAL:
            self.write = self._write_normal
        elif mode == RING:
            self.write = self._write_ring

#Example code
# s = storage(1, open("test", "wb"))
# s.write([1.23, 4.56])
# s.write([7.89, 1234.124])
# s.close()