#include "lcd.h"
#include "rfid.h"

void setup()
{
  Serial.begin(9600);
  lcd.begin(16,2);
  lcd.backlight();
  SPI.begin();      // Initiate  SPI bus
  mfrc522.PCD_Init();   // Initiate MFRC522
}
void loop()
{
  welcome_mssg();
  rfid_read();

  
}
