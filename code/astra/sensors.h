#ifndef SENSORS_H
#define SENSORS_H

//Reads a "frame" into a byte array, a frame is all the sensor information read during the flight
//Not GPS, but accelerometer/gyroscope etc
#define TIME_SIZE 8
#define N_SENSORS 8
#define FRAME_SIZE (TIME_SIZE + N_SENSORS * 4)
#define BYTE unsigned char

void init_sensors(void);
BYTE* read_frame(void);

#endif /* SENSORS_H */