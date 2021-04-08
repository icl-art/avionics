#Note convert the libraries marked with "u" to micropython libraries (by adding a u)
import utime
import struct

FLOAT_SIZE = 4

class storage:
    def __init__(self, max_buffer_size, filename):
        self.max_buffer_size = max_buffer_size
        self.buffer_size = 0
        self.buffer = bytearray(max_buffer_size)
        self.file = open(filename, "wb")

    #Readings is a tuple of the readings
    #Note a max_buffer_size must be divisible by the size of the readings
    def write(self, readings):
        if self.buffer_size >= self.max_buffer_size:
            self.flush()
        
        for val in readings:
            self.buffer[self.buffer_size:] = struct.pack("f", val)
            self.buffer_size += FLOAT_SIZE

    def flush(self):
        self.file.write(self.buffer)
        self.buffer = bytearray(self.max_buffer_size)
        print(f"Wrote {self.buffer_size} bytes")
        self.buffer_size = 0
        
    def close(self):
        self.flush()
        del self.buffer
        self.file.close()


#Example code
# s = storage(1, "test")
# s.write([1.23, 4.56])
# s.write([7.89, 1234.124])
# s.close()