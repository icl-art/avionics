#This file implements a ringbuffer that should store the readings for the first n seconds

class RingBuffer:    

    def __init__(self, max_size):
        self.max_size = max_size
        self.buf = [[float()]*9] * self.max_size
        self.i = 0
    
    def add(self, reading):
        if self.i >= self.max_size:
            self.i = 0
        self.buf[self.i] = reading
        self.i += 1

    def __iter__(self):
        for i in range(self.max_size):
            yield self.buf[i]

#Example code
# rb = RingBuffer(4)

# for i in range(10):
#     rb.add([i, i+1, i+2])

# for i in rb:
#     print(i)