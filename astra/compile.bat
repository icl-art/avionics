@echo off
TITLE Compiling Modules

ECHO Compiling Altimeter
mpy-cross -O[4] -march=armv7m MPL3115A2.py

ECHO Compiling MPU
mpy-cross -O[4] -march=armv7m MPU6050.py 

ECHO Complete
PAUSE