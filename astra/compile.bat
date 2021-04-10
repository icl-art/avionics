@echo off
TITLE Compiling Modules

ECHO Compiling Altimeter
mpy-cross -O[4] -march=armv7m MPL3115A2.py

ECHO Compiling MPU
mpy-cross -O[4] -march=armv7m MPU6050.py

ECHO Compiling Ring Buffer
mpy-cross -O[4] -march=armv7m ring_buffer.py

ECHO Compiling Serialisation
mpy-cross -O[4] -march=armv7m serialisation.py

REM ECHO Compiling copy
REM mpy-cross -O[4] -march=armv7m copy.py

REM ECHO Compiling types 
REM mpy-cross -O[4] -march=armv7m types.py

ECHO Complete
PAUSE