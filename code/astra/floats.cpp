#include <iostream>
#include <stdio.h>
#include <bitset>


#define BYTE unsigned char

BYTE* to_bytes(float x) {
    static union {
        float x;
        unsigned char bytes[4];
    } bytes;
    bytes.x = x;
    return bytes.bytes;
}

int main() {
    float x = 32.0f;
    union {
        float x;
        BYTE bytes[4];
    } bytes;
    bytes.x = x;
}