#Astra

This folder contains the code used for the Astra launch.

## Inventory
* Launch initialisation
* Data logger
* GPS recovery
* Pnut altitude tracking

## Lauch procedure
1. Just before launch, run the launch script, this should provide basic diagnostics as well as start the data logger.

2. If any errors are detected, postpone the launch by a few minutes until the errors disappear.

3. If all is well, launch.


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