#include <WiFi.h>
#include <Wire.h>
#include <Adafruit_MPL3115A2.h>

Adafruit_MPL3115A2 baro = Adafruit_MPL3115A2();

const char *ssid = "Bill Gates' 5G Cancer Ray";
const char *password = "YGF97T9BA8N";

int status = WL_IDLE_STATUS;
IPAddress server(192, 168, 8, 104); // Server address

void setup()
{
    Serial.begin(115200);
    Serial.println("Attempting to connect to WPA network...");
    Serial.print("SSID: ");
    Serial.println(ssid);

    while (!baro.begin()){
        Serial.println("Couldn't find sensor");
        delay(1000);
    }
    
    baro.setSeaPressure(99600);

    status = WiFi.begin(ssid, password);
    while(status != WL_CONNECTED){
        Serial.println("Couldn't get a wifi connection");
        delay(1000);
        status = WiFi.begin(ssid, password);
    }

    Serial.println("Connected to wifi");
}

void loop()
{
    float pascals = baro.getPressure();
    float tempC = baro.getTemperature();
    String queryString = "pressure="+String(pascals)+"&temperature="+String(tempC);

    Serial.print(pascals);
    Serial.println(" Pa");
    
    
    // Initialize the client library
    WiFiClient client;

    while (!client.connect(server, 8080))
    {
        Serial.println("Waiting for connection");
        delay(1000);
    }
    Serial.println("connected");
    // send HTTP header
    client.println("POST /get HTTP/1.1");
    client.println("Host: 192.168.8.104");
    client.println("user-agent: larryTheLauncher");
    client.println("accept: */*");
    client.println("Content-Length: " + String(queryString.length()));
    client.println("content-type: application/x-www-form-urlencoded");
    client.println(); // end HTTP header

    // send HTTP body
    client.println(queryString);
    client.stop()

    delay(200);
}
