from ring_buffer import RingBuffer

rb = RingBuffer(8)

for i in range(200):
    rb.add([i, i])

for val in rb:
    print (val)
