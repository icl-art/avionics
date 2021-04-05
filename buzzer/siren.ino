int freq = 880;
int channel = 0;
int resolution = 8;

int hi = 2650;
int lo = 900;

void setup() {
  // put your setup code here, to run once: 

  Serial.begin(115200);
  ledcSetup(channel, freq, resolution);
  ledcAttachPin(13, channel);  
  
  ledcWrite(channel, 200); 
  
}


void loop() {
  // put your main code here, to run repeatedly:

  for (int freq = lo; freq < hi; freq = freq + 10){
  
     Serial.println(freq);
  
     ledcWriteTone(channel, freq);
     delay(20);
  }

  for (int freq = hi; freq > lo; freq = freq - 10){
  
     Serial.println(freq);
  
     ledcWriteTone(channel, freq);
     delay(20);
  }
}
