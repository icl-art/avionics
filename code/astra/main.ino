#include <Arduino.h>
#include "sensors.h"

#define sample_rate 20
#define start_lag 5
#define buffer_size 

void setup() {
    init_sensors();
}

void loop() {
    
}

// int main(void) {
//     const int sample_rate = 20;
//     const int start_buffer_size = FRAME_SIZE * sample_rate * 5;
//     BYTE* start_buffer = (BYTE*) malloc(start_buffer_size);

//     int i = 0;

//     //Pseudocode for the first 5 second recording
//     while (true) {
//         memcpy(start_buffer, read_frame(), FRAME_SIZE);
//         i += FRAME_SIZE;
//         if (i > start_buffer_size) {
//             i = 0;
//         }
//         //sleep(1000 / sample_rate);
//     }

//     //write start_buffer to flash
// }