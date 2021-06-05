from external import PWM, Pin

buzzer = PWM(Pin(5))

def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)
    buzzer.deinit()

# tones = [1000, 2000, 4000]