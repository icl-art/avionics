#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <Adafruit_MPL3115A2.h>

Adafruit_MPL3115A2 baro = Adafruit_MPL3115A2();
Adafruit_MPU6050 mpu;

void setup(void) {
  //Serial.begin(115200);
  Serial.begin(500000);
  while (!Serial) {
    delay(10); // will pause Zero, Leonardo, etc until serial console opens
  }

  // Try to initialize!
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }

  while (!baro.begin()){
        Serial.println("Couldn't find sensor");
        delay(1000);
    }

  baro.setSeaPressure(102800);
  mpu.setAccelerometerRange(MPU6050_RANGE_16_G);
  mpu.setGyroRange(MPU6050_RANGE_250_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  Serial.println("");
  delay(100);
}

void loop() {
  // put your main code here, to run repeatedly:

  float pascals = baro.getPressure();
  float baro_temp = baro.getTemperature();
  /* Get new sensor events with the readings */
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  /* Print out the values */
  Serial.print(a.acceleration.x);
  Serial.print(",");
  Serial.print(a.acceleration.y);
  Serial.print(",");
  Serial.print(a.acceleration.z);
  Serial.print(", ");
  Serial.print(g.gyro.x);
  Serial.print(",");
  Serial.print(g.gyro.y);
  Serial.print(",");
  Serial.print(g.gyro.z);
  Serial.print(",");
  //Serial.print(pascals);
  //Serial.print(",");
  Serial.print(baro_temp);
  Serial.print(",");
  Serial.print(temp.temperature);
  Serial.println("");

  delay(10);
}
