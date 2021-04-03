using namespace std;

#include "serialisation.h"

#include <stdio.h>
#include <iostream>
#include <string.h>

BYTE* to_bytes(float x) {
    static union {
        float x;
        BYTE bytes[4];
    } bytes;
    bytes.x = x;
    return bytes.bytes;
}


BYTE* serialise_floats(vector<float> floats) {
    int length = floats.size();
    BYTE* bytes = (BYTE*) malloc(length * sizeof(float));

    for (int i = 0; i < length; i++) {
        //Should check the return value isn't NULL
        memmove((void*) (bytes + i*sizeof(float)), to_bytes(floats[i]), sizeof(float));
    }
    return bytes;
}

//This is just for debugging
//Note this will print in little endian order, so 0000803f should be 3f800000 (1 in ieee754)
string to_string(const unsigned char* const bytes) {
    char hexstr[2*4*sizeof(float)+1];
    int i;
    for (i=0; i<4*sizeof(float); i++) {
        sprintf(hexstr+i*2, "%02x", bytes[i]);
    }
    hexstr[i*2] = 0;
    return hexstr;
}

//should print 0000803f000000400000404000008040
// int main() {
//     static const float arr[] = {1, 2, 3, 4};
//     vector<float> vec (arr, arr + sizeof(arr) / sizeof(arr[0]) );

//     auto bytes = serialise_floats(vec);
//     cout << to_string(bytes) << endl;
// }