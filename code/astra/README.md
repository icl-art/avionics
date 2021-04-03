#Astra

This folder contains the code used for the Astra launch.

## Inventory
* Launch initialisation
* Data logger
* GPS recovery
* Pnut altitude tracking

## Lauch procedure
1. Pico waits 5 minutes before starting the recording.
2. Pico records sensor data in a ring buffer with 5 seconds of data each time.
3. After the accelerometer magnitude is 3G, break out of the ring buffer.
4. When flash is full, stop recording.

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