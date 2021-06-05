from machine import Pin, PWM

buzzer = PWM(Pin(5))

def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)


tones = [1000, 2000, 4000]