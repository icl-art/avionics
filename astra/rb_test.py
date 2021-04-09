from ring_buffer import RingBuffer

rb = RingBuffer(8)

for i in range(15):
    rb.add([i, i])

for val in rb:
    print (val)
