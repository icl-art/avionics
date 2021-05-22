#This file implements a ringbuffer that should store the readings for the first n seconds

class RingBuffer:    

    def __init__(self, max_size, frame_size):
        self.max_size = max_size
        self.buf = [0.0] * max_size * frame_size
        self.frame_size = frame_size
        self.i = 0
    
    def add(self, reading):
        if self.i >= self.max_size*self.frame_size:
            self.i = 0

        next_i = self.i + self.frame_size
        self.buf[self.i:next_i] = reading
        self.i = next_i

    def __iter__(self):
        for i in range(0, self.max_size*self.frame_size, self.frame_size):
            reading = self.buf[i:self.frame_size + i]
            #if sum(reading) != 0:
            yield reading