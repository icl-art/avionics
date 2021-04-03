#ifndef SENSORS_H
#define SENSORS_H

#include <vector>

//Reads a "frame" into a vector, a frame is all the sensor information read during the flight
//Not GPS, but accelerometer/gyroscope etc
vector<float> read_frame();

#endif