int freq = 880;
int channel = 0;
int resolution = 8;

void setup() {
  // put your setup code here, to run once:
  

  Serial.begin(115200);
  ledcSetup(channel, freq, resolution);
  ledcAttachPin(13, channel);

  
  
  ledcWrite(channel, 200);
  
  
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int freq = 100; freq < 5000; freq = freq + 50){
  
     Serial.println(freq);
  
     ledcWriteTone(channel, freq);
     delay(500);
  }

  ledcWrite(channel, 0);
  delay(4000);
}
