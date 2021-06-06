from external import Pin, PWM
from external import sleep_ms
import struct

class Buzzer:

    def __init__(self, pin = 5):
        self.buzzer = PWM(Pin(pin))
        self.buzzer.duty_u16(1000)
        self.buzzer.freq(1000)

    def _playtone(self, frequency):
        self.buzzer.freq(frequency)

    def parse_song(self, data):
        tempo = struct.unpack_from("B", data, 0)[0]
        melody = []
        for i in range(1, len(data), 3):
            note = struct.unpack_from("H", data, i)[0]
            duration = struct.unpack_from("b", data, i+2)[0]
            melody += [note, duration]
        return (melody, tempo)

    def playsong(self, song):
        try:
            with open(song, "rb") as file:
                melody, tempo = self.parse_song(file.read())
                noteduration = 240000/tempo

                for i in range(0, len(melody) - 1, 2):
                    divider = melody[i+1]

                    sleeptime = 0
                    if divider > 0:
                        sleeptime = noteduration/divider
                    elif divider < 0:
                        sleeptime = 1.5*(noteduration/abs(divider))

                    print(melody[i])
                    if melody[i] != 0:
                        self._playtone(melody[i])
                    self.buzzer.duty_u16(1000)
                    sleep_ms(int(sleeptime*0.9))
                    self.buzzer.duty_u16(0)
                    sleep_ms(int(sleeptime*0.1))
        except FileNotFoundError:
            print("File not found ", song)
