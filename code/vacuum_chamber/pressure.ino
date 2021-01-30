#include "WiFi.h"
#include <Wire.h>
#include <Adafruit_MPL3115A2.h>

Adafruit_MPL3115A2 baro = Adafruit_MPL3115A2();
 
void setup()
{
    Serial.begin(115200);
 
    // Set WiFi to station mode and disconnect from an AP if it was previously connected
    WiFi.mode(WIFI_STA);
    WiFi.disconnect();
    delay(100);

    baro.setSeaPressure(99600);
     
    Serial.println("Setup done");
}
 
void loop()
{
    Serial.println("scan start");
 
    // WiFi.scanNetworks will return the number of networks found
    int n = WiFi.scanNetworks();
    Serial.println("scan done");
    if (n == 0) {
        Serial.println("no networks found");
    } else {
        Serial.print(n);
        Serial.println(" networks found");
        for (int i = 0; i < n; ++i) {
            // Print SSID and RSSI for each network found
            Serial.print(i + 1);
            Serial.print(": ");
            Serial.print(WiFi.SSID(i));
            Serial.print(" (");
            Serial.print(WiFi.RSSI(i));
            Serial.print(")");
            Serial.println((WiFi.encryptionType(i) == WIFI_AUTH_OPEN)?" ":"*");
            delay(10);
        }
    }
    Serial.println("");
 
    // Wait a bit before scanning again
    delay(5000);

 if (! baro.begin()) {
    Serial.println("Couldn't find sensor");
    return;
    }

float pascals = baro.getPressure();
float tempC = baro.getTemperature();

Serial.println(pascals);
Serial.print(" Pa, ");
Serial.print(tempC); 
Serial.println("*C \n");
}