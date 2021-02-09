#include <WiFi.h>
#include <Wire.h>
#include <Adafruit_MPL3115A2.h>

Adafruit_MPL3115A2 baro = Adafruit_MPL3115A2();

const char *ssid = "Bill Gates' 5G Cancer Ray";
const char *password = "YGF97T9BA8N";

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
  float pascals = baro.getPressure();
  float tempC = baro.getTemperature();
  String queryString = "pressure="+String(pascals)+"&temperature="+String(tempC);

  //Serial.print(pascals);
  //Serial.println(" Pa");
  
      // send HTTP header
  client.println("POST /get HTTP/1.1");
  client.println("Host: localhost");
  client.println("Content-Length: " + String(queryString.length()));
  client.println("Connection: close");
  client.println(); // end HTTP header

  // send HTTP body
  client.println(queryString);  
  Serial.println(queryString);
  delay(200);
}
