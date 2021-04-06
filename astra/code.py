import board
import time
import storage
import digitalio
 
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

try:
    with open("/out.txt", "w") as datalog:
        i = 0
        while i<20:
            print(i)
            led.value = True
            time.sleep(0.1)
            datalog.write("on\n")
            datalog.flush()
            led.value = False
            time.sleep(0.1)
            datalog.write("off\n")
            datalog.flush()
            i = i + 1            
except:    
    print("oh no")
    raise

with open("/out.txt", "r") as datalog:
    for line in datalog:
        print(line)
