from machine import Pin, PWM

class Buzzer:

    def __init__(self, pin = 5):
        self.buzzer = PWM(Pin(5))
        self.state = False

    def _playtone(self, frequency):
        self.buzzer.freq(frequency)

    def toggle(self, frequency = NOTE_C5):
        tones = [0, frequency]
        self.state = not self.state
        self._playtone(self, tones[self.state])
