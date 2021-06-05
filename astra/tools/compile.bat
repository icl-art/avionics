@echo off
TITLE Compiling Modules

cd ../src

ECHO Compiling Altimeter
mpy-cross -O[4] -march=armv7m MPL3115A2.py

ECHO Compiling MPU
mpy-cross -O[4] -march=armv7m MPU6050.py

ECHO Compiling Serialisation
mpy-cross -O[4] -march=armv7m serialisation.py

ECHO Compiling External
mpy-cross -O[4] -march=armv7m external.py

ECHO Compiling Sensors
mpy-cross -O[4] -march=armv7m sensors.py

ECHO Compiling State Machine
mpy-cross -O[4] -march=armv7m state_machine.py

REM ECHO Compiling copy
REM mpy-cross -O[4] -march=armv7m copy.py

REM ECHO Compiling types 
REM mpy-cross -O[4] -march=armv7m types.py

ECHO Complete
PAUSE