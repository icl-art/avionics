#Astra

This folder contains the code used for the Astra launch.

## Inventory
* Launch initialisation
* Data logger
* GPS recovery
* Pnut altitude tracking

## Pre launch
Flash required files using push_fast.bat. This will compile all required libraries, and push all code to the Pico on COM 3 (this can be modified). Code will be configured to run automatically on boot. Pico must be reset for code to take effect.
If an error occurs, ensure the pico serial connection has not been captured by another program.

## Lauch procedure
0. Pin 22 must be shorted to ground to start logging code, to avoid accidental overwriting during data recovery.
1. Pico waits 10 minutes before starting the recording.
2. Pico records sensor data in a ring buffer with 5 seconds of data each time.
3. After the accelerometer magnitude exceeds ~4.5 G, break out of the ring buffer.
4. Once 120 seconds have elapsed, data recording is stopped. 

## Post launch
Run get_fast.bat. This will extract the data, run the parsing program, and plot the data in MATLAB. 

## Files

# serialisation.h
This converts a vector floats into a byte array.
Should be used when storing sensor readings into files.

# sensors.h
This file should contain all code related to reading sensors.
* Barometer
* Pnut
* Accelerometer
* Gyroscope
* GPS
* Temperature?
