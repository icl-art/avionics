#ifndef SENSORS_H
#define SENSORS_H

//Reads a "frame" into a byte array, a frame is all the sensor information read during the flight
//Not GPS, but accelerometer/gyroscope etc
#define TIME_SIZE 8
#define N_SENSORS 1
#define FRAME_SIZE (TIME_SIZE + N_SENSORS * 4)
#define BYTE unsigned char
BYTE* read_frame(void);

#endif