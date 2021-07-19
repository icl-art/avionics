import time import sleep
from busio import UART
import board
import pwmio

rled = pwmio.PWMOut(board.LED_R, frequency=440)
gled = pwmio.PWMOut(board.LED_G, frequency=440)
bled = pwmio.PWMOut(board.LED_B, frequency=440)

def LED(r,g,b):
    rduty = int(65535 -(65535 * r/255))
    gduty = int(65535 -(65535 * g/255))
    bduty = int(65535 -(65535 * b/255))
    rled.duty_cycle = rduty
    gled.duty_cycle = gduty
    bled.duty_cycle = bduty

print("Initialising SIM")
LED(255, 0, 0)

sleep_ms = lambda n: time.sleep(n/1000)

with open("phone.number") as pno:
    OWNER_NUMBER = pno.readline()

print(OWNER_NUMBER)

SEND_DELAY_MS = 50


class sms:
    def __init__(self, rx, tx):
        self._uart = UART(baudrate=9600, rx=rx, tx=tx)

        # Perform self check
        if not self._check():
            ...  # TODO replace this with a buzz or something

        self._report()

        # TODO indicate sim setup complete

    def _send(self, cmd: str) -> str:
        self._uart.write(bytes((cmd+"\r\n").encode("ascii")))
        sleep_ms(SEND_DELAY_MS)
        resp = self._uart.read()
        if resp is None:
            return ""
        return resp.decode("ascii")

    def _check(self) -> bool:
        if "ok" not in self._send("at"):
            return False
        if "error" in self._send("at+ccid"):
            return False
        if "error" in self._send("at+creg?"):
            return False
        return True

    # Report will send commands to the sim800l and collect the responses.
    # Then the responses will be sent via sms to the "owner"
    def _report(self):
        rep = ""
        rep += self._send("at+csq")  # signal strength
        rep += self._send("AT+COPS?")  # connected network
        rep += self._send("AT+CBC")  # lipo state
        self.send_msg(rep)

    def send_msg(self, msg: str):
        self._send("AT+CMGF=1")  # Text message mode
        self._send(f"AT+CMGS=\"{OWNER_NUMBER}\"")
        self._send(msg)
        self._uart.write(bytes(chr(26)))

    def recv_msg(self) -> str:
        self._send("AT+CMGF=1")  # Text message mode
        self._send("AT+CNMI=1,2,0,0,0")  # Send text message over uart
        resp = ""
        while resp == "" or "+CMT" not in resp:
            resp = self._uart.read()
            if resp == None:
                resp = ""
        
        msg = resp.decode("ascii")
        words = msg.split("\r\n")
        return words[2]

# sim = busio.UART(baudrate = 9600, rx = board.GP5, tx = board.GP4)
sim = sms(board.GP5, board.GP4)


while True:
    voltage = sim._send("AT+CBC")
    sim.send_msg(voltage)
    time.sleep(0.5)