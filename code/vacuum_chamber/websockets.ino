#include <WiFi.h>
// #include <Wire.h>
// #include <Adafruit_MPL3115A2.h>

// Adafruit_MPL3115A2 baro = Adafruit_MPL3115A2();

const char* ssid = "Bill Gates' 5G Cancer Ray";
const char* password = "YGF97T9BA8N";

//const char* ssid = "DESKTOP-PHQVTQJ 8512";
//const char* password = "9#9z09K2";

int status = WL_IDLE_STATUS;
IPAddress server(192, 168, 8, 104);  // Google

// Initialize the client library
WiFiClient client;

void setup() {
  Serial.begin(115200);
  Serial.println("Attempting to connect to WPA network...");
  Serial.print("SSID: ");
  Serial.println(ssid);

  

  while(true){
    status = WiFi.begin(ssid, password);
    
     if ( status != WL_CONNECTED) {
      Serial.println("Couldn't get a wifi connection");
      Serial.println(status);
      delay(1000);
      //don't do anything else:
    }
    else {
      break;
    }
  }
  
  Serial.println("Connected to wifi");
  Serial.println("\nStarting connection...");
  // if you get a connection, report back via serial:

  while(true){
    if (client.connect(server, 8080)) {
      Serial.println("connected");
      // Make a HTTP request:
      client.println("GET /search?q=arduino HTTP/1.0");
      client.println();
      break;
    }

    else {
      Serial.println("Waiting for connection");
      delay(1000);
  }
  }
}

void loop() {

}

// void loop() {
//   // if (!baro.begin()) {
//  //  Serial.println("Couldn't find sensor");
//  //  return;
//    // }
//  WiFiClient client = server.available();
//  if (client.connected() && webSocketServer.handshake(client)) {
//    String data;
//    while (client.connected()) {
//      // float pascals = baro.getPressure();
//      // float tempC = baro.getTemperature();
//      // float altm = baro.getAltitude();
//      webSocketServer.sendData("5G radiation incoming");
//      delay(200);
//    }
//   Serial.println("The client disconnected");
//   delay(100);
//  }
  
//  delay(100);
// }