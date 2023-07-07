#include <Wire.h>

int I2C_Address = 0x53;
float Xa, Ya, Za, pitch, roll;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  
  // Begin transmission with I2C Hex Address
  Wire.beginTransmission(I2C_Address);

  // Access POWER_CTL at 0x2D
  Wire.write(0x2D);

  // Send 0000 1000 (8) to enable D3 measure
  Wire.write(8);

  // End transmission
  Wire.endTransmission();
  delay(10);

  // Axis Corrections

  //(0x1E) OFSX (Offset X-Axis)

  Wire.beginTransmission(I2C_Address);
  Wire.write(0x1E); // X-axis offset register
  Wire.write(1);
  Wire.endTransmission();
  delay(10);

  //(0x1F) OFSY (Offset Y-Axis)

  Wire.beginTransmission(I2C_Address);
  Wire.write(0x1F); // Y-axis offset register
  Wire.write(1);
  Wire.endTransmission();
  delay(10);

  //(0x20) OFSZ (Offset Z-Axis)

  Wire.beginTransmission(I2C_Address);
  Wire.write(0x20); // Z-axis offset register
  Wire.write(-9);
  Wire.endTransmission();
  delay(10);

}

void loop() {
  Wire.beginTransmission(I2C_Address);
  Wire.write(0x32); // Starting point DATAX0
  Wire.endTransmission(false);
  Wire.requestFrom(I2C_Address, 6, true); // Reads DATAX0 through DATAZ1
  Xa = ( Wire.read()| Wire.read() << 8); // X-axis value
  Xa = Xa/256; 
  Ya = ( Wire.read()| Wire.read() << 8); // Y-axis value
  Ya = Ya/256;
  Za = ( Wire.read()| Wire.read() << 8); // Z-axis value
  Za = Za/256;

  // Pitch (X) Roll (Y)
  pitch = asin(Xa / sqrt(pow(Xa, 2) + pow(Ya, 2) + pow(Za, 2)));
  pitch = pitch * (180/PI);
  roll = atan(Ya / Za);
  roll = roll * (180/PI);

  //roll = atan2(Ya , Za) * 57.3;
  //pitch = atan2((- Xa) , sqrt(Ya * Ya + Za * Za)) * 57.3;

  Serial.print(roll);
  Serial.print(" ");
  Serial.println(pitch);

  delay(500);
}
