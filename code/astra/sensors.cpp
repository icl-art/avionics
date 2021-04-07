using namespace std;

#include "sensors.h"

#include "stdlib.h"
#include "string.h"

#include <Wire.h>
#include <Adafruit_MPL3115A2.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPL3115A2 baro = Adafruit_MPL3115A2();

unsigned long boot_time = millis();

void init_sensors(void) {
    // Initialize the barometer
    while (!baro.begin()){
        Serial.println("Couldn't find sensor");
        delay(1000);
    }
    baro.setSeaPressure(102800);

    while (!mpu.begin()) {
        Serial.println("Failed to find MPU6050 chip");
        delay(10);
    }
    mpu.setAccelerometerRange(MPU6050_RANGE_8_G); //TODO: set this
    mpu.setGyroRange(MPU6050_RANGE_500_DEG);
    mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
}

#define APPEND_FRAME(VAR, TYPE) memcpy(frame + i, &VAR, sizeof(TYPE)); i += sizeof(TYPE);

BYTE* read_frame(void) {
    //Get sensor readings
    unsigned long timestamp = millis() - boot_time;
    float altitude = baro.getAltitude();

    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);

    static BYTE frame[FRAME_SIZE]; //Note only 1 frame can exist at a time
    int i = 0;
    APPEND_FRAME(timestamp, unsigned long);
    APPEND_FRAME(altitude, float);
    APPEND_FRAME(a.acceleration.x, float);
    APPEND_FRAME(a.acceleration.y, float);
    APPEND_FRAME(a.acceleration.z, float);
    APPEND_FRAME(g.gyro.x, float);
    APPEND_FRAME(g.gyro.y, float);
    APPEND_FRAME(g.gyro.z, float);
    APPEND_FRAME(baro.getTemperature(), float);

    return frame;
}

void print_frame(BYTE frame[FRAME_SIZE]) {
    unsigned long timestamp;
    float altitude;
    int i = 0;
    memcpy(&timestamp, frame + i, sizeof(unsigned long)); i += sizeof(unsigned long);
    memcpy(&altitude, frame + i, sizeof(float)); i += sizeof(float);
    printf("Time: %ld, Altitude: %f", timestamp, altitude);
}