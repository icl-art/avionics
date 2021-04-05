using namespace std;

#include "sensors.h"
#include <stdio.h>
#include "string.h"

// #include <Wire.h>
// #include <Adafruit_MPL3115A2.h>

// Adafruit_MPL3115A2 baro = Adafruit_MPL3115A2();
unsigned long millis(void) {
    return 4;
}

unsigned long boot_time = millis();

void init_sensors(void) {
    // Initialize the barometer
    // while (!baro.begin()){
    //     Serial.println("Couldn't find sensor");
    //     delay(1000);
    // }
    // baro.setSeaPressure(102800);
}

float getAltitude(void) {
    return 0.32;
}

#define APPEND_FRAME(VAR, TYPE) memcpy(frame + i, &VAR, sizeof(TYPE)); i += sizeof(TYPE);

BYTE* read_frame(void) {
    //Get sensor readings
    unsigned long timestamp = millis() - boot_time;
    float altitude = getAltitude();

    static BYTE frame[FRAME_SIZE];
    int i = 0;
    APPEND_FRAME(timestamp, unsigned long);
    APPEND_FRAME(altitude, float);
    return frame;
}

// void print_frame(BYTE frame[FRAME_SIZE]) {
//     unsigned long timestamp;
//     float altitude;
//     int i = 0;
//     memcpy(&timestamp, frame + i, sizeof(unsigned long)); i += sizeof(unsigned long);
//     memcpy(&altitude, frame + i, sizeof(float)); i += sizeof(float);
//     printf("Time: %ld, Altitude: %f", timestamp, altitude);
// }

int main(void) {
    for (int i = 0; i < 1; i++) {
        BYTE* frame = read_frame();
    }
}