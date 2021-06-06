#NOTE TO ANYONE WHO LOOKS AT THIS MONSTROSITY
#This file separates all the external dependencies from the rest of the codebase
#If you have to add any micropython specific dependencies, add them here
#When TEST_MODE is set, all dependencies will be mocked to avoid import issues

TEST_MODE = False
if TEST_MODE:
    from unittest.mock import Mock #Mock objects can do anything

    utime = Mock()
    sleep_ms = Mock()
    PWM = Mock()
    
    MPL3115A2 = Mock()
    MPU6050 = Mock()
    
    I2C = Mock()
    Pin = Mock()
    Pin.IN = 0
    Pin.OUT = 0
else:
    from utime import *
    from MPL3115A2 import *
    from MPU6050 import *
    from machine import I2C, Pin, PWM