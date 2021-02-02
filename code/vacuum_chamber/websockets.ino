#include <WiFi.h>
#include <Wire.h>
#include <Adafruit_MPL3115A2.h>

// Adafruit_MPL3115A2 baro = Adafruit_MPL3115A2();

const char *ssid = "Bill Gates' 5G Cancer Ray";
const char *password = "YGF97T9BA8N";

//const char* ssid = "DESKTOP-PHQVTQJ 8512";
//const char* password = "9#9z09K2";

int status = WL_IDLE_STATUS;
IPAddress server(192, 168, 8, 104); // Server address

// Initialize the client library
WiFiClient client;

void setup()
{
    Serial.begin(115200);
    Serial.println("Attempting to connect to WPA network...");
    Serial.print("SSID: ");
    Serial.println(ssid);
    baro.setSeaPressure(99600);

    status = WiFi.begin(ssid, password);
    do
    {
        Serial.println("Couldn't get a wifi connection");
        Serial.println(status);
        delay(1000);
    } while (status != WL_CONNECTED);

    Serial.println("Connected to wifi");
    Serial.println("\nStarting connection...");

    while (!client.connect(server, 8080))
    {
        Serial.println("Waiting for connection");
        delay(1000);
    }
    Serial.println("connected");
}

void loop()
{
    if (!baro.begin())
    {
        Serial.println("Couldn't find sensor");
        return;
    }

    float pascals = baro.getPressure();
    float tempC = baro.getTemperature();

    client.printf("GET /%fAVIONICSISTHEBEST%f HTTP/1.0", pascals, tempC);
    delay(1000);
}