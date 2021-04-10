import argparse
import struct
import os

def to_csv(ifname, ofname, reading_size):
    #reading_size = os.path.getsize(ifname)
    csv = ""
    with open(ifname, "rb") as f:
        data = bytearray(f.read())
        for i in range(0, len(data), reading_size):
            for j in range(0, reading_size, 4):
                csv += str(struct.unpack("f", data[i+j: i+j+4])[0])
                csv += ", "
            csv += "\n"

    with open(ofname, "w") as f:
        f.write(csv)

parser = argparse.ArgumentParser(description = 'Parsing Data Output')

parser.add_argument("--dir", "-d", type = str, help = "Path to working directory")
parser.add_argument("--input", "-i", type = str, help = "Input file name")
parser.add_argument("--output", "-o", type = str, help = "Output file name")

    
args = parser.parse_args()

if not args.input:
    ifname = "log.bin"
else:
    ifname = args.input

if not args.output:
    ofname = "log.csv"
else:
    ofname = args.output

os.chdir(args.dir)

print("Parsing data")
to_csv(ifname, ofname, 36)
print("Complete")
