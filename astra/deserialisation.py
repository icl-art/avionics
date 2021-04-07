#This file doesn't go on the pico - use it to convert the text file
from sys import argv
import struct

def to_csv(filename, reading_size):
    csv = ""
    with open(filename, "rb") as f:
        data = bytearray(f.read())
        for i in range(0, len(data), reading_size):
            for j in range(0, reading_size, 4):
                csv += str(struct.unpack("f", data[i+j: i+j+4])[0])
                csv += ", "
            csv += "\n"

    with open(filename+".csv", "w") as f:
        f.write(csv)

if __name__ == "__main__":
    assert len(argv) == 3, "Expected 2 arguments - filename and reading size in bytes"
    filename = argv[1]
    reading_size = int(argv[2])
    to_csv(filename, reading_size)