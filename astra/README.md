# <ins>Astra</ins>

---

This document explains the design of the Astra Avionics System (AAS), as well as the associated testing and launch procedures.

### Contents

1. [Design](#Schematic)
2. [Testing](#Testing)
3. [Launch](#Launch)

## Schematic

Here is a basic schematic showing the overall design of the original AAS.

                                   +---------------+ 
                                   |    MPU6050    | 
                                   | Accelerometer | 
                                   +-------|-------+ 
                                           |         
                                           |         
                                           |         
         +-----------+             +-------v-------+ 
         | MPL3115A2 |             |    RP2040     | 
         | Altimeter -------------->     CPU       | 
         +-----------+             +-------|-------+ 
                                           |         
                                           |         
                                           |         
                                   +-------v-------+ 
                                   | Flash Storage | 
                                   |      2MB      | 
                                   +---------------+ 

**N.B.** The original flash size was 2MB - changed to 8MB after the first launch due to its insufficient size.
This system takes 20 sensor readings per second, which are stored in flash storage.

See [this commit](https://github.com/icl-art/avionics/commit/b56d4629c624b6bab54ca2577aa3f64e02a82ea5) for the code used in the first launch.

---

Here is the (tentative) schematic for the second iteration of the AAS.

      +---------------+             +---------+                    
      |  ICM-20649    |             | BMP390  |                    
      | Accelerometer --+           |Altimeter|                    
      | (Wide range)  | |           +----|----+                    
      +---------------+ |                |                         
                        |                |                         
      +---------------+ |           +----v---+          +---------+
      |    BNO085     --v-----------> RP2040 -----------> PAM8302 |
      | Accelerometer |             |  CPU   |          | Speaker |
      +---------------+             +----|---+          +---------+
                                         |                         
                                         |                         
                                         |                         
                                 +-------v-------+                 
                                 | Flash Storage |                 
                                 |      8MB      |                 
                                 +---------------+                 

Note: only one of the 2 accelerometers will be used.

Key differences:

* Either the BNO085 or ICM-20649 will replace the MPU6050
* The BMP390 will replace the MPL3115A2
* The PAM8302 speaker was added to assist in recovery

### Code

This system records data in the following format using 32 bit floating point numbers.

    0 1          31 32         63 64         95 96                                    191 192                                   383 384
     +-------------+-------------+-------------+-----------------------------------------+-----------------------------------------+
     |             |             |             |           Linear Acceleration           |         Rotational Acceleration         |
     | Time offset |  Pressure   | Temperature +-------------+-------------+-------------+-------------+-------------+-------------+
     |             |             |             |      x      |       y     |      z      |      x      |       y     |      z      |
     +-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+
    0 1          31 32         63 64         95 96        127 128       159 160       191 192       223 224       255 256       383 384

So each record uses 36 bytes, and since 20 records are taken per second, 720 bytes are needed to record 1 second of flight.
The simulated flight takes 120 seconds, which means that 86,400 bytes are used for the flight, which is significantly lower than 2MB.


The above calculation does not factor time spent at the launch pad, and the time taken to recover the rocket, which increases the data stored significantly.
One method of reducing the data is to trigger data recording at launch, using the accelerometer to detect launch.

However, some data may not be recorded as there is time between the actual launch and launch detection. This is fixed by using a ring buffer of 10 seconds of data.

---

During the first launch, 2 things went wrong with this method.

1. The system was programmed to only collect 120 seconds of data.
2. The accelerometer was triggered early.

Luckily it seems that the rocket launched soon after the incorrect detection, so some data was recovered.

---

### Performance hacks

* Writing to flash is much slower than writing to RAM, so we actually store the data in a buffer in RAM, and periodically flush it to flash.

* The RP2040 has Programmable IO and a DMA controller which can allow for readings to be taken asynchronously.

* The RP2040 has 2 cores, so the 2nd core can be used to provide nonblocking flash writes. Since we now use 2 cores, a synchronisation method needs to be provided. Either locks or using 2 buffers. - TODO: fill this in with benchmark results.


## Testing

The following parts can be unit tested:

* Ring buffer
* Data encoding/decoding

Since the rest of the system is tightly coupled with the hardware, the avionics bay will need to be tested before launch.

Tests include:

* It is impossible to trigger launch detection without an actual launch. This could be done by shaking the assembly.

* The data collected from the sensors is accurate. This could be done by manually triggering a launch event, and moving with the avionics bay.

## Launch procedures
